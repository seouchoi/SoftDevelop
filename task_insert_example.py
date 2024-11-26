import sys
import os

# 부모 디렉토리 경로를 얻어 sys.path에 추가
parent_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
if parent_dir not in sys.path:
    sys.path.insert(0, parent_dir)

from DBHandler.task_DBHandler import Task_DBHandler  # Task_DBHandler import

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

def insert_tasks():
    task_db_handler = Task_DBHandler()
    for category, tasks in categories_tasks.items():
        for task_name in tasks:
            task_data = {
                "task_name": task_name,
                "category": category
            }
            # 태스크 생성
            result = task_db_handler.create_task(task_data)
            if result:
                print(f"'{task_name}' 태스크가 성공적으로 추가되었습니다. (카테고리: {category})")
            else:
                print(f"'{task_name}' 태스크 추가에 실패했습니다. (카테고리: {category})")
    task_db_handler.close_connection()

if __name__ == "__main__":
    insert_tasks()

