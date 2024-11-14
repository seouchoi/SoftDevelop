import pymongo
from pymongo import MongoClient
class Category_DBHandler:
    def __init__(self, collection_name='category'):
        # MongoDB 연결
        self.client = MongoClient('mongodb://localhost:27017/')
        self.db = self.client['informatrion']  # 'informatrion' 데이터베이스 선택
        self.category_collection = self.db[collection_name]  # 'category' 컬렉션 객체 선택

    def generate_category_key_id(self):
        # category 컬렉션의 문서 수에 맞춰서 key_id 값 증가
        return self.category_collection.count_documents({}) + 1

    def create_category(self, category_name):
        # key_id 생성
        key_id = self.generate_category_key_id()

        # 새로운 카테고리 데이터 생성
        new_category_data = {
            "key_id": key_id,  # 자동 증가된 key_id
            "category_name": category_name  # 사용자가 입력한 카테고리 이름
        }

        try:
            # 'category' 컬렉션에 새로운 카테고리 데이터 삽입
            self.category_collection.insert_one(new_category_data)
            return True
        except Exception as e:
            print(f"카테고리 추가 실패: {e}")
            return False