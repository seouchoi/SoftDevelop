import pymongo
from pymongo import MongoClient

class DBHandler:
    def __init__(self, collection_name ='members'):
        # MongoDB 연결
        self.client = MongoClient('mongodb://localhost:27017/')  # 로컬 MongoDB 서버 연결
        self.db = self.client['Contest_team_member_matching']  # 'Contest_team_member_matching DB 선택
        self.collection = self.db['collection_name']  # 'users'라는 컬렉션 선택

    def create_user(self, member_data):
        # 데이터베이스에 사용자 추가
        try:
            # 사용자 데이터를 MongoDB에 삽입 (중복 시 오류 발생)
            self.members_collection.insert_one(member_data)
            return True
        except pymongo.errors.DuplicateKeyError:
            # 중복된 사용자 (예: member_id가 이미 존재할 경우)
            return False

    def check_user_credentials(self, user_id, password):
        # 로그인 정보 확인 (DB에서 사용자 ID와 비밀번호 확인)
        member = self.members_collection.find_one({"member_id": user_id, "member_password": password})
        return member is not None

    def close_connection(self):
        # MongoDB 연결 닫기
        self.client.close()
