from flask import Blueprint, request
from DBHandler.team_DBHandler import Team_DBHandler

#contest_detail_page accept에서 수락하면 add_team_member를시킴.

accept_deny_bp = Blueprint('accept_deny', __name__)
team_db_handler = Team_DBHandler()

@accept_deny_bp.route("/api/accept", methods = ["POST", "GET"])
def accept():  
    data = request.get_json()
    user_id = data['key_id']
    team_db_handler.add_team_member(user_id)
    
@accept_deny_bp.route("/api/deny", methods = ["POST", "GET"])
def deny():
    