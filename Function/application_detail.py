from flask import Blueprint, render_template
from DBHandler.member_DBHandler import member_DBHandler
from DBHandler.contest_DBhandler import Contest_DBHandler
from DBHandler.invite_DBHandler import invite_DBHandler

application_detail_bp = Blueprint('application_detail', __name__)
member_db_handler = member_DBHandler()
contest_db_handler = Contest_DBHandler()
invite_db_handler = invite_DBHandler()

@application_detail_bp.route("/application_detail/<int:invite_id>", methods = ["POST", "GET"])
def show_detail(invite_id):
    invite_data = invite_db_handler.get_invite_data(invite_id)
    contest_id = invite_data[0]['contest_id']
    sender_id = invite_data[0]['sender_id']
    team_id = invite_data[0]['team_id']
    
    contest_data = contest_db_handler.get_contest_by_id(contest_id)
    sender_data = member_db_handler.get_member_data_for_key(sender_id)
    invite_db_handler.mark_invite_as_read(invite_id)
    
    return render_template('application_detail_page.html', contest_data = contest_data, member_data = sender_data
                           ,team_id = team_id), 200