import pymongo
from pymongo import MongoClient 
from datetime import datetime
from DBHandler.contest_DBhandler import Contest_DBHandler

class invite_DBHandler:
    def __init__(self, collection_name='invite'):
        # MongoDB 연결 설정
        self.client = MongoClient('mongodb://localhost:27017/')  # 로컬 MongoDB 서버에 연결
        self.db = self.client['informatrion']  #초대 기능에 대한 정보를 담고있는 invite collection 
        self.invite_collection = self.db[collection_name]  # 'invite' 컬렉션 선택

    #key_id 증가하는 부분 
    def generate_key_id(self):
        # key_id 값 생성: 현재 DB에서 문서 수에 맞춰서 증가시킴
        return self.invite_collection.count_documents({}) + 1

    #invite collection에 알림을 삽입하는 코드 
    def insert_invite(self, sender_id, receiver_id, message, contest_id):
        invite_id = invite_DBHandler.generate_key_id(self)
        contest_id = int(contest_id)
        contest_name = contest_db_handler.get_contest_name(contest_id)
        # 초대 데이터 생성
        invite_data = {
            'invite_id': invite_id,
            'sender_id': sender_id,
            'receiver_id': receiver_id,
            'message': message,
            'contest_id': contest_id,
            'contest_name': contest_name,
            'read': False,  # reciever가 읽었는지 안 읽었는지 확인하는 코드 부분
            'timestamp': datetime.now()
        }
        try:
            self.invite_collection.insert_one(invite_data)
            return invite_id  # 성공 시 invite_id 반환
        except Exception as e:
            print(f"Error inserting invite: {e}")
            return None
        
    #reciever가 읽었을 경우 bool 값을 true로 만들어 --> 이 값을 통해 reciever의 알림창에서 불빛 꺼지도록 구현 
    def mark_invite_as_read(self, invite_id):
        try:
            self.invite_collection.update_one(
                {'invite_id': invite_id},
                {'$set': {'read': True}}
            )
        except Exception as e:
            print(f"Error updating invite: {e}")

    #사용자가 받은 모든 초대 메시지를 확인할 수 있도록 한다. 
    def get_received_invites(self, user_id):
        """
        receiver_id가 user_id와 일치하는 초대 목록을 반환합니다.
        """
        invites_cursor = self.invite_collection.find(
            {'receiver_id': user_id},
            {'_id': 0}
        ).sort('timestamp', -1)
        return list(invites_cursor)    
    
    #사용자가 보낸 모든 초대 메시지를 확인할 수 있도록 한다.     
    def get_sent_invites(self, user_id):
        """
        sender_id가 user_id와 일치하는 초대 목록을 반환합니다.
        """
        invites_cursor = self.invite_collection.find(
            {'sender_id': user_id},
            {'_id': 0}
        ).sort('timestamp', -1)
        return list(invites_cursor)

    def get_unread_invites(self, user_id):
        """
        receiver_id가 user_id와 일치하고, read 값이 False인 초대 목록을 반환합니다.
        만약 읽지 않은 메시지가 없다면, 다른 값을 반환합니다.
        """
        invites_cursor = self.invite_collection.find(
            {'receiver_id': user_id, 'read': False},
            {'_id': 0}
        ).sort('timestamp', -1)
        
        # 커서를 리스트로 변환
        invites_list = list(invites_cursor)
        
        if invites_list:
            # 읽지 않은 메시지가 있으면 그 목록을 반환
            return invites_list
        else:
            # 읽지 않은 메시지가 없으면 다른 값을 반환
            return None  # 또는 원하는 다른 값

    
