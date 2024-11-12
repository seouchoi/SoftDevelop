from flask import Blueprint, jsonify, request, Response
from werkzeug.security import generate_password_hash
from member_db_handler import member_DBHandler

# member_db_handler 객체 생성
member_db_handler = member_DBHandler()

signup_bp = Blueprint('signup', __name__)

@signup_bp.route("/signup", methods=["POST"])
def signup():
    # 회원가입 사용자 정보를 JSON으로 받아옴
    member_data = request.get_json()
    print("Received member data:", member_data)
    
    # member_id와 member_password를 받음
    member_id = member_data['member_id']
    member_password = member_data['member_password']  # password -> member_password로 수정

    # 기존 회원이 있는지 확인 (member_id로 확인)
    existing_member = member_db_handler.check_existing_member(member_id)

    if existing_member:
        # 회원이 이미 존재하면 에러 메시지 반환
        return jsonify({"message": "이미 존재하는 아이디입니다."}), 400

    # 비밀번호 해싱
    password_hash = generate_password_hash(member_password)  # member_password를 해싱
    member_data['member_password'] = password_hash  # 입력된 비밀번호를 해싱된 값으로 대체

    # key_id 값 생성 (현재 DB에서 문서 수에 맞춰서 증가시킴)
    key_id = member_db_handler.generate_key_id()

    # 새 사용자 데이터 생성 (key_id와 기존 데이터를 합침)
    new_member_data = {
        "key_id": key_id,  # 사용자 고유 키
        **member_data  # 나머지 사용자 데이터
    }

    # 회원가입 시 데이터베이스에 새 사용자 추가
    if member_db_handler.create_member(new_member_data):
        return Response(status=201)  # 성공
    else:
        return jsonify({"message": "회원가입 실패. 다시 시도해주세요."}), 500
