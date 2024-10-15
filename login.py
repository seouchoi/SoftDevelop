from flask import Blueprint, jsonify, request, redirect, url_for, render_template, flash
from pymongo import MongoClient
from werkzeug.security import check_password_hash


#아래는 데이터 베이스와 연동 코드 작성

login_bp = Blueprint('login', __name__)

@login_bp.route("login", methods = ['GET', 'POST'])
def login():
    if request.method == 'POST': #로그인 요청을 받았다면 해당 코드를 실행
        data = request.get_json()
        user_id = data['user_id']
        password = data['password']
        
        user = users_collection.find_one({'user_id': user_id}) #데이터베이스에서 아이디가 같으면 해당 사용자의 정보를 dic로 들고옴
        
        if user is None: #id가 없다면
            flash('아이디 또는 비밀번호가 일치하지 않습니다.', 'error')
            return redirect(url_for("로그인 페이지"))
        else: #id가 존재한다면 
            if check_password_hash(user['password'], password): #입력받은 password를 해싱시켜 받아온 정보(비밀번호)와 비교
                return redirect(url_for("홈페이지(로그인)")) #일치한다면 홈페이지(로그인)으로 이동
            else: #password가 다르다면
                flash('아이디 또는 비밀번호가 일치하지 않습니다.', 'error') 
                return redirect(url_for('login.login', user_id = user_id)) #작성한 아이디가 남아있는 로그인 페이지로 이동
    #처음 로그인 페이지에 접속할 경우(GET), 아무것도 적혀있지 않는 로그인 페이지 로드
    return render_template()
                   