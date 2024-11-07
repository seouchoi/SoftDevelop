#호환되게 바꿔야함.(전체 수정)

from flask import Blueprint, request, Response, session, redirect, url_for
from team_db_handler import team_DBHandler #만들어야함
from competition_db_handler import com_DBHandler #만들어야함
from member_db_handler import member_DBHandler

team_db_handler = team_DBHandler()
member_db_handler = member_DBHandler()
com_db_handler = com_DBHandler()

build_team_bp = Blueprint('bulid_team', __name__)

@build_team_bp.route('/bulid_team', methods = ["POST"])
def build_team():
    key_id = session.get('key_id')  # 세션에서 key_id 가져오기
    if not key_id:
        flash("로그인 후 이용 가능합니다")
        return redirect(url_for('login.login'))
    team_data = request.get_json()
    #팀 키, 팀이름, 주장(팀빌딩한 사람의 키), 공모전, 팀 인원(멤버 키), 인원 수 
    #입력받는 데이터 : 팀이름
    team_key_id = team_db_handler.teams_collection.count_documents({}) + 1
    user_data = member_db_handler.get_member_data(key_id)
    competition_data = com_db_handler. #알맞는 코드


    new_team_data = {
        "team_key_id" : team_key_id,
        "team_name" : team_data["team_name"],
        "captain" : user_data["key_id"],
        "competition" : competition_data['com_key_id'],
        "member_id" : user_data["key_id"],
        "member_number" : 1
    }

    #아래는 데이터베이스로 가져다 주는 코드
    
