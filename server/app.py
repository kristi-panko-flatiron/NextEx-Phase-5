#!/usr/bin/env python3

# Standard library imports

# Remote library imports
from flask import request, make_response, session
from flask_restful import Resource

# Local imports
from config import app, db, api
# Add your model imports
from models import User, UserMatch, AstrologicalSign, BestMatch, Match

api = App.

# Views go here!

@app.route('/')
def index():
    return '<h1>NextEx</h1>'
class UserList(Resource):
    def get(self):
        return_list = [u.to_dict() for u in User.query.all()]
        return make_response(return_list, 200)

    def post(self):
        data = request.get_json()
        try:
            user_hold = User(name=data["name"], username=data["username"], password=data["password"])
            db.session.add(user_hold)
            db.session.commit()
            session["user_id"] = user_hold.id
            return make_response(user_hold.to_dict(), 201)
        except:
            return make_response("Failed to create user", 400)

    def patch(self, id):
        user_hold = User.query.filter_by(id=id).one_or_none()
        if not user_hold:
            return make_response("User not found", 404)
        try:
            data = request.get_json()
            for attr in data:
                setattr(user_hold,attr,data[attr])
            db.session.add(user_hold)
            db.session.commit()
            return make_response(user_hold.to_dict(),202)
        except:
            return make_response("Failed to update user",400)

    def delete(self, id):
        user_hold = User.query.filter_by(id=id).one_or_none()
        if not user_hold:
            return make_response("User not found", 404)
        db.session.delete(user_hold)
        db.session.commit()
        return make_response("Successful delete", 204)

api.add_resource(UserList, "/users")

class UserByID(Resource):
    def get(self, id):
        user_hold = User.query.filter_by(id=id).one_or_none()
        if not user_hold:
            return make_response("User not found", 404)
        return make_response(user_hold.to_dict(), 200)

    def patch(self, id):
        user_hold = User.query.filter_by(id=id).one_or_none()
        if not user_hold:
            return make_response("User not found", 404)
        try:
            data = request.get_json()
            for attr in data:
                setattr(user_hold,attr,data[attr])
            db.session.add(user_hold)
            db.session.commit()
            return make_response(user_hold.to_dict(),202)
        except:
            return make_response("Failed to update user",400)

    def delete(self, id):
        user_hold = User.query.filter_by(id=id).one_or_none()
        if not user_hold:
            return make_response("User not found", 404)
        db.session.delete(user_hold)
        db.session.commit()
        return make_response("Successful delete", 204)

api.add_resource(UserByID, "/users/<int:id>")

class AstrologicalSignList(Resource):
    def get(self):
        return_list = [a.to_dict() for a in AstrologicalSign.query.all()]
        return make_response(return_list, 200)

    def post(self):
        data = request.get_json()
        try:
            astrological_sign_hold = AstrologicalSign(sign_name=data["sign_name"], sign_description=data["sign_description"])
            db.session.add(astrological_sign_hold)
            db.session.commit()
            return make_response(astrological_sign_hold.to_dict(), 201)
        except:
            return make_response("Failed to create astrological sign", 400)

    def patch(self, id):
        astrological_sign_hold = AstrologicalSign.query.filter_by(id=id).one_or_none()
        if not astrological_sign_hold:
            return make_response("Astrological sign not found", 404)
        try:
            data = request.get_json()
            for attr in data:
                setattr(astrological_sign_hold, attr, data[attr])
            db.session.add(astrological_sign_hold)
            db.session.commit()
            return make_response(astrological_sign_hold.to_dict(), 202)
        except:
            return make_response("Failed to update astrological sign", 400)

    def delete(self, id):
        astrological_sign_hold = AstrologicalSign.query.filter_by(id=id).one_or_none()
        if not astrological_sign_hold:
            return make_response("Astrological sign not found", 404)
        db.session.delete(astrological_sign_hold)
        db.session.commit()
        return make_response("Successful delete", 204)

api.add_resource(AstrologicalSignList, "/astrological_signs")

class AstrologicalSignByID(Resource):
    def get(self, id):
        astrological_sign_hold = AstrologicalSign.query.filter_by(id=id).one_or_none()
        if not astrological_sign_hold:
            return make_response("Astrological sign not found", 404)
        return make_response(astrological_sign_hold.to_dict(), 200)

    def patch(self, id):
        astrological_sign_hold = AstrologicalSign.query.filter_by(id=id).one_or_none()
        if not astrological_sign_hold:
            return make_response("Astrological sign not found", 404)
        try:
            data = request.get_json()
            for attr in data:
                setattr(astrological_sign_hold, attr, data[attr])
            db.session.add(astrological_sign_hold)
            db.session.commit()
            return make_response(astrological_sign_hold.to_dict(), 202)
        except:
            return make_response("Failed to update astrological sign", 400)

    def delete(self, id):
        astrological_sign_hold = AstrologicalSign.query.filter_by(id=id).one_or_none()
        if not astrological_sign_hold:
            return make_response("Astrological sign not found", 404)
        db.session.delete(astrological_sign_hold)
        db.session.commit()
        return make_response("Successful delete", 204)

api.add_resource(AstrologicalSignByID, "/astrological_signs/<int:id>")

class MatchList(Resource):
    def get(self):
        return_list = [m.to_dict() for m in Match.query.all()]
        return make_response(return_list, 200)

    def post(self):
        data = request.get_json()
        try:
            match_hold = Match(match_date=data["match_date"])
            db.session.add(match_hold)
            db.session.commit()
            return make_response(match_hold.to_dict(), 201)
        except:
            return make_response("Failed to create match", 400)

    def patch(self, id):
        match_hold = Match.query.filter_by(id=id).one_or_none()
        if not match_hold:
            return make_response("Match not found", 404)
        try:
            data = request.get_json()
            for attr in data:
                setattr(match_hold, attr, data[attr])
            db.session.add(match_hold)
            db.session.commit()
            return make_response(match_hold.to_dict(), 202)
        except:
            return make_response("Failed to update match", 400)

    def delete(self, id):
        match_hold = Match.query.filter_by(id=id).one_or_none()
        if not match_hold:
            return make_response("Match not found", 404)
        db.session.delete(match_hold)
        db.session.commit()
        return make_response("Successful delete", 204)

api.add_resource(MatchList, "/matches")

class MatchByID(Resource):
    def get(self, id):
        match_hold = Match.query.filter_by(id=id).one_or_none()
        if not match_hold:
            return make_response("Match not found", 404)
        return make_response(match_hold.to_dict(), 200)

    def patch(self, id):
        match_hold = Match.query.filter_by(id=id).one_or_none()
        if not match_hold:
            return make_response("Match not found", 404)
        try:
            data = request.get_json()
            for attr in data:
                setattr(match_hold, attr, data[attr])
            db.session.add(match_hold)
            db.session.commit()
            return make_response(match_hold.to_dict(), 202)
        except:
            return make_response("Failed to update match", 400)

    def delete(self, id):
        match_hold = Match.query.filter_by(id=id).one_or_none()
        if not match_hold:
            return make_response("Match not found", 404)
        db.session.delete(match_hold)
        db.session.commit()
        return make_response("Successful delete", 204)

api.add_resource(MatchByID, "/matches/<int:id>")

class BestMatchList(Resource):
    def get(self):
        return_list = [bm.to_dict() for bm in BestMatch.query.all()]
        return make_response(return_list, 200)

    def post(self):
        data = request.get_json()
        try:
            best_match_hold = BestMatch(
                astrological_sign_id=data["astrological_sign_id"],
                best_match_name=data["best_match_name"]
            )
            db.session.add(best_match_hold)
            db.session.commit()
            return make_response(best_match_hold.to_dict(), 201)
        except:
            return make_response("Failed to create best match", 400)

    def patch(self, id):
        best_match_hold = BestMatch.query.filter_by(id=id).one_or_none()
        if not best_match_hold:
            return make_response("Best match not found", 404)
        try:
            data = request.get_json()
            for attr in data:
                setattr(best_match_hold, attr, data[attr])
            db.session.add(best_match_hold)
            db.session.commit()
            return make_response(best_match_hold.to_dict(), 202)
        except:
            return make_response("Failed to update best match", 400)

    def delete(self, id):
        best_match_hold = BestMatch.query.filter_by(id=id).one_or_none()
        if not best_match_hold:
            return make_response("Best match not found", 404)
        db.session.delete(best_match_hold)
        db.session.commit()
        return make_response("Successful delete", 204)

api.add_resource(BestMatchList, "/best_matches")

class BestMatchByID(Resource):
    def get(self, id):
        best_match_hold = BestMatch.query.filter_by(id=id).one_or_none()
        if not best_match_hold:
            return make_response("Best match not found", 404)
        return make_response(best_match_hold.to_dict(), 200)

    def patch(self, id):
        best_match_hold = BestMatch.query.filter_by(id=id).one_or_none()
        if not best_match_hold:
            return make_response("Best match not found", 404)
        try:
            data = request.get_json()
            for attr in data:
                setattr(best_match_hold, attr, data[attr])
            db.session.add(best_match_hold)
            db.session.commit()
            return make_response(best_match_hold.to_dict(), 202)
        except:
            return make_response("Failed to update best match", 400)

    def delete(self, id):
        best_match_hold = BestMatch.query.filter_by(id=id).one_or_none()
        if not best_match_hold:
            return make_response("Best match not found", 404)
        db.session.delete(best_match_hold)
        db.session.commit()
        return make_response("Successful delete", 204)

api.add_resource(BestMatchByID, "/best_matches/<int:id>")


if __name__ == '__main__':
    app.run(port=5555, debug=True)

