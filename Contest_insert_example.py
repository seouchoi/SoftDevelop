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
        "category_id": 8,  # 건축
        "organization_website": "http://www.kosda.org/bbs/board.php?bo_table=v4_01&wr_id=80",
        "image_path":"poster/poster1.png"
    },
    {
        "contest_name": "공공주택_설계개선_업무노하우_공모전",
        "max_participate": 5,
        "application_start": datetime(2024, 11, 1),
        "application_end": datetime(2025, 11, 15),
        "contest_start": datetime(2025, 3, 10),
        "contest_end": datetime(2025, 4, 10),
        "category_id": 8,  # 건축
        "organization_website": "https://www.lh.or.kr/board.es?mid=a10601020000&bid=0034&list_no=721497&act=view",
        "image_path": "poster/poster2.jpg"
    },
    {
        "contest_name": "증권박물관_이전_건립_설계공모",
        "max_participate": 2,
        "application_start": datetime(2024, 11, 25),
        "application_end": datetime(2024, 12, 11),
        "contest_start": datetime(2025, 1, 14),
        "contest_end": datetime(2025, 1, 27),
        "category_id": 8,  # 건축
        "organization_website": "https://ksdmuseum-design.kr/bbs/board.php?bo_table=notice&wr_id=15",
        "image_path": "poster/poster3.jpeg"
    },
    {
        "contest_name": "비홈_네이밍_공모전",
        "max_participate": 1,
        "application_start": datetime(2024, 11, 14),
        "application_end": datetime(2024, 11, 30),
        "contest_start": datetime(2024, 11, 30),
        "contest_end": datetime(2024, 11, 30),
        "category_id": 8,  # 건축
        "organization_website": "https://linkareer.com/activity/209422",
        "image_path": "poster/poster4.png"
    },
    {
        "contest_name": "2025_정림학생건축상(고고학자와_발명가)",
        "max_participate": 3,
        "application_start": datetime(2024, 11, 4),
        "application_end": datetime(2025, 1, 9),
        "contest_start": datetime(2025, 1, 13),
        "contest_end": datetime(2025, 1, 16),
        "category_id": 8,  # 건축
        "organization_website": "https://www.junglimaward.com/",
        "image_path": "poster/poster5.png"
    },
    {
        "contest_name": "친환경 에너지 관리 시스템 공모전",
        "max_participate": 3,
        "application_start": datetime(2024, 11, 4),
        "application_end": datetime(2025, 1, 9),
        "contest_start": datetime(2025, 1, 13),
        "contest_end": datetime(2025, 1, 16),
        "category_id": 8,  # 건축
        "organization_website": "https://via.placeholder.com/300x200",
        "image_path": "poster/poster5.png"
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
