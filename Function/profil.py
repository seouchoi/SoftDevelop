from flask import Blueprint, redirect, url_for, render_template, session, flash
from DBHandler.member_DBHandler import member_DBHandler
from utils.login_required import login_required

#아래는 데이터 베이스와 연동 코드 작성
member_db_handler = member_DBHandler()

profil_bp = Blueprint('profil', __name__)

@profil_bp.route('/profil', methods = ["POST", "GET"])
@login_required
def profil():
    key_id = session.get('key_id')  # 세션에서 key_id 가져오기
    # key_id로 유저의 전체 데이터를 데이터베이스에서 조회
    user = member_db_handler.get_member_data_for_key(key_id)  # 전체 데이터를 가져오는 함수 호출
    
    if user:
        return render_template("profil_page.html", user=user) #수정 예정 -> 프로필 페이지에서 로그인된 홈페이지로 수정
    else:
        return redirect(url_for('login.show_login_page'))  # 유저 데이터가 없으면 로그인 페이지로 리디렉션
