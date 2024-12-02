from pymongo import MongoClient

# FavoriteContests_DBHandler.py

from pymongo import MongoClient

class FavoriteContests_DBHandler:
    def __init__(self):
        # MongoDB 클라이언트 초기화
        self.client = MongoClient('mongodb://localhost:27017/')  # 실제 MongoDB 연결 문자열로 변경하세요
        self.db = self.client['informatrion']  # 데이터베이스 이름을 실제 이름으로 변경하세요
        self.collection = self.db['favorite_contest ']
        
        # user_id와 contest_id의 조합에 대한 고유 인덱스 생성 (중복 방지)
        self.collection.create_index([('user_id', 1), ('contest_id', 1)], unique=True)
        
    def add_favorite_contest(self, user_id, contest_id):
        """
        관심 공모전을 추가합니다.
        """
        favorite_data = {
            'user_id': user_id,
            'contest_id': contest_id
        }

        try:
            self.collection.insert_one(favorite_data)
            return True  # 추가 성공
        except Exception as e:
            print(f"Error adding favorite contest: {e}")
            return False  # 추가 실패 (중복 등)

    def remove_favorite_contest(self, user_id, contest_id):
        """
        관심 공모전을 제거합니다.
        """
        result = self.collection.delete_one({'user_id': user_id, 'contest_id': contest_id})
        return result.deleted_count > 0  # 제거 성공 여부 반환

    def get_favorite_contests(self, user_id):
        """
        사용자의 관심 공모전 ID 목록을 반환합니다.
        """
        favorites = self.collection.find({'user_id': user_id}, {'_id': 0, 'contest_id': 1})
        return [favorite['contest_id'] for favorite in favorites]

    def is_favorite(self, user_id, contest_id):
        """
        특정 공모전이 사용자의 관심 공모전인지 확인합니다.
        """
        return self.collection.find_one({'user_id': user_id, 'contest_id': contest_id}) is not None

    def close_connection(self):
        """
        MongoDB 연결을 닫습니다.
        """
        self.client.close()
