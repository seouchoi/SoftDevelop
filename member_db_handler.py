import pymongo
from pymongo import MongoClient
from werkzeug.security import check_password_hash

class member_DBHandler:
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

    def get_member_data_for_key(self, key_id): #key_id를 이용해 로그인된 사람의 정보 DB로부터 들고오기
        member = self.members_collection.find_one({"key_id": key_id})
        return member
    
    def get_member_data_catgory_and_task(self, query): #gpt에서 쿼리문을 받아와 멤버를 찾고, 그 멤버들의 정보를 넘겨줌
        member = list(self.members_collection.find(query)) #리스트 안에 딕셔너리 형태로 반환
        return member

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
