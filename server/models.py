from sqlalchemy import Column, Integer, String, Date, ForeignKey
from sqlalchemy.orm import relationship, validates
from datetime import datetime
from sqlalchemy.ext.hybrid import hybrid_property
from config import db, bcrypt

favorite = db.Table(
    'favorite',
    db.Column('user_id', db.Integer, db.ForeignKey('users.id')),
    db.Column('fav_user_id', db.Integer, db.ForeignKey('users.id'))
)

class User(db.Model):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False)
    birthday = Column(String(50), nullable=False)
    username = Column(String(50), nullable=False)
    _password_hash = Column(String, nullable=False)
    astrological_sign_id = Column(Integer, ForeignKey('astrological_signs.id'))
    image_url = db.Column(db.String, nullable=True)

    favorites = db.relationship('User', 
                                secondary = favorite, 
                                primaryjoin = (favorite.c.user_id == id),
                                secondaryjoin = (favorite.c.fav_user_id == id),
                                backref = 'matches'
                                )
    
    def mutual_matches(self):
        # This method checks for mutual matches by comparing favorites and favorited_by lists
        matches = [user for user in self.favorites if self in user.favorites]
        return matches

    @hybrid_property
    def password_hash ( self ) :
        return self._password_hash
    
    @password_hash.setter
    def password_hash ( self, password ) :
        if password:
            password_hash = bcrypt.generate_password_hash ( password.encode( 'utf-8' ) )
            self._password_hash = password_hash.decode( 'utf-8' )
        else :
            self.validation_errors.append( "Password validation error goes here!" )

    def authenticate ( self, password ) :
        return bcrypt.check_password_hash( self._password_hash, password.encode( 'utf-8' ) )

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'birthday': self.birthday,
            'username': self.username,
            'astrological_sign': self.astrological_sign.to_dict(),
            'image_url': self.image_url
        }


    @validates('name')
    def validate_name(self, key, name):
        if not name:
            raise ValueError("Name must be provided.")
        return name

    @validates('username')
    def validate_username(self, key, username):
        if not username:
            raise ValueError("Username must be provided.")
        return username

    @validates('astrological_sign_id')
    def validate_astrological_sign_id(self, key, astrological_sign_id):
        if not astrological_sign_id:
            raise ValueError("Valid astrological sign must be provided.")
        return astrological_sign_id
    
    @validates('birthday')
    def validate_birthday(self, key, birthday):
        try:
            date_format = "%Y-%m-%d"
            datetime.strptime(birthday, date_format)
            dob = datetime.strptime(birthday, date_format)
            today = datetime.today()
            age = today.year - dob.year - ((today.month, today.day) < (dob.month, dob.day))
            if not 18 <= age <= 99:
                raise ValueError("Age must be between 18 and 99.")
            return birthday
        except ValueError:
            raise ValueError("Invalid date format. Please use 'YYYY-MM-DD'.")

class AstrologicalSign(db.Model):
    __tablename__ = 'astrological_signs'
    id = Column(Integer, primary_key=True)
    sign_name = Column(String(20), nullable=False)
    sign_description = Column(String(200), nullable=True)
    users = relationship("User", backref="astrological_sign")
    best_matches = relationship("BestMatch", back_populates="astrological_sign")
    serialize_rules = ('-best_matches.astrological_sign',)

    def to_dict(self):
        return {
            'id': self.id,
            'sign_name': self.sign_name,
            'sign_description': self.sign_description
        }

class BestMatch(db.Model):
    __tablename__ = 'best_matches'
    id = Column(Integer, primary_key=True)
    astrological_sign_id = Column(Integer, ForeignKey('astrological_signs.id'))
    best_match_name = Column(String(20), nullable=False)
    astrological_sign = relationship("AstrologicalSign", back_populates="best_matches")
    serialize_rules = ('-favorites.best_match',)

    def to_dict(self):
        return {
            'id': self.id,
            'astrological_sign_id': self.astrological_sign_id,
            'best_match_name': self.best_match_name,
        }
