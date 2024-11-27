from DBHandler.category_DBhandler import Category_DBHandler

# Category_DBHandler 클래스 인스턴스 생성
category_db_handler = Category_DBHandler()

def insert_competition_categories():
    # 사용할 카테고리 목록 (4개 카테고리)
    categories = [
        "기계/제조",
        "전기/전자",
        "재료/나노",
        "생명과학/생명공학",
        "에너지/환경",
        "건축/토목",
        "항공/우주",
        "로봇공학/자동화",
        "화학공학",
        "자연과학"
    ]
    
    # 각 카테고리를 데이터베이스에 삽입
    for category_name in categories:
        if category_db_handler.create_category(category_name):
            print(f"'{category_name}' 카테고리가 성공적으로 추가되었습니다.")
        else:
            print(f"'{category_name}' 카테고리 추가에 실패했습니다.")

# 공모전 카테고리 삽입 실행
insert_competition_categories()
