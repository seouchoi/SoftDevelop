#호환되게 바꿔야함.(전체 수정)
#팀만드는 시나리오 : 팀 빌딩하는 사람의 정보와 팀 이름 적고 결정 
#competition_db_handler = Contest_DBHandler 
#이 페이지는 공모전 디테일까지 끝내고 난 뒤에 수정(상호작용 시켜야함.)
from flask import Blueprint, request, Response, session, redirect, url_for
from DBHandler.team_DBHandler import Team_DBHandler #만들어야함
from DBHandler.Contest_DBhandler import Contest_DBHandler #만들어야함
from DBHandler.member_DBHandler import member_DBHandler

team_db_handler = Team_DBHandler()
member_db_handler = member_DBHandler()
Contest_db_handler = Contest_DBHandler()

build_team_bp = Blueprint('bulid_team', __name__)

@build_team_bp.route('/api/bulid_team', methods = ["POST"])
def build_team():
    key_id = session.get('key_id')  # 세션에서 key_id 가져오기
    if not key_id:
        return redirect(url_for('login.login'))
    team_data = request.get_json()
    #팀 키, 팀이름, 주장(팀빌딩한 사람의 키), 공모전, 팀 인원(멤버 키), 인원 수 
    #입력받는 데이터 : 팀이름
    

    team_db_handler.create_team(team_data['team_name'], key_id, team_data['contest_id'], team_subject) #team_name과 contest_id는 웹으로부터 받아온 team_data를 가지고 사용
                                                                                                       #contest_detail.html 파일에서 fetch로 contest_id도 넘겨줄 수 있도록 해야함.

    