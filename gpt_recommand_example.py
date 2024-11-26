import sys
import os

# 부모 디렉토리를 sys.path에 추가하여 DBHandler 모듈을 임포트할 수 있도록 설정
parent_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
if parent_dir not in sys.path:
    sys.path.insert(0, parent_dir)

from DBHandler.member_DBHandler import member_DBHandler  # member_DBHandler 임포트

def test_get_members_by_category_and_task():
    # DBHandler 인스턴스 생성
    db_handler = member_DBHandler()

    # 테스트할 카테고리와 태스크 설정
    category = 'IT'
    task = '개발자'

    # 함수 호출하여 결과 가져오기
    members = db_handler.get_members_by_category_and_task(category, task)

    # 결과 출력
    print(f"카테고리 '{category}'와 태스크 '{task}'에 해당하는 회원 목록:")
    for member in members:
        print(f"이름: {member['name']}, 지역: {member['region']}, 카테고리: {member['category']}, 태스크: {member['task']}")

    # 데이터베이스 연결 닫기
    db_handler.close_connection()

if __name__ == "__main__":
    test_get_members_by_category_and_task()
