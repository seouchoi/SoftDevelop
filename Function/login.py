from flask import Blueprint, jsonify, request, redirect, url_for, render_template, session
from DBHandler.member_DBHandler import member_DBHandler

#아래는 데이터 베이스와 연동 코드 작성
member_db_handler = member_DBHandler()

login_bp = Blueprint('login', __name__)

@login_bp.route("/login")
def show_login_page():
    #처음 로그인 페이지에 접속할 경우(GET), 아무것도 적혀있지 않는 로그인 페이지 로드
    return render_template("login_page.html")

@login_bp.route("/api/login", methods = ['GET', 'POST'])
def login_activate():
    if request.method == 'POST': #로그인 요청을 받았다면 해당 코드를 실행
        data = request.get_json()
        print("Received member data:", data)
        member_id = data['member_id']
        member_password = data['member_password']

        key_id = member_db_handler.check_member_credentials(member_id, member_password)        
        if (key_id == 0): #로그인 실패시 0을 반환           
            return jsonify({"message": "사용자 ID 또는 비밀번호가 올바르지 않습니다."}), 400
        else:
            session['key_id'] = key_id
            redirect_url = session.pop('next', url_for("homepage.homepage")) #로그인 기능이 필요했던 페이지로 이동

            if redirect_url == "/api/build_team":
                redirect_url = session.pop('now')
                return jsonify({"redirect_url": redirect_url}), 200
            elif redirect_url == "/gpt":
                redirect_url = session.pop('now')
                jsonify({"redirect_url": redirect_url}), 200 
            return jsonify({"redirect_url": redirect_url}), 200 
                   