from flask import Blueprint, render_template, jsonify, session
from DBHandler.contest_DBhandler import Contest_DBHandler
import random

homepage_bp = Blueprint('homepage', __name__)

#아래는 전체 공모전을 받아와야함.(데이터베이스를 통해서)
contest_db_handler = Contest_DBHandler()


#처음 켰을 때 보여지는 홈페이지
@homepage_bp.route("/")
def homepage():
    contests_data = contest_db_handler.get_all_contest() #공모전 데이터 모두 가져오기
    random_contest_data = random.sample(contests_data, k = 3) #그 중 3개를 랜덤으로 뽑아서 홈페이지에 보여줌
    if 'key_id' in session: #session이 True인지 확인(로그인상태인지 아닌지)
        return render_template("login_homepage.html", contest_data = random_contest_data) #홈페이지(로그인 상태)
    else:
        return render_template("logout_homepage.html", contest_data = random_contest_data) #홈페이지(로그아웃 상태)

#홈페이지 안에서의 작동되는 기능################


################################################