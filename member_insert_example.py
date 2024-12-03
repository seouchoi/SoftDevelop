import sys
import os
import random
import string

# 부모 디렉토리를 sys.path에 추가하여 DBHandler 모듈을 임포트할 수 있도록 설정
parent_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
if parent_dir not in sys.path:
    sys.path.insert(0, parent_dir)

from DBHandler.member_DBHandler import member_DBHandler  # member_DBHandler 임포트

def generate_random_string(length):
    # 지정된 길이의 랜덤 문자열 생성
    return ''.join(random.choices(string.ascii_lowercase + string.digits, k=length))

def generate_phone_number():
    # 랜덤한 전화번호 생성
    return "010-" + "".join([str(random.randint(0, 9)) for _ in range(4)]) + "-" + "".join([str(random.randint(0, 9)) for _ in range(4)])

def generate_email(member_id):
    domains = ['naver.com', 'gmail.com', 'gnu.ac.kr']
    return member_id + '@' + random.choice(domains)

def insert_members():
    # DBHandler 인스턴스 생성
    db_handler = member_DBHandler()

    # 카테고리와 태스크 목록 정의
    categories_tasks = {
        "AI": ["기획자", "엔지니어"],
        "IT": ["기획자", "개발자", "UI/UX 디자이너"],
        "기계/제조": ["기획자", "엔지니어", "품질관리"],
        "전기/전자": ["기획자", "설계 엔지니어", "개발자"],
        "재료/나노": ["기획자", "엔지니어", "개발자"],
        "생명과학/생명공학": ["기획자", "데이터 분석", "실험 관리자"],
        "에너지/환경": ["기획자", "엔지니어", "데이터 분석"],
        "건축/토목": ["기획자", "설계 엔지니어"],
        "항공/우주": ["기획자", "엔지니어", "개발자"],
        "로봇공학/자동화": ["기획자", "하드웨어 엔지니어", "소프트웨어 엔지니어"],
        "화학공학": ["기획자", "공정설계", "실험 관리자"],
        "자연과학": ["기획자", "연구원", "자료 분석가"]
    }

    existing_member_ids = set()

    for i in range(1000):
        # 고유한 member_id 생성 (중복 방지)
        while True:
            member_id = "user" + generate_random_string(6)
            if member_id not in existing_member_ids:
                existing_member_ids.add(member_id)
                break

        # 기타 회원 데이터 생성
        member_password = 'password123'  # 실제로는 해시 처리 필요
        name = 'user' + str(i)
        member_phone_number = generate_phone_number()
        email = generate_email(member_id)
        region = random.choice(['서울', '부산', '인천', '대구', '대전', '광주', '울산', '수원'])

        # 랜덤한 카테고리 선택
        category = random.choice(list(categories_tasks.keys()))

        # 선택된 카테고리의 태스크 목록 가져오기
        tasks_in_category = categories_tasks[category]

        # 랜덤한 태스크 선택
        task = random.choice(tasks_in_category)

        # 회원 데이터 생성
        member_data = {
            'member_id': member_id,
            'member_password': member_password,
            'name': name,
            'member_phone_number': member_phone_number,
            'email': email,
            'region': region,
            'category': category,
            'task': task
            # 'key_id'는 create_member에서 자동으로 추가됩니다.
        }

        # 회원 데이터 삽입
        key_id = db_handler.create_member(member_data)
        if key_id:
            print(f"회원 '{member_data['member_id']}' (key_id: {key_id})가 성공적으로 추가되었습니다.")
        else:
            print(f"회원 '{member_data['member_id']}' 추가에 실패했습니다.")

    # 데이터베이스 연결 닫기
    db_handler.close_connection()

if __name__ == "__main__":
    insert_members()
