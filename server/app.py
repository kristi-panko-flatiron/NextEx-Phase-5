#!/usr/bin/env python3

from flask import request, make_response, session, jsonify
from flask_restful import Resource, Api
from datetime import datetime, date
import requests

from config import app, db
from models import *

from flask import Flask, request, jsonify
app = Flask(__name__)

api = Api(app)

class UserRegistration(Resource):
    def post(self):
        data = request.get_json()
        if not data:
            return make_response("No input data provided", 400)

        name = data.get('name')
        username = data.get('username')
        password = data.get('password')
        birthday = data.get('birthday')
        astrological_sign_id = data.get('astrological_sign_id')
        if not all([name, username, password, birthday, astrological_sign_id]):
            return make_response("Missing required fields", 400)

        new_user = User(name=name, username=username, password=password, birthday=birthday, astrological_sign_id=astrological_sign_id)

        try:
            db.session.add(new_user)
            db.session.commit()
            return make_response(new_user.to_dict(), 201)
        except Exception as e:
            db.session.rollback()
            return make_response(f"Failed to register user: {str(e)}", 500)


class UserLogin(Resource):
    def post(self):
        # Add your user login logic here
        pass

class UserProfile(Resource):
    def get(self):
        # Add your get user profile logic here
        pass

    def post(self):
        # Add your create user profile logic here
        pass

class UserManagement(Resource):
    def get(self, user_id):
        # Add your get user by ID logic here
        pass

    def patch(self, user_id):
        # Add your update user profile logic here
        pass

    def delete(self, user_id):
        # Add your delete user logic here
        pass

class AstrologicalSignAssignment(Resource):
    def post(self):
        # Add your astrological sign assignment logic here
        pass

class UsersBySign(Resource):
    def get(self, sign_id):
        # Add your logic to get users by sign ID here
        pass

class Favorites(Resource):
    def get(self):
        # Add your logic to get favorites here
        pass

    def post(self):
        # Add your logic to add favorites here
        pass

if __name__ == '__main__':
    api.add_resource(UserRegistration, '/register')
    api.add_resource(UserLogin, '/login')
    api.add_resource(UserProfile, '/profile')
    api.add_resource(UserManagement, '/profile/<int:user_id>')
    api.add_resource(AstrologicalSignAssignment, '/assign_astrological_sign')
    api.add_resource(UsersBySign, '/users_by_sign/<int:sign_id>')
    api.add_resource(Favorites, '/favorites')
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

