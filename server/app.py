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

# @app.after_request
# def after_request(response):
#     response.headers.add('Access-Control-Allow-Origin', '*')
#     response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization')
#     response.headers.add('Access-Control-Allow-Methods', 'GET, PATCH, POST, DELETE, OPTIONS')
#     return response

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
            return make_response("Login successful", 200)
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
        user_birthday = datetime.strptime(birthday, '%Y-%m-%d').date()
        astrological_sign_id = calculate_astrological_sign(user_birthday)
        if not all([name, username, password, birthday, astrological_sign_id]):
            return make_response("Missing required fields", 400)
        new_user = User(name=name, username=username, password_hash=password, birthday=birthday, astrological_sign_id=astrological_sign_id)
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
        users = User.query.filter_by(astrological_sign_id=sign_id).all()
        if not users:
            return make_response("No users found for the specified sign ID", 404)
        user_list = [user.to_dict() for user in users]
        return make_response(user_list, 200)

class Favorites(Resource):
    def get(self):
        favorites = Favorite.query.all()
        if not favorites:
            return make_response("No favorites found", 404)
        favorite_list = [favorite.to_dict() for favorite in favorites]
        return make_response(favorite_list, 200)

    def post(self):
        data = request.json
        if not data:
            return make_response("No input data provided", 400)
        user_id = data.get("user_id")
        best_match_id = data.get("best_match_id")
        if not all([user_id, best_match_id]):
            return make_response("Missing required fields", 400)
        user = User.query.get(user_id)
        if not user:
            return make_response(f"User with ID {user_id} not found", 404)
        best_match = BestMatch.query.get(best_match_id)
        if not best_match:
            return make_response(f"Best match with ID {best_match_id} not found", 404)
        user.favorites.append(best_match)
        db.session.commit()
        return make_response("Favorite added successfully", 201)

    def delete(self):
        data = request.json
        if not data:
            return make_response("No input data provided", 400)
        user_id = data.get("user_id")
        best_match_id = data.get("best_match_id")
        if not all([user_id, best_match_id]):
            return make_response("Missing required fields", 400)
        user = User.query.get(user_id)
        if not user:
            return make_response(f"User with ID {user_id} not found", 404)
        best_match = BestMatch.query.get(best_match_id)
        if not best_match:
            return make_response(f"Best match with ID {best_match_id} not found", 404)
        if best_match in user.favorites:
            user.favorites.remove(best_match)
            db.session.commit()
            return make_response("Favorite removed successfully", 200)
        else:
            return make_response("The specified favorite does not exist for the user", 404)

class BestMatches(Resource):
    def get(self):
        astrological_signs = AstrologicalSign.query.all()
        all_users = User.query.all()  
        best_matches = {}
        for sign in astrological_signs:
            users_for_sign = [user for user in all_users if user.astrological_sign_id == sign.id]
            matches_data = db.session.query(BestMatch).filter_by(astrological_sign_id=sign.id).all()
            best_match_names = [match.best_match_name for match in matches_data]
            best_match_users = [{
                "name": user.name,
                "astrological_sign": map_astrological_sign_id_to_name(user.astrological_sign_id)
            } for user in users_for_sign if user.name in best_match_names]
            best_matches[map_astrological_sign_id_to_name(sign.id)] = best_match_users
        return make_response(best_matches, 200)


if __name__ == '__main__':
    api.add_resource(UserRegistration, '/register')
    api.add_resource(UserLogin, '/login')
    api.add_resource(UserProfile, '/profile')
    api.add_resource(UserManagement, '/profile/<int:user_id>')
    api.add_resource(AstrologicalSignAssignment, '/assign_astrological_sign')
    api.add_resource(UsersBySign, '/users_by_sign/<int:sign_id>')
    api.add_resource(Favorites, '/favorites')
    api.add_resource(BestMatches, '/bestmatches')
    app.run(port=5555, debug=True)

# # Remote library imports
# from flask import request, jsonify, make_response, session
# from flask_restful import Resource, Api
# from datetime import datetime, date

# # Local imports
# from config import app, db
# from models import *

# # from models import User

# # Instantiate API
# api = Api(app)

# # User endpoints
# class UserList(Resource):
#     def get(self):
#         from models import User
#         return_list = [u.to_dict() for u in User.query.all()]
#         return make_response(return_list, 200)

#     def post(self):
#         try:
#             data = request.get_json(force=True)
#             if not data:
#                 return make_response(jsonify({"message": "No input data provided"}), 400)

#             required_fields = ["name", "birthday", "username", "password", "astrological_sign_id"]
#             for field in required_fields:
#                 if field not in data:
#                     return make_response(jsonify({"message": f"Missing required field: {field}"}), 400)

#             user_hold = User(
#                 name=data["name"],
#                 birthday=data["birthday"],
#                 username=data["username"],
#                 password=data["password"],
#                 astrological_sign_id=data["astrological_sign_id"]
#             )
#             db.session.add(user_hold)
#             db.session.commit()
#             session["user_id"] = user_hold.id
#             return make_response(jsonify(user_hold.to_dict()), 201)

#         except ValueError as e:
#             return make_response(jsonify({"message": f"Value error: {str(e)}"}), 400)

#         except Exception as e:
#             return make_response(jsonify({"message": f"Failed to create user: {str(e)}"}), 400)


#     # def patch(self, user_id):
#     #     user_hold = User.query.filter_by(id=user_id).one_or_none()
#     #     if not user_hold:
#     #         return make_response("User not found", 404)
#     #     try:
#     #         data = request.get_json()
#     #         for attr in data:
#     #             setattr(user_hold, attr, data[attr])
#     #         db.session.add(user_hold)
#     #         db.session.commit()
#     #         return make_response(user_hold.to_dict(), 202)
#     #     except:
#     #         return make_response("Failed to update user", 400)


#     # def delete(self, user_id):
#     #     user_hold = User.query.filter_by(id=user_id).one_or_none()
#     #     if not user_hold:
#     #         return make_response("User not found", 404)
#     #     db.session.delete(user_hold)
#     #     db.session.commit()
#     #     return make_response("Successful delete", 204)

# class UserByID(Resource):
#     def get(self, id):
#         user_hold = User.query.filter_by(id=id).one_or_none()
#         if not user_hold:
#             return make_response("User not found", 404)
#         return make_response(user_hold.to_dict(), 200)

#     def patch(self, id):
#         user_hold = User.query.filter_by(id=id).one_or_none()
#         if not user_hold:
#             return make_response("User not found", 404)
#         try:
#             data = request.get_json()
#             for attr in data:
#                 setattr(user_hold, attr, data[attr])
#             db.session.add(user_hold)
#             db.session.commit()
#             return make_response(user_hold.to_dict(), 202)
#         except:
#             return make_response("Failed to update user", 400)

#     def delete(self, id):
#         user_hold = User.query.filter_by(id=id).one_or_none()
#         if not user_hold:
#             return make_response("User not found", 404)
#         db.session.delete(user_hold)
#         db.session.commit()
#         return make_response("Successful delete", 204)

# class AstrologicalSignList(Resource):
#     def get(self):
#         return_list = [a.to_dict() for a in AstrologicalSign.query.all()]
#         return make_response(return_list, 200)

#     def post(self):
#         data = request.get_json()
#         try:
#             astrological_sign_hold = AstrologicalSign(sign_name=data["sign_name"], sign_description=data["sign_description"])
#             db.session.add(astrological_sign_hold)
#             db.session.commit()
#             return make_response(astrological_sign_hold.to_dict(), 201)
#         except:
#             return make_response("Failed to create astrological sign", 400)

#     def patch(self, id):
#         astrological_sign_hold = AstrologicalSign.query.filter_by(id=id).one_or_none()
#         if not astrological_sign_hold:
#             return make_response("Astrological sign not found", 404)
#         try:
#             data = request.get_json()
#             for attr in data:
#                 setattr(astrological_sign_hold, attr, data[attr])
#             db.session.add(astrological_sign_hold)
#             db.session.commit()
#             return make_response(astrological_sign_hold.to_dict(), 202)
#         except:
#             return make_response("Failed to update astrological sign", 400)

#     def delete(self, id):
#         astrological_sign_hold = AstrologicalSign.query.filter_by(id=id).one_or_none()
#         if not astrological_sign_hold:
#             return make_response("Astrological sign not found", 404)
#         db.session.delete(astrological_sign_hold)
#         db.session.commit()
#         return make_response("Successful delete", 204)


# class AstrologicalSignByID(Resource):
#     def get(self, id):
#         astrological_sign_hold = AstrologicalSign.query.filter_by(id=id).one_or_none()
#         if not astrological_sign_hold:
#             return make_response("Astrological sign not found", 404)
#         return make_response(astrological_sign_hold.to_dict(), 200)

#     def patch(self, id):
#         astrological_sign_hold = AstrologicalSign.query.filter_by(id=id).one_or_none()
#         if not astrological_sign_hold:
#             return make_response("Astrological sign not found", 404)
#         try:
#             data = request.get_json()
#             for attr in data:
#                 setattr(astrological_sign_hold, attr, data[attr])
#             db.session.add(astrological_sign_hold)
#             db.session.commit()
#             return make_response(astrological_sign_hold.to_dict(), 202)
#         except:
#             return make_response("Failed to update astrological sign", 400)

#     def delete(self, id):
#         astrological_sign_hold = AstrologicalSign.query.filter_by(id=id).one_or_none()
#         if not astrological_sign_hold:
#             return make_response("Astrological sign not found", 404)
#         db.session.delete(astrological_sign_hold)
#         db.session.commit()
#         return make_response("Successful delete", 204)

# class MatchList(Resource):
#     def get(self):
#         return_list = [m.to_dict() for m in Match.query.all()]
#         return make_response(return_list, 200)

#     def post(self):
#         data = request.get_json()
#         try:
#             match_hold = Match(match_date=data["match_date"])
#             db.session.add(match_hold)
#             db.session.commit()
#             return make_response(match_hold.to_dict(), 201)
#         except:
#             return make_response("Failed to create match", 400)

#     def patch(self, id):
#         match_hold = Match.query.filter_by(id=id).one_or_none()
#         if not match_hold:
#             return make_response("Match not found", 404)
#         try:
#             data = request.get_json()
#             for attr in data:
#                 setattr(match_hold, attr, data[attr])
#             db.session.add(match_hold)
#             db.session.commit()
#             return make_response(match_hold.to_dict(), 202)
#         except:
#             return make_response("Failed to update match", 400)

#     def delete(self, id):
#         match_hold = Match.query.filter_by(id=id).one_or_none()
#         if not match_hold:
#             return make_response("Match not found", 404)
#         db.session.delete(match_hold)
#         db.session.commit()
#         return make_response("Successful delete", 204)

# class MatchByID(Resource):
#     def get(self, id):
#         match_hold = Match.query.filter_by(id=id).one_or_none()
#         if not match_hold:
#             return make_response("Match not found", 404)
#         return make_response(match_hold.to_dict(), 200)

#     def patch(self, id):
#         match_hold = Match.query.filter_by(id=id).one_or_none()
#         if not match_hold:
#             return make_response("Match not found", 404)
#         try:
#             data = request.get_json()
#             for attr in data:
#                 setattr(match_hold, attr, data[attr])
#             db.session.add(match_hold)
#             db.session.commit()
#             return make_response(match_hold.to_dict(), 202)
#         except:
#             return make_response("Failed to update match", 400)

#     def delete(self, id):
#         match_hold = Match.query.filter_by(id=id).one_or_none()
#         if not match_hold:
#             return make_response("Match not found", 404)
#         db.session.delete(match_hold)
#         db.session.commit()
#         return make_response("Successful delete", 204)

# class BestMatchList(Resource):
#     def get(self):
#         return_list = [bm.to_dict() for bm in BestMatch.query.all()]
#         return make_response(return_list, 200)

#     def post(self):
#         data = request.get_json()
#         try:
#             best_match_hold = BestMatch(
#                 astrological_sign_id=data["astrological_sign_id"],
#                 best_match_name=data["best_match_name"]
#             )
#             db.session.add(best_match_hold)
#             db.session.commit()
#             return make_response(best_match_hold.to_dict(), 201)
#         except:
#             return make_response("Failed to create best match", 400)

#     def patch(self, id):
#         best_match_hold = BestMatch.query.filter_by(id=id).one_or_none()
#         if not best_match_hold:
#             return make_response("Best match not found", 404)
#         try:
#             data = request.get_json()
#             for attr in data:
#                 setattr(best_match_hold, attr, data[attr])
#             db.session.add(best_match_hold)
#             db.session.commit()
#             return make_response(best_match_hold.to_dict(), 202)
#         except:
#             return make_response("Failed to update best match", 400)

#     def delete(self, id):
#         best_match_hold = BestMatch.query.filter_by(id=id).one_or_none()
#         if not best_match_hold:
#             return make_response("Best match not found", 404)
#         db.session.delete(best_match_hold)
#         db.session.commit()
#         return make_response("Successful delete", 204)


# class BestMatchByID(Resource):
#     def get(self, id):
#         best_match_hold = BestMatch.query.filter_by(id=id).one_or_none()
#         if not best_match_hold:
#             return make_response("Best match not found", 404)
#         return make_response(best_match_hold.to_dict(), 200)

#     def patch(self, id):
#         best_match_hold = BestMatch.query.filter_by(id=id).one_or_none()
#         if not best_match_hold:
#             return make_response("Best match not found", 404)
#         try:
#             data = request.get_json()
#             for attr in data:
#                 setattr(best_match_hold, attr, data[attr])
#             db.session.add(best_match_hold)
#             db.session.commit()
#             return make_response(best_match_hold.to_dict(), 202)
#         except:
#             return make_response("Failed to update best match", 400)

#     def delete(self, id):
#         best_match_hold = BestMatch.query.filter_by(id=id).one_or_none()
#         if not best_match_hold:
#             return make_response("Best match not found", 404)
#         db.session.delete(best_match_hold)
#         db.session.commit()
#         return make_response("Successful delete", 204)
#     # Consolidated add_resource calls
    # api.add_resource(UserList, "/users")
    # api.add_resource(UserByID, "/users/<int:id>")
    # api.add_resource(AstrologicalSignList, "/astrological_signs")
    # api.add_resource(AstrologicalSignByID, "/astrological_signs/<int:id>")
    # api.add_resource(MatchList, "/matches")
    # api.add_resource(MatchByID, "/matches/<int:id>")
    # api.add_resource(BestMatchList, "/best_matches")
    # api.add_resource(BestMatchByID, "/best_matches/<int:id>")

# if __name__ == '__main__':

#     app.run(port=5555, debug=True)

