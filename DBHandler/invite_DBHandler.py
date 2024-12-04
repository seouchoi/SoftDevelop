import pymongo
from pymongo import MongoClient 
from datetime import datetime
from DBHandler.contest_DBhandler import Contest_DBHandler

contest_db_handler = Contest_DBHandler()

class invite_DBHandler:
    def __init__(self, collection_name='invite'):
        # MongoDB 연결 설정
        self.client = MongoClient('mongodb://localhost:27017/')  # 로컬 MongoDB 서버에 연결
        self.db = self.client['informatrion']  #초대 기능에 대한 정보를 담고있는 invite collection 
        self.invite_collection = self.db[collection_name]  # 'invite' 컬렉션 선택
        
          # team_id에 인덱스 생성 (고유값 보장)
        self.invite_collection.create_index("invite_id", unique=True)

    #key_id 증가하는 부분 
    def generate_key_id(self):
        # key_id 값 생성: 현재 DB에서 문서 수에 맞춰서 증가시킴
        return self.invite_collection.count_documents({}) + 1

    #invite collection에 알림을 삽입하는 코드 
    def insert_invite(self, sender_id, team_id, receiver_id, message, contest_id):
        invite_id = invite_DBHandler.generate_key_id(self)
        contest_id = int(contest_id)
        sender_id = int(sender_id)
        contest_name = contest_db_handler.get_contest_name(contest_id)
        # 초대 데이터 생성
        invite_data = {
            'invite_id': invite_id,
            'sender_id': sender_id,
            'team_id': team_id,
            'receiver_id': receiver_id,
            'message': message,
            'contest_id': contest_id,
            'contest_name': contest_name,
            'read': False,
            'invite_type': 'leader_to_member',  # 또는 'user_to_team'       #누가 누구에게 초대를 보내는지 구분(팀장->추천받은회원 : leader_to_member, 일반 회원->leader)
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

    def get_invite_data(self, invite_id):
        """
        invite_id로 전체 초대 알림 정보를 가져오는 코드.
        """
        invites_cursor = self.invite_collection.find(
            {'invite_id': invite_id},
            {'_id': 0}
        ).sort('timestamp', -1)
        return list(invites_cursor)
    
    def send_team_application(self, user_id, team_id, message):
        """
        일반 유저가 특정 팀에 지원(초대)을 보내는 함수입니다.

        :param user_id: 지원하는 유저의 ID (sender_id)
        :param team_id: 지원하려는 팀의 ID
        :param message: 지원 메시지
        :return: 성공 시 invite_id, 실패 시 None
        """
        try:
            # 팀 정보 가져오기
            team = self.db['teams'].find_one({"team_id": team_id})
            if not team:
                print(f"팀 ID {team_id}을(를) 찾을 수 없습니다.")
                return None

            team_leader_id = team['team_leader_id']
            contest_id = team['contest_id']
            contest_name = team['contest_name']

            # 초대 메시지 생성
            application_message = f"{message}\n\n지원자 ID: {user_id}가 팀에 지원합니다."

            # 초대 데이터 생성
            invite_id = self.generate_key_id()
            invite_data = {
                'invite_id': invite_id,
                'sender_id': user_id,
                'team_id': team_id,
                'receiver_id': team_leader_id,
                'message': application_message,
                'contest_id': contest_id,
                'contest_name': contest_name,
                'read': False,
                'invite_type': 'user_to_team',
                'timestamp': datetime.now()
            }

            # invite 컬렉션에 초대 데이터 삽입
            self.invite_collection.insert_one(invite_data)
            print(f"팀 ID {team_id}에 대한 지원이 성공적으로 전송되었습니다.")
            return invite_id

        except Exception as e:
            print(f"팀 지원 실패: {e}")
            return None
        
        
    # 특정 팀에 대한 모든 지원 초대를 조회하는 함수
    def get_team_applications(self, team_id):
        """
        특정 팀에 대한 모든 지원(초대)을 조회합니다.

        :param team_id: 조회할 팀의 ID
        :return: 지원 초대 리스트 또는 빈 리스트
        """
        try:
            # 팀 정보 가져오기
            team = self.db['teams'].find_one({"team_id": team_id})
            if not team:
                print(f"팀 ID {team_id}을(를) 찾을 수 없습니다.")
                return []

            team_leader_id = team['team_leader_id']

            # 'invite_type'이 'user_to_team'이고, receiver_id가 팀장인 초대 조회
            applications_cursor = self.invite_collection.find(
                {
                    'invite_type': 'user_to_team',
                    'receiver_id': team_leader_id,
                    'contest_id': team['contest_id']
                },
                {'_id': 0}
            ).sort('timestamp', -1)

            return list(applications_cursor)

        except Exception as e:
            print(f"팀 지원 조회 실패: {e}")
            return []

