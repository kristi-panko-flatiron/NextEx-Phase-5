#!/usr/bin/env python3

from flask import request, make_response, session
from flask_restful import Resource, Api
from datetime import datetime
from werkzeug.security import check_password_hash, generate_password_hash
import requests

from config import app, db
from models import *

from flask import Flask, request, jsonify

api = Api(app)


def calculate_astrological_sign(birthdate):
    if (birthdate.month == 3 and birthdate.day >= 21) or (birthdate.month == 4 and birthdate.day <= 19):
        return 1  # Aries
    elif (birthdate.month == 4 and birthdate.day >= 20) or (birthdate.month == 5 and birthdate.day <= 20):
        return 2  # Taurus
    elif (birthdate.month == 5 and birthdate.day >= 21) or (birthdate.month == 6 and birthdate.day <= 20):
        return 3  # Gemini
    elif (birthdate.month == 6 and birthdate.day >= 21) or (birthdate.month == 7 and birthdate.day <= 22):
        return 4  # Cancer
    elif (birthdate.month == 7 and birthdate.day >= 23) or (birthdate.month == 8 and birthdate.day <= 22):
        return 5  # Leo
    elif (birthdate.month == 8 and birthdate.day >= 23) or (birthdate.month == 9 and birthdate.day <= 22):
        return 6  # Virgo
    elif (birthdate.month == 9 and birthdate.day >= 23) or (birthdate.month == 10 and birthdate.day <= 22):
        return 7  # Libra
    elif (birthdate.month == 10 and birthdate.day >= 23) or (birthdate.month == 11 and birthdate.day <= 21):
        return 8  # Scorpio
    elif (birthdate.month == 11 and birthdate.day >= 22) or (birthdate.month == 12 and birthdate.day <= 21):
        return 9  # Sagittarius
    elif (birthdate.month == 12 and birthdate.day >= 22) or (birthdate.month == 1 and birthdate.day <= 19):
        return 10  # Capricorn
    elif (birthdate.month == 1 and birthdate.day >= 20) or (birthdate.month == 2 and birthdate.day <= 18):
        return 11  # Aquarius
    elif (birthdate.month == 2 and birthdate.day >= 19) or (birthdate.month == 3 and birthdate.day <= 20):
        return 12  # Pisces
    else:
        raise ValueError("Invalid birthdate or astrological sign not determined.")

def map_astrological_sign_id_to_name(sign_id):
    sign_names = {
        1: 'Aries',
        2: 'Taurus',
        3: 'Gemini',
        4: 'Cancer',
        5: 'Leo',
        6: 'Virgo',
        7: 'Libra',
        8: 'Scorpio',
        9: 'Sagittarius',
        10: 'Capricorn',
        11: 'Aquarius',
        12: 'Pisces'
    }
    return sign_names.get(sign_id)

class UserLogin(Resource):
    def post(self):
        data = request.json
        if not data:
            return make_response("No input data provided", 400)
        username = data['username']
        password = data['password']
        user = User.query.filter_by(username=username).first()
        if user and user.authenticate(password):
            session['user_id'] = user.id
            return make_response(jsonify({"user_id": user.id}), 200)
        else:
            return make_response("Invalid credentials", 401)
        
        
class UserRegistration(Resource):
    def post(self):
        data = request.json
        if not data:
            return make_response("No input data provided", 400)
        name = data['name']
        username = data['username']
        password = data['password']
        birthday = data['birthday']
        
        #bd into string object
        user_birthday = datetime.strptime(birthday, '%Y-%m-%d').date()
        
        #Calculate sign
        astrological_sign_id = calculate_astrological_sign(user_birthday)
        
        # Hash password
        password_hash = bcrypt.generate_password_hash(password).decode('utf-8')
        
        new_user = User(
            name=name, 
            username=username, 
            password_hash=password_hash, 
            birthday=birthday, 
            astrological_sign_id=astrological_sign_id
        )
        
        try:
            db.session.add(new_user)
            db.session.commit()
            return make_response(new_user.to_dict(), 201)
        except Exception as e:
            db.session.rollback()
            return make_response(f"Failed to register user: {str(e)}", 500)


class UserProfile(Resource):
    def get(self, user_id):
        user = User.query.filter_by(id=user_id).first()
        if not user:
            return make_response(f"No user found with ID: {user_id}", 404)
        user_data = user.to_dict()
        user_data['astrological_sign'] = map_astrological_sign_id_to_name(user.astrological_sign_id)
        return make_response(user_data, 200)

class UserManagement(Resource):
    def get(self, user_id):
        user = User.query.get(user_id)
        if not user:
            return make_response(f"No user found with ID: {user_id}", 404)
        return make_response(user.to_dict(), 200)

    def patch(self, user_id):
        data = request.get_json()
        if not data:
            return make_response("No input data provided", 400)
        user = User.query.filter_by(id=user_id).first()
        if not user:
            return make_response(f"No user found with ID: {user_id}", 404)
        if 'name' in data:
            user.name = data['name']
        if 'username' in data:
            user.username = data['username']
        if 'password' in data:
            user.password = data['password']
        if 'birthday' in data:
            user.birthday = data['birthday']
        if 'astrological_sign_id' in data:
            user.astrological_sign_id = data['astrological_sign_id']
        try:
            db.session.commit()
            return make_response(user.to_dict(), 200)
        except Exception as e:
            db.session.rollback()
            return make_response(f"Failed to update user: {str(e)}", 500)

    def delete(self, user_id):
        user = User.query.filter_by(id=user_id).first()
        if not user:
            return make_response(f"No user found with ID: {user_id}", 404)
        try:
            db.session.delete(user)
            db.session.commit()
            return make_response(f"User with ID {user_id} has been deleted", 200)
        except Exception as e:
            db.session.rollback()
            return make_response(f"Failed to delete user: {str(e)}", 500)

class AstrologicalSignAssignment(Resource):
    def post(self):
        data = request.json
        if not data:
            return make_response("No input data provided", 400)
        name = data["name"]
        username = data["username"]
        password = data["password"]
        birthday = data["birthday"]
        try:
            user_birthday = datetime.strptime(birthday, "%Y-%m-%d")
            astrological_sign_id = calculate_astrological_sign(user_birthday)
        except ValueError as e:
            return make_response(str(e), 400)
        if not all([name, username, password, birthday, astrological_sign_id]):
            return make_response("Missing required fields", 400)
        new_user = User(
            name=name,
            username=username,
            password=password,
            birthday=birthday,
            astrological_sign_id=astrological_sign_id
        )
        try:
            db.session.add(new_user)
            db.session.commit()
            return make_response(new_user.to_dict(), 201)
        except Exception as e:
            db.session.rollback()
            return make_response(f"Failed to register user sign: {str(e)}", 500)

class UsersBySign(Resource):
    def get(self, sign_id):
        best_matches = BestMatch.query.filter_by(astrological_sign_id=sign_id).all()
        best_match_sign_ids = [match.id for match in best_matches]
        
        matched_users = []
        for match_sign_id in best_match_sign_ids:
            users = User.query.filter_by(astrological_sign_id=match_sign_id).all()
            matched_users.extend(users)
        return jsonify([user.to_dict() for user in matched_users])


class Favorites(Resource):
    def get(self):
        favorites = Favorite.query.all()
        if not favorites:
            return make_response("No favorites found", 404)
        favorite_list = [favorite.to_dict() for favorite in favorites]
        return make_response(favorite_list, 200)

    # def post(self):
    #     data = request.json
    #     new_favorite = Favorite(user_id=data['user_id'], best_match_id=data['best_match_id'])
    #     db.session.add(new_favorite)
    #     db.session.commit()
    #     return make_response("Favorite added successfully", 201)

    def post(self):
        data = request.json
        new_favorite = Favorite(user_id=data['user_id'], best_match_id=data['best_match_id'])
        db.session.add(new_favorite)
        db.session.commit()
        # Return the new favorite data as well
        return jsonify(new_favorite.to_dict()), 201


    def delete(self):
        data = request.json
        favorite = Favorite.query.filter_by(user_id=data['user_id'], best_match_id=data['best_match_id']).first()
        if not favorite:
            return make_response("Favorite not found", 404)
        
        db.session.delete(favorite)
        db.session.commit()
        return make_response("Favorite removed successfully", 200)
        


class AllUsers(Resource):
    def get(self):
        all_users = User.query.all()
        users_data = [user.to_dict() for user in all_users]
        for user_data in users_data:
            user_sign = AstrologicalSign.query.get(user_data['astrological_sign']['id'])
            best_matches = BestMatch.query.filter_by(astrological_sign_id=user_sign.id).limit(2).all()
            user_data['best_matches'] = [match.best_match_name for match in best_matches]
        return jsonify(users_data)
    
class UsersByBestMatch(Resource):
    def get(self, user_id):
        user = User.query.get(user_id)
        if not user:
            return make_response("User not found", 404)
        best_matches = BestMatch.query.filter_by(astrological_sign_id=user.astrological_sign_id).limit(2).all()
        best_match_sign_ids = [match.id for match in best_matches]
        matched_users = User.query.filter(User.astrological_sign_id.in_(best_match_sign_ids)).all()
        return jsonify([user.to_dict() for user in matched_users])

class BestMatches(Resource):
    def get(self, sign_id):
        matches_data = BestMatch.query.filter_by(astrological_sign_id=sign_id).limit(2).all()
        if not matches_data:
            return {'message': 'No matches found'}, 404
        return jsonify([match.astrological_sign.to_dict() for match in matches_data])
    
class BestMatchesForUser(Resource):
    def get(self, user_id):
        user = User.query.get(user_id)
        if not user:
            return {'message': 'User not found'}, 404

        # Get the best matches for the user's sign
        best_matches = BestMatch.query.filter_by(astrological_sign_id=user.astrological_sign_id).all()
        best_match_sign_names = [match.best_match_name for match in best_matches]
        
        # Get all users with a sign that's in the best matches
        matched_users = User.query.join(AstrologicalSign).filter(AstrologicalSign.sign_name.in_(best_match_sign_names)).all()
        return jsonify([matched_user.to_dict() for matched_user in matched_users])

    # class BestMatches(Resource):
#     def get(self):
#         astrological_signs = AstrologicalSign.query.all()
#         all_users = User.query.all()  
#         best_matches = {}
#         for sign in astrological_signs:
#             users_for_sign = [user for user in all_users if user.astrological_sign_id == sign.id]
#             matches_data = db.session.query(BestMatch).filter_by(astrological_sign_id=sign.id).all()
#             best_match_names = [match.best_match_name for match in matches_data]
#             best_match_users = [{
#                 "name": user.name,
#                 "astrological_sign": map_astrological_sign_id_to_name(user.astrological_sign_id)
#             } for user in users_for_sign if user.name in best_match_names]
#             best_matches[map_astrological_sign_id_to_name(sign.id)] = best_match_users
#         return make_response(best_matches, 200)

if __name__ == '__main__':
    api.add_resource(UserRegistration, '/register')
    api.add_resource(UserLogin, '/login')
    api.add_resource(UserProfile, '/profile')
    api.add_resource(UserManagement, '/profile/<int:user_id>')
    api.add_resource(AstrologicalSignAssignment, '/assign_astrological_sign')
    api.add_resource(UsersBySign, '/users_by_sign/<int:sign_id>')
    api.add_resource(Favorites, '/favorites')
    api.add_resource(BestMatches, '/bestmatches/<int:sign_id>')
    api.add_resource(UsersByBestMatch, '/users_by_best_match/<int:user_id>')
    api.add_resource(AllUsers, '/users')
    api.add_resource(BestMatchesForUser, '/best_matches_for_user/<int:user_id>')
    app.run(port=5555, debug=True)
