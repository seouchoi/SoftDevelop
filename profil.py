from flask import Blueprint, redirect, url_for, render_template, session, flash
from db_handler import DBHandler

#아래는 데이터 베이스와 연동 코드 작성
db_handler = DBHandler()

profil_bp = Blueprint('profil', __name__)

@profil_bp.route('/profil')
def profil():
    key_id = session.get('key_id')  # 세션에서 key_id 가져오기
    if not key_id:
        flash("로그인 후 이용 가능합니다")
        return redirect(url_for('login.login'))  # 로그인되지 않았으면 로그인 페이지로 리디렉션

    # key_id로 유저의 전체 데이터를 데이터베이스에서 조회
    user = db_handler.get_member_data(key_id)  # 전체 데이터를 가져오는 함수 호출
    
    if user:
        return render_template("profil_page.html", user=user) #수정 예정 -> 프로필 페이지에서 로그인된 홈페이지로 수정
    else:
        return redirect(url_for('login.login'))  # 유저 데이터가 없으면 로그인 페이지로 리디렉션
