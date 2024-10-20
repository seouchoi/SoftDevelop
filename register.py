from flask import Blueprint, jsonify, request
from werkzeug.security import generate_password_hash
register_bp = Blueprint('register', __name__)

#아래는 데이터베이스 연동 코드

users = [] #등록된 사용자들 리스트(수정해야함.)

@register_bp.route("/register", methods = ["POST"])
def register():
    user_data = request.get_json() #회원가입 사용자 정보를 json으로 받아옴
    print("Received user data:", user_data) 
    key_id = len(users) + 1     #사용자 수에 맞춰서 key를 생성
    user_id = user_data['user_id']   #사용자 id가 있는지 없는지 판단하기 위해서 변수에 넣음
    password = user_data['password']
    
    for user in users:  #key와 id중 하나라도 중복되는게 있으면 오류를 발생
        if user['key_id'] == key_id:
            return jsonify({"message" : "User key id is already exists."}), 400
        elif user['user_id'] == user_id:
            return jsonify({"message" : "Id is already exists."}), 400
    
    #비밀번호 해싱
    password_hash = generate_password_hash(password)
    user_data['password'] = password_hash #입력된 비밀번호를 해싱된 값으로 대체
    
    # 새 사용자 데이터 생성
    new_user_data = {
        "key_id": key_id,  # 사용자 고유 키
        **user_data  # 나머지 사용자 데이터
    }
    users.append(new_user_data) #사용자 리스트에 추가
    print(users)
    return jsonify({"message": "User registered successfully!"}), 201