#선택된 공모전의 정보를 넘겨주는 코드
from flask import Blueprint, render_template, request, session
from DBHandler.contest_DBhandler import Contest_DBHandler
from DBHandler.team_DBHandler import Team_DBHandler
from DBHandler.member_DBHandler import member_DBHandler

contest_db_handler = Contest_DBHandler()
team_db_handler = Team_DBHandler()
member_db_handler = member_DBHandler()

contest_detail_bp = Blueprint('contest_detail', __name__)

@contest_detail_bp.route('/category/<contest_id>', methods = ["GET"]) #<contest_id>를 <contest_name>으로 사용할 수 있는 방법 생각해보기
def contest_detail(contest_id):
    key_id = session.get('key_id')
    member_data = member_db_handler.get_member_data_for_key(key_id)
    contest_id = int(contest_id)
    contest_data = contest_db_handler.get_contest_by_id(contest_id)
    team_list = team_db_handler.get_team_info_by_contest_id(contest_id)
    
    return render_template('contest_detail_page.html', contest_data = contest_data,
                           team_list = team_list, member_data = member_data)
