#!/usr/bin/env python3

# Standard library imports
from random import randint, choice as rc

# Remote library imports
from faker import Faker

# Local imports
from app import app
from models import db
from app import db, User, AstrologicalSign, Match, BestMatch
# Create users
users_data = [
    {'name': 'Kris', 'birthday': '1990-05-15', 'username': 'kris123', 'password': 'password123', 'astrological_sign_id': 1},
    {'name': 'Idalis', 'birthday': '1990-05-15', 'username': 'idalis456', 'password': 'password456', 'astrological_sign_id': 3},
    {'name': 'Tano', 'birthday': '1990-05-15', 'username': 'tano789', 'password': 'password789', 'astrological_sign_id': 2},
    {'name': 'Matthew', 'birthday': '1990-05-15', 'username': 'matthew987', 'password': 'password987', 'astrological_sign_id': 4},
    # Add more users...
]

for user_data in users_data:
    user = User(**user_data)
    db.session.add(user)

# Create astrological signs
signs_data = [
    {'sign_name': 'Aries', 'sign_description': 'Direct, passionate, and headstrong.'},
    {'sign_name': 'Taurus', 'sign_description': 'Practical, pragmatic, steadfast, dedicated, dependable, and stubborn.'},
    {'sign_name': 'Gemini', 'sign_description': 'Chatty, amicable, and easy to get along with! A zesty personality, they may be somewhat of an entertainer but also flaky and indecisive. '},
    {'sign_name': 'Cancer', 'sign_description': 'Loyal, protective, and intuitive but may become too much creatures of comfort stuck in their routines.'},
    {'sign_name': 'Leo', 'sign_description': 'Confident, extravagant (in gestures and money), loyal, and ambitious.'},
    {'sign_name': 'Virgo', 'sign_description': 'Practical, grounded, detail-oriented, meticulous, as well as flexible and open to change'},
    {'sign_name': 'Libra', 'sign_description': 'A strong sense of fairness and justice, and are are eager mediators. They are idealistic and imaginative, but may be indecisive and self-pitying.'},
    {'sign_name': 'Scorpio', 'sign_description': 'A keen sense of perception but may keep themselves hidden, prone to secrecy. They are determined, ambitious, and obsessive.'},
    {'sign_name': 'Sagittarius', 'sign_description': 'Spiritual, intellectual, and sarcastic. Spontaneous lovers of freedom who love to converse with a wide array of people.'},
    {'sign_name': 'Capricorn', 'sign_description': 'Resilient, persistent, realistic, and disciplined. They may place an importance on career, social status or money, and have a strong work ethic. They are capable leaders and loyal team players but may be prone to stubbornness.'},
    {'sign_name': 'Aquarius', 'sign_description': 'Progressive, independent, and idealistic. They’re comfortable on the fringes of society and have a unique vision of the world.'},
    {'sign_name': 'Pisces', 'sign_description': 'Highly creative, as well as being friendly, sensitive, kind, and caring.'}
]

for sign_data in signs_data:
    sign = AstrologicalSign(**sign_data)
    db.session.add(sign)

# Create matches
matches_data = [
    {'match_date': '2023-10-24'},
    {'match_date': '2023-10-22'},
    # Add more matches...
]

for match_data in matches_data:
    match = Match(**match_data)
    db.session.add(match)

# Create best matches
best_matches_data = [
    {'astrological_sign_id': 1, 'best_match_name': 'Leo'},
    {'astrological_sign_id': 1, 'best_match_name': 'Sagittarius'},
    {'astrological_sign_id': 2, 'best_match_name': 'Virgo'},
    {'astrological_sign_id': 2, 'best_match_name': 'Capricorn'},
    {'astrological_sign_id': 3, 'best_match_name': 'Libra'},
    {'astrological_sign_id': 3, 'best_match_name': 'Aquarius'},
    {'astrological_sign_id': 4, 'best_match_name': 'Scorpio'},
    {'astrological_sign_id': 4, 'best_match_name': 'Pisces'},
    {'astrological_sign_id': 5, 'best_match_name': 'Aries'},
    {'astrological_sign_id': 5, 'best_match_name': 'Sagittarius'},
    {'astrological_sign_id': 6, 'best_match_name': 'Taurus'},
    {'astrological_sign_id': 6, 'best_match_name': 'Capricorn'},
    {'astrological_sign_id': 7, 'best_match_name': 'Gemini'},
    {'astrological_sign_id': 7, 'best_match_name': 'Aquarius'},
    {'astrological_sign_id': 8, 'best_match_name': 'Cancer'},
    {'astrological_sign_id': 8, 'best_match_name': 'Pisces'},
    {'astrological_sign_id': 9, 'best_match_name': 'Aries'},
    {'astrological_sign_id': 9, 'best_match_name': 'Leo'},
    {'astrological_sign_id': 10, 'best_match_name': 'Scorpio'},
    {'astrological_sign_id': 10, 'best_match_name': 'Pisces'},
    {'astrological_sign_id': 11, 'best_match_name': 'Gemini'},
    {'astrological_sign_id': 11, 'best_match_name': 'Libra'},
    {'astrological_sign_id': 12, 'best_match_name': 'Cancer'},
    {'astrological_sign_id': 12, 'best_match_name': 'Scorpio'}
    # Add more best matches...
]

for best_match_data in best_matches_data:
    best_match = BestMatch(**best_match_data)
    db.session.add(best_match)

# Commit the session to the database
db.session.commit()

print("Seed data added successfully.")



if __name__ == '__main__':
    fake = Faker()
    with app.app_context():
        print("Starting seed...")
        

