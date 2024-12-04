from pymongo import MongoClient
from datetime import datetime

class Awards_DBHandler:
    def __init__(self):
        # MongoDB 연결 설정
        self.client = MongoClient('mongodb://localhost:27017/')
        self.db = self.client['informatrion']  # 실제 데이터베이스 이름으로 변경하세요
        self.collection = self.db['awards']

    #수상경력에 정보 기입하는 코드
    def add_award(self, user_id, txt, rank):
        """
        수상 정보를 데이터베이스에 저장합니다.
        """
        award_data = {
            'user_id': user_id,
            'txt': txt,          # 공모전 이름
            '수상경력': rank,     # 수상 순위
            'timestamp': datetime.now()
        }
        self.collection.insert_one(award_data)

    #순위 기반 계산하는 코드(1등:5점, 2등:4점,3등:3점,4등:2점,5등:1점)
    def calculate_user_award_points(self, user_id):
        """
        사용자의 수상 경력 점수를 계산합니다.
        """
        # 수상 순위에 따른 점수 매핑
        rank_points = {1: 5, 2: 4, 3: 3, 0: 0} #0은 수상없음, 수상은 3등까지있음
        
        # 사용자의 수상 기록 가져오기
        awards = self.collection.find({'user_id': user_id})
        
        total_points = 0
        for award in awards:
            rank = award.get('수상경력')
            points = rank_points.get(rank, 0)  # 순위에 따른 점수, 순위가 없거나 5등 밖이면 0점
            total_points += points
        
        return total_points

    #참여횟수를 +1점으로 계산하여 참여경력 점수를 구하기 
    def get_user_participation_count(self, user_id):
        """
        사용자의 총 참여 횟수를 반환합니다.
        """
        participation_count = self.collection.count_documents({'user_id': user_id})
        return participation_count
    


    def close_connection(self):
        """
        MongoDB 연결을 닫습니다.
        """
        self.client.close()
