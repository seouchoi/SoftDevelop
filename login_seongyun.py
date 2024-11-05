from flask import request
from flask_restx import Resource, Namespace
from db_handler import DBHandler  # 데이터베이스와의 상호작용을 위한 모듈 import

# 로그인 및 회원가입 네임스페이스 생성
auth_namespace = Namespace('auth', description='User authentication related operations')

# DB 핸들러 인스턴스 생성
db_handler = DBHandler()

# 기본 경로: 로그인 엔드포인트 정의 (예: /auth/)
@auth_namespace.route('/')
class Login(Resource):
    def post(self):
        # 프론트엔드로부터 로그인 데이터 받아오기
        data = request.json
        id = data.get('id')
        password = data.get('password')
        
        # 데이터베이스에서 사용자 확인
        if db_handler.check_user_credentials(id, password):
            return {"message": "로그인 성공"}, 200  # 상태 코드 200: OK
        else:
            return {"message": "아이디 또는 비밀번호가 잘못되었습니다."}, 401  # 상태 코드 401: Unauthorized

# 회원가입 엔드포인트 정의 (예: /auth/signup)
@auth_namespace.route('/signup')
class SignUp(Resource):
    def post(self):
        # 프론트엔드로부터 회원가입 데이터 받아오기
        data = request.json

        # 회원가입 정보 딕셔너리 구성
        member_data = {
            "key_id": data.get("key_id"),
            "member_id": data.get("member_id"),
            "member_password": data.get("member_password"),
            "member_name": data.get("member_name"),
            "member_email": data.get("member_email"),
            "region": data.get("region"),
            "member_phone_number": data.get("member_phone_number"),
            "task_name": data.get("task_name"),
            "interested_contest": data.get("interested_contest")
        }

        # 데이터베이스에 사용자 추가
        if db_handler.create_user(member_data):
            return {"message": "회원가입 성공"}, 201  # 상태 코드 201: Created
        else:
            return {"message": "이미 존재하는 사용자입니다."}, 409  # 상태 코드 409: Conflict
