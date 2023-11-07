#!/usr/bin/env python3

# Standard library imports
from random import randint, choice as rc

# Remote library imports
from faker import Faker

# Local imports
from app import app
from models import db
from app import db, User, AstrologicalSign, BestMatch, favorite
from datetime import datetime
from datetime import date


if __name__ == '__main__':
    fake = Faker()
    with app.app_context():
        print("Starting seed...")
        User.query.delete()

        # Create users
        users_data = []
        for _ in range(40):
            user_birthday = fake.date_of_birth(minimum_age=18, maximum_age=99)
            user_sign_id = None
            if (user_birthday.month == 3 and user_birthday.day >= 21) or (user_birthday.month == 4 and user_birthday.day <= 19):
                user_sign_id = 1  # Aries
            elif (user_birthday.month == 4 and user_birthday.day >= 20) or (user_birthday.month == 5 and user_birthday.day <= 20):
                user_sign_id = 2  # Taurus
            elif (user_birthday.month == 5 and user_birthday.day >= 21) or (user_birthday.month == 6 and user_birthday.day <= 20):
                user_sign_id = 3  # Gemini
            elif (user_birthday.month == 6 and user_birthday.day >= 21) or (user_birthday.month == 7 and user_birthday.day <= 22):
                user_sign_id = 4  # Cancer
            elif (user_birthday.month == 7 and user_birthday.day >= 23) or (user_birthday.month == 8 and user_birthday.day <= 22):
                user_sign_id = 5  # Leo
            elif (user_birthday.month == 8 and user_birthday.day >= 23) or (user_birthday.month == 9 and user_birthday.day <= 22):
                user_sign_id = 6  # Virgo
            elif (user_birthday.month == 9 and user_birthday.day >= 23) or (user_birthday.month == 10 and user_birthday.day <= 22):
                user_sign_id = 7  # Libra
            elif (user_birthday.month == 10 and user_birthday.day >= 23) or (user_birthday.month == 11 and user_birthday.day <= 21):
                user_sign_id = 8  # Scorpio
            elif (user_birthday.month == 11 and user_birthday.day >= 22) or (user_birthday.month == 12 and user_birthday.day <= 21):
                user_sign_id = 9  # Sagittarius
            elif (user_birthday.month == 12 and user_birthday.day >= 22) or (user_birthday.month == 1 and user_birthday.day <= 19):
                user_sign_id = 10  # Capricorn
            elif (user_birthday.month == 1 and user_birthday.day >= 20) or (user_birthday.month == 2 and user_birthday.day <= 18):
                user_sign_id = 11  # Aquarius
            elif (user_birthday.month == 2 and user_birthday.day >= 19) or (user_birthday.month == 3 and user_birthday.day <= 20):
                user_sign_id = 12  # Pisces

            user_data = User(
                name = fake.name(),
                username = fake.user_name(),
                password_hash = "1234",
                birthday = user_birthday.strftime('%Y-%m-%d'),
                image_url=fake.image_url(),
                astrological_sign_id = user_sign_id
            )
            users_data.append(user_data)

        db.session.add_all(users_data)

        db.session.commit()

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
        ]

        # Add best matches to the session
        for match_data in best_matches_data:
            match = BestMatch(**match_data)
            db.session.add(match)

        # Commit all best matches to the database
        db.session.commit()

        print("Seed data added successfully.")
