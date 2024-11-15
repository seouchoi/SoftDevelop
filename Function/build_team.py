#호환되게 바꿔야함.(전체 수정)
#팀만드는 시나리오 : 팀 빌딩하는 사람의 정보와 팀 이름 적고 결정 
#competition_db_handler = Contest_DBHandler 

from flask import Blueprint, request, Response, session, redirect, url_for
from DBHandler.team_DBHandler import Team_DBHandler #만들어야함
from DBHandler.Contest_DBhandler import Contest_DBHandler #만들어야함
from DBHandler.member_DBHandler import member_DBHandler

team_db_handler = team_DBHandler()
member_db_handler = member_DBHandler()
Contest_db_handler = Contest_DBHandler()

build_team_bp = Blueprint('bulid_team', __name__)

@build_team_bp.route('/bulid_team', methods = ["POST"])
def build_team():
    key_id = session.get('key_id')  # 세션에서 key_id 가져오기
    if not key_id:
        return redirect(url_for('login.login'))
    team_data = request.get_json()
    #팀 키, 팀이름, 주장(팀빌딩한 사람의 키), 공모전, 팀 인원(멤버 키), 인원 수 
    #입력받는 데이터 : 팀이름
    team_key_id = team_db_handler.teams_collection.count_documents({}) + 1
    user_data = member_db_handler.get_member_data(key_id)
    competition_data = com_db_handler. #알맞는 코드     #competition key_id 넣기 


    new_team_data = {
        "team_key_id" : team_key_id,
        "team_name" : team_data["team_name"],
        "captain" : user_data["key_id"],
        "competition" : competition_data['com_key_id'],
        "member_id" : user_data["key_id"],
        "member_number" : 1
    }

    #아래는 데이터베이스로 가져다 주는 코드
    
    