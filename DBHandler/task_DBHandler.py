import pymongo
from pymongo import MongoClient

class Task_DBHandler:
    def __init__(self, collection_name='tasks'):
        # MongoDB 연결
        self.client = MongoClient('mongodb://localhost:27017/')  # 로컬 MongoDB 서버 연결
        self.db = self.client['informatrion']  # 'information' 이름의 DB 선택
        self.tasks_collection = self.db[collection_name]  # 'tasks'라는 컬렉션 선택

    def create_task(self, task_data):
        # 새로운 태스크를 DB에 추가
        try:
            # 중복 태스크 검사
            if self.tasks_collection.find_one({"task_name": task_data['task_name'], "category": task_data['category']}):
                print(f"태스크 '{task_data['task_name']}'는 이미 존재합니다. (카테고리: {task_data['category']})")
                return False
            self.tasks_collection.insert_one(task_data)
            return True
        except Exception as e:
            print(f"태스크 추가 실패: {e}")
            return False

    def get_tasks_by_category(self, category_name):
        tasks_cursor = self.tasks_collection.find({'category': category_name}, {'_id': 0, 'task_name': 1})
        return [doc['task_name'] for doc in tasks_cursor]
    
    def close_connection(self):
        # MongoDB 연결 닫기
        self.client.close()

