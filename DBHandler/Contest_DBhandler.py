import gridfs
from pymongo import MongoClient
from datetime import datetime

class Contest_DBHandler:
    def __init__(self, collection_name='contests'):
        # MongoDB 연결
        self.client = MongoClient('mongodb://localhost:27017/')
        self.db = self.client['informatrion']  # 'informatrion' 데이터베이스 선택
        self.contest_collection = self.db[collection_name]  # 'contests' 컬렉션 객체 선택
        self.fs = gridfs.GridFS(self.db)  # GridFS 객체 생성

    def generate_contest_id(self):
        # contest 컬렉션의 문서 수에 맞춰서 contest_id 값 증가
        return self.contest_collection.count_documents({}) + 1

    def create_contest(self, contest_name, max_participate, application_start, application_end, contest_start, contest_end, category_id, organization_website, image_path=None):
        # contest_id 생성
        contest_id = self.generate_contest_id()

        # 공모전 데이터 생성
        new_contest_data = {
            "contest_id": contest_id,
            "contest_name": contest_name,
            "max_participate": max_participate,
            "application_start": application_start,
            "application_end": application_end,
            "contest_start": contest_start,
            "contest_end": contest_end,
            "category_id": category_id,
            "organization_website": organization_website,  # 기관의 웹사이트 URL 추가
            "image_path": image_path
        }

        # 이미지 처리 (이미지가 있다면 GridFS에 저장)
        # if image_path:
        #     with open(image_path, "rb") as image_file:
        #         # GridFS에 이미지 저장
        #         image_id = self.fs.put(image_file, filename=f"{contest_name}_image")
        #         new_contest_data["image_id"] = image_id  # 이미지의 GridFS ID를 데이터에 추가

        try:
            # 'contests' 컬렉션에 새로운 공모전 데이터 삽입
            self.contest_collection.insert_one(new_contest_data)
            print(f"'{contest_name}' 공모전이 성공적으로 추가되었습니다.")
            return True
        except Exception as e:
            print(f"공모전 추가 실패: {e}")
            return False

    #DB에서 id로 contest 정보 가져오기 
    def get_contest_by_id(self, contest_id):
        # 주어진 contest_id로 공모전 데이터를 찾기
        contest = self.contest_collection.find_one({"contest_id": contest_id})  # contest_id로 해당 공모전 정보 찾기
        return contest
    
    #category_id를 통해 부합하는 공모전 모두 가져오기(공모전 나열 용)
    def get_contest_by_category_id(self, category_id):
        contests = list(self.contest_collection.find({"category_id": category_id}))
        return contests
    
    #모든 contest가져오기 -> list로 반환
    def get_all_contest(self):
        return list(self.contest_collection.find())