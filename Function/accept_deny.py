from flask import Blueprint, request, jsonify
from DBHandler.team_DBHandler import Team_DBHandler

#contest_detail_page accept에서 수락하면 add_team_member를시킴.

accept_deny_bp = Blueprint('accept_deny', __name__)
team_db_handler = Team_DBHandler()

@accept_deny_bp.route("/api/accept", methods = ["POST", "GET"])
def accept():  
    data = request.get_json()
    print(data)
    user_id = int(data['user_id'])
    team_id = int(data['team_id'])
    team_db_handler.add_team_member(team_id, user_id)
    return jsonify(data)
    
#거절할 경우에는 아무런 조치가 필요없음
@accept_deny_bp.route("/api/deny", methods = ["POST", "GET"])
def deny():
    return 0