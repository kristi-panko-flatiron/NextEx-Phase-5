from sqlalchemy_serializer import SerializerMixin
from sqlalchemy.orm import relationship
from sqlalchemy.orm import validates
from datetime import datetime
from config import db

# User model
class User(db.Model, SerializerMixin):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    birthday = db.Column(db.String(50), nullable=False)
    astrological_sign_id = db.Column(db.Integer, db.ForeignKey('astrological_signs.id'))
    astrological_sign = relationship('AstrologicalSign', back_populates='users')
    matches = db.relationship('Match', secondary='user_matches', back_populates='users')
    serialize_rules = ('-user_matches.user',)
    
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

# UserMatch model (intermediary table)
class UserMatch(db.Model):
    __tablename__ = 'user_matches'
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), primary_key=True)
    match_id = db.Column(db.Integer, db.ForeignKey('matches.id'), primary_key=True)
    user = relationship('User', back_populates='matches')
    match = relationship('Match', back_populates='users')

# Match model
class Match(db.Model, SerializerMixin):
    __tablename__ = 'matches'
    id = db.Column(db.Integer, primary_key=True)
    match_date = db.Column(db.Date)
    users = db.relationship('User', secondary='user_matches', back_populates='matches')
    serialize_rules = ('-user_matches.user', '-match.user_matches',)

# AstrologicalSign model
class AstrologicalSign(db.Model, SerializerMixin):
    __tablename__ = 'astrological_signs'
    id = db.Column(db.Integer, primary_key=True)
    sign_name = db.Column(db.String(20), nullable=False)
    sign_description = db.Column(db.String(200))
    best_matches = db.relationship('BestMatch', back_populates='astrological_sign')

# BestMatch model
class BestMatch(db.Model):
    __tablename__ = 'best_matches'
    id = db.Column(db.Integer, primary_key=True)
    astrological_sign_id = db.Column(db.Integer, db.ForeignKey('astrological_signs.id'))
    best_match_name = db.Column(db.String(20), nullable=False)
    astrological_sign = relationship('AstrologicalSign', back_populates='best_matches')
