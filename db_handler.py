import pymongo
from pymongo import MongoClient
from werkzeug.security import check_password_hash

class DBHandler:
    def __init__(self, collection_name ='members'):
        # MongoDB 연결
        self.client = MongoClient('mongodb://localhost:27017/')  # 로컬 MongoDB 서버 연결
        self.db = self.client['informatrion']  # information이름의 DB 선택
        self.members_collection = self.db[collection_name]  # 'members'라는 컬렉션 선택(테이블)

    def create_member(self, member_data):
        #기존 member_id가 존재한다면 오류(아래 코드는 존재하는지 검사하는 코드)
        existing_member = self.members_collection.find_one({"member_id": member_data['member_id']})
        if existing_member:
            return False
        else:#만약 존재하지않는다면 회원가입시켜줌
            self.members_collection.insert_one(member_data)
            return True       

    def check_member_credentials(self, member_id, password):
        # 로그인 정보 확인 (DB에서 사용자 ID와 비밀번호 확인)
        member = self.members_collection.find_one({"member_id": member_id})  # 사용자 ID로 회원 정보 가져오기

        if member and check_password_hash(member['password'], password):  # 비밀번호 비교
            return member['key_id']  # 로그인 성공 시 해당 멤버의 key_id 반환
        else:
            return 0  # 로그인 실패 시 0 반환

    def close_connection(self):
        # MongoDB 연결 닫기
        self.client.close()
