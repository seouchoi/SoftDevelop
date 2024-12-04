from flask import Blueprint, request, jsonify
from DBHandler.invite_DBHandler import invite_DBHandler

member_application_bp = Blueprint('member_application', __name__)

invite_db_handler = invite_DBHandler()

@member_application_bp.route("/api/application", methods = ["POST", "GET"])
def member_application():
    application_data = request.get_json()
    print(application_data)
    user_id = int(application_data['user_id'])
    team_id = int(application_data['team_id'])
    message = application_data['message']
    
    invite_db_handler.send_team_application(user_id, team_id, message)
    
    return jsonify({"message": "가입 신청 완료"}), 200
    