from flask import Blueprint, jsonify, request
from werkzeug.security import generate_password_hash
from db_handler import DBHandler


db_handler = DBHandler()

signup_bp = Blueprint('signup', __name__)

#아래는 데이터베이스 연동 코드

@signup_bp.route("/signup", methods = ["POST"])
def signup():
    user_data = request.get_json() #회원가입 사용자 정보를 json으로 받아옴
    print("Received user data:", user_data) 
    key_id = db_handler.collection.count_documents({}) + 1   #사용자 수에 맞춰서 key를 생성
    password = user_data['password']
    
    #비밀번호 해싱
    password_hash = generate_password_hash(password)
    user_data['password'] = password_hash #입력된 비밀번호를 해싱된 값으로 대체
    
    # 새 사용자 데이터 생성(키값과 합침)
    new_user_data = {
        "key_id": key_id,  # 사용자 고유 키
        **user_data  # 나머지 사용자 데이터
    }

    if db_handler.create_user(new_user_data):
        return 201 #성공했다는 값
    else:
        return jsonify({"message" : "이미 존재하는 사용자입니다."}), 400 