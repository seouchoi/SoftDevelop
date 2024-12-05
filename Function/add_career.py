from flask import Blueprint, request, jsonify
from DBHandler.award_DBHandler import Awards_DBHandler

add_career_bp = Blueprint("add_career", __name__)

award_db_handler = Awards_DBHandler()

@add_career_bp.route("/api/add_career", methods = ["POST", "GET"])
def add_career():
    award_data = request.get_json()
    user_id = int(award_data['user_id'])
    txt = award_data['award']
    rank = int(award_data['result'])
    award_db_handler.add_award(user_id, txt, rank)
    return jsonify({'message': "수상이력이 저장되었습니다."}), 200
    