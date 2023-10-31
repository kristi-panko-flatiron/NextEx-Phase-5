from sqlalchemy import Column, Integer, String, Date, ForeignKey
from sqlalchemy.orm import relationship, validates
from datetime import datetime
from app import db

class User(db.Model):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False)
    birthday = Column(String(50), nullable=False)
    username = Column(String(50), nullable=False)
    password = Column(String(50), nullable=False)
    astrological_sign_id = Column(Integer, ForeignKey('astrological_signs.id'))
    astrological_sign = relationship("AstrologicalSign", back_populates="users")
    matches = relationship("UserMatch", back_populates="user")
    favorites = relationship("Favorites", back_populates="user")
    serialize_rules = ('-user_matches.user',)


    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'birthday': self.birthday,
            'username': self.username,
            'password': self.password,
            'astrological_sign_id': self.astrological_sign_id
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

    @validates('password')
    def validate_password(self, key, password):
        if not password:
            raise ValueError("Password must be provided.")
        return password

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
    users = relationship("User", back_populates="astrological_sign")
    best_matches = relationship("BestMatch", back_populates="astrological_sign")
    serialize_rules = ('-users.astrological_sign', '-best_matches.astrological_sign',)

class UserMatch(db.Model):
    __tablename__ = 'user_matches'
    user_id = Column(Integer, ForeignKey('users.id'), primary_key=True)
    match_id = Column(Integer, ForeignKey('matches.id'), primary_key=True)
    user = relationship("User", back_populates="matches")
    match = relationship("Match", back_populates="users")
    serialize_rules = ('-user.matches', '-match.users',)

class Match(db.Model):
    __tablename__ = 'matches'
    id = Column(Integer, primary_key=True)
    match_date = Column(Date, nullable=True)
    users = relationship("UserMatch", back_populates="match")
    serialize_rules = ('-users.match',)

class BestMatch(db.Model):
    __tablename__ = 'best_matches'
    id = Column(Integer, primary_key=True)
    astrological_sign_id = Column(Integer, ForeignKey('astrological_signs.id'))
    best_match_name = Column(String(20), nullable=False)
    astrological_sign = relationship("AstrologicalSign", back_populates="best_matches")
    favorites = relationship("Favorites", back_populates="best_match")
    serialize_rules = ('-astrological_sign.best_matches', '-favorites.best_match',)

class Favorites(db.Model):
    __tablename__ = 'favorites'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'))
    best_match_id = Column(Integer, ForeignKey('best_matches.id'))
    user = relationship("User", back_populates="favorites")
    best_match = relationship("BestMatch", back_populates="favorites")

    def to_dict(self):
        return {
            'id': self.id,
            'user_id': self.user_id,
            'best_match_id': self.best_match_id
        }

    serialize_rules = ('-user.favorites', '-best_match.favorites',)