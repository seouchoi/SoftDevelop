import pymongo
from pymongo import MongoClient
from werkzeug.security import check_password_hash
from DBHandler.award_DBHandler import Awards_DBHandler
from DBHandler.favorite_contest import FavoriteContests_DBHandler

class member_DBHandler:
    def __init__(self, collection_name ='members'):
        # MongoDB 연결
        self.client = MongoClient('mongodb://localhost:27017/')  # 로컬 MongoDB 서버 연결
        self.db = self.client['informatrion']  # information이름의 DB 선택
        self.members_collection = self.db[collection_name]  # 'members'라는 컬렉션 선택(테이블)

        # Awards_DBHandler 인스턴스 생성
        self.award_handler = Awards_DBHandler()

        # FavoriteContests_DBHandler 인스턴스 생성
        self.favorite_handler = FavoriteContests_DBHandler()
        
    def create_member(self, member_data):
        # 새로운 회원을 DB에 추가
        try:
            current_member_count = self.members_collection.count_documents({})  # 전체 문서 수
            member_data['key_id'] = current_member_count + 1  # 새 user_id는 현재 수 + 1
            self.members_collection.insert_one(member_data)
            return True
        except Exception as e:
            print(f"회원가입 실패: {e}")
            return False
        
    def get_member_data_for_key(self, key_id): #key_id를 이용해 로그인된 사람의 정보 DB로부터 들고오기
        member = self.members_collection.find_one({"key_id": key_id})
        return member
    
    def get_member_data_catgory_and_task(self, query): #gpt에서 쿼리문을 받아와 멤버를 찾고, 그 멤버들의 정보를 넘겨줌
        member = list(self.members_collection.find(query)) #리스트 안에 딕셔너리 형태로 반환
        return member

    def check_member_credentials(self, member_id, member_password):
        # 로그인 정보 확인 (DB에서 사용자 ID와 비밀번호 확인)
        member = self.members_collection.find_one({"member_id": member_id})  # 사용자 ID로 회원 정보 가져오기

        if member and check_password_hash(member['member_password'], member_password):  # 비밀번호 비교
            return member['key_id']  # 로그인 성공 시 해당 멤버의 key_id 반환
        else:
            return 0  # 로그인 실패 시 0 반환
        
    #회원가입시 db에 동일한 정보 있는지 확인하는 부분 
    def check_existing_member(self, member_id):
        # member_id로 기존 회원을 확인
        existing_member = self.members_collection.find_one({"member_id": member_id})
        return existing_member

    #key_id 증가하는 부분 
    def generate_key_id(self):
        # key_id 값 생성: 현재 DB에서 문서 수에 맞춰서 증가시킴
        return self.members_collection.count_documents({}) + 1

    def close_connection(self):
        # MongoDB 연결 닫기
        self.client.close()
        
        
    #DB에서 member data 받아오는 함수 
    def get_member_data_for_key(self, key_id):  
        # 주어진 key_id로 회원 데이터를 찾기
        member = self.members_collection.find_one({"key_id": key_id})  # key_id를 사용하여 해당 회원 정보 찾기
        return member

    def get_members_by_category_and_task(self, category, task):
        # 주어진 카테고리와 태스크를 가진 회원들을 검색하여 리스트로 반환
        try:
            query = {'category': category, 'task': task}
            members_cursor = self.members_collection.find(query, {'key_id': 1, 'name': 1, 'region': 1, 'category': 1, 'task': 1})   #1은 포함, 0은 제외시킨다는 의미
            return list(members_cursor)
        except Exception as e:
            print(f"회원 검색 실패: {e}")
            return []
        
        
        #sfd
        #필터 최종 결과 
        #관심 공모전을 표시한 회원들 사이의 total_score기반 순위가 상단에 배치
        #그 밑에 관심 공모전을 표시하지 않은 회원들 사이의 total_score 기반 순위가 하단에 배치 
    def recommend_members(self, category, task, contest_id):
        """
        카테고리와 태스크에 따라 회원들을 추천 순위로 정렬하여 반환합니다.
        관심 공모전에 표시한 회원들을 우선으로 배치합니다.
        """
        # 1차 필터링: 카테고리와 태스크가 일치하는 회원들 가져오기
        members = self.get_members_by_category_and_task(category, task)

        # 각 회원에 대해 점수 계산 수행
        for member in members:
            user_id = member['key_id']

            # 2차 필터링: 수상 경력 점수 계산
            award_points = self.award_handler.calculate_user_award_points(user_id)

            # 3차 필터링: 참여 이력 점수 계산 (참여 횟수 × 1점)
            participation_points = self.award_handler.get_user_participation_count(user_id)

            # 총점 계산
            total_score = award_points + participation_points

            # 4차 필터링: 해당 공모전에 관심을 표시한 경우
            is_favorite = self.favorite_handler.is_favorite(user_id, contest_id)

            # 회원 정보에 점수 및 관심 여부 추가
            member['award_points'] = award_points
            member['participation_points'] = participation_points
            member['is_favorite'] = is_favorite
            member['total_score'] = total_score

        # 추천 순위 결정: 먼저 is_favorite으로 정렬하고, 그 다음 total_score로 정렬
        sorted_members = sorted(
            members,
            key=lambda x: (x['is_favorite'], x['total_score']),
            reverse=True
        )

        return sorted_members
