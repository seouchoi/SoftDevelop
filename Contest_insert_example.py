from DBHandler.contest_DBhandler import Contest_DBHandler
from datetime import datetime

# Contest_DBHandler 인스턴스 생성
contest_db_handler = Contest_DBHandler()

# 공모전 정보 리스트
contests = [
    {
        "contest_name": "제 19회 2024년 한국공간디자인 전국공모전",
        "max_participate": 4,
        "application_start": datetime(2024, 11, 1),
        "application_end": datetime(2025, 11, 22),
        "contest_start": datetime(2025, 12, 3),
        "contest_end": datetime(2025, 12, 3),
        "category_id": 3,  # 예시: 3번 카테고리
        "organization_website": "http://www.kosda.org/bbs/board.php?bo_table=v4_01&wr_id=80",
        "image_path":r"C:\Users\hi034\OneDrive\바탕 화면\SoftDevelop\front\templates\pictures\logo.png"
    },
    {
        "contest_name": "2024년도 건설기계안전 콘텐츠 공모전",
        "max_participate": 3,
        "application_start": datetime(2024, 10, 21),
        "application_end": datetime(2025, 11, 15),
        "contest_start": datetime(2025, 11, 25),
        "contest_end": datetime(2025,  12, 15),
        "category_id": 3,  # 예시: 2번 카테고리
        "organization_website": "https://www.osan.go.kr/portal/saeol/gosi/view.do?notAncmtMgtNo=45958&mId=0302010000",
        "image_path" : r"C:\Users\hi034\OneDrive\바탕 화면\SoftDevelop\front\templates\pictures\logo.png"
    },
    {
        "contest_name": "공공주택_설계개선_업무노하우_공모전",
        "max_participate": 5,
        "application_start": datetime(2024, 11, 1),
        "application_end": datetime(2025, 11, 15),
        "contest_start": datetime(2025, 3, 10),
        "contest_end": datetime(2025, 4, 10),
        "category_id": 3,  # 예시: 4번 카테고리
        "organization_website": "https://www.lh.or.kr/board.es?mid=a10601020000&bid=0034&list_no=721497&act=view",
        "image_path": r"C:\Users\hi034\OneDrive\바탕 화면\SoftDevelop\front\templates\pictures\logo.png"
    }
]

# 공모전 정보 삽입
for contest in contests:
    contest_db_handler.create_contest(
        contest['contest_name'], 
        contest['max_participate'], 
        contest['application_start'], 
        contest['application_end'], 
        contest['contest_start'], 
        contest['contest_end'], 
        contest['category_id'], 
        contest['organization_website'], 
        image_path=contest['image_path']
    )
