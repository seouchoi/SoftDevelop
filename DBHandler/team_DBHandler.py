from DBHandler.member_DBHandler import member_DBHandler  # member_DBHandler import
from DBHandler.contest_DBhandler import Contest_DBHandler  # Contest_DBHandler import
from pymongo import MongoClient
from datetime import datetime

class Team_DBHandler:
    def __init__(self, collection_name='teams'):
        # MongoDB 연결
        self.client = MongoClient('mongodb://localhost:27017/')
        self.db = self.client['informatrion']  # 'informatrion' 데이터베이스 선택
        self.team_collection = self.db[collection_name]  # 'teams' 컬렉션 객체 선택

        # 인스턴스화된 member_DBHandler 및 Contest_DBHandler 가져오기
        self.member_db_handler = member_DBHandler()
        self.contest_db_handler = Contest_DBHandler()

    def generate_team_id(self):
        # team 컬렉션의 문서 수에 맞춰서 team_id 값 증가
        return self.team_collection.count_documents({}) + 1

    def create_team(self, team_name, team_leader_id, contest_id):
        # team_id 생성
        team_id = self.generate_team_id()
        contest_id = int(contest_id)

        # 팀장 정보 가져오기 (전체 멤버 정보 포함)
        team_leader = self.member_db_handler.get_member_data_for_key(team_leader_id)
#영차
        if not team_leader:
            print("팀장을 찾을 수 없습니다.")
            return False
        
        # 팀 주제(공모전 정보) 가져오기
        contest = self.contest_db_handler.get_contest_by_id(contest_id)

        if not contest:
            print("해당 공모전 정보를 찾을 수 없습니다.")
            return False

        # 팀 데이터 생성 (팀원은 비어있음)
        new_team_data = {
            "team_id": team_id,
            "team_name": team_name,
            "team_leader_id": team_leader_id,
            "team_leader": team_leader,  # 팀장의 전체 member 정보
            "contest_id": contest_id,
            "contest_name": contest["contest_name"],  # 공모전 이름
            "team_members": [team_leader],  # 팀원들을 비어있지 않도록 팀장만 임베디드로 저장
            "creation_date": datetime.now(),  # 팀 생성 날짜
        }

        try:
            # 'teams' 컬렉션에 새로운 팀 데이터 삽입
            self.team_collection.insert_one(new_team_data)
            print(f"'{team_name}' 팀이 성공적으로 생성되었습니다.")
            return True
        except Exception as e:
            print(f"팀 생성 실패: {e}")
            return False

    def add_team_member(self, team_id, member_id):
        # 특정 팀에 팀원 추가
        team = self.team_collection.find_one({"team_id": team_id})
        
        if not team:
            print(f"팀 {team_id}을(를) 찾을 수 없습니다.")
            return False
        
        # 팀원 데이터 가져오기
        team_member = self.member_db_handler.get_member_data_for_key(member_id)

        if not team_member:
            print(f"팀원 {member_id}을(를) 찾을 수 없습니다.")
            return False

        # 팀원 추가
        try:
            self.team_collection.update_one(
                {"team_id": team_id}, 
                {"$push": {"team_members": team_member}}
            )
            print(f"팀 {team_id}에 팀원 {member_id}이(가) 성공적으로 추가되었습니다.")
            return True
        except Exception as e:
            print(f"팀원 추가 실패: {e}")
            return False


    def get_team_info(self, team_id):
            """
            특정 team_id에 해당하는 팀의 정보를 조회하여 반환합니다.
            :return: 팀 정보 딕셔너리 또는 None
            """
            try:
                # team_id로 팀 정보 조회
                team = self.team_collection.find_one(
                    {"team_id": team_id},
                    {
                        "_id": 0,  # MongoDB의 _id 필드를 제외
                        "team_id": 1,
                        "team_name": 1,
                        "team_leader_id": 1,
                        "team_leader": 1,
                        "contest_id": 1,
                        "contest_name": 1,
                        "team_members": 1,
                        "creation_date": 1
                    }
                )

                if team:
                    return team # 딕셔너리 형식으로 반환 
                else:
                    print(f"팀 ID {team_id}을(를) 찾을 수 없습니다.")
                    return None

            except Exception as e:
                print(f"팀 정보 조회 실패: {e}")
                return None