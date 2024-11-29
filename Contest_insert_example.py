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
    },

    {
                title: "친환경 에너지 관리 시스템 공모전",
                description: "디지털 디자인 작품을 모집하는 공모전입니다.",
                deadline: "2024-12-31",
                organizer: "한국전력공사(KEPCO), 한국에너지공단",
                image: "https://via.placeholder.com/300x200"
            },
            {
                title: "스마트 시티 구축을 위한 IoT 솔루션",
                description: "IoT(사물인터넷) 기술을 활용하여 스마트 시티를 위한 솔루션을 개발하세요.",
                deadline: "2024-11-30",
                organizer: "국토교통부",
                image: "https://via.placeholder.com/300x200"
            },
            {
                title: "AI 기술 혁신 공모전",
                description: "AI 기술을 활용한 혁신적인 아이디어 공모전입니다.",
                deadline: "2025-01-15",
                organizer: "AI 혁신 포럼",
                image: "https://via.placeholder.com/300x200"
            },
            {
                title: "2025년 항공우주논문상 공모전",
                description: "항공우주 산업과 4차 산업혁명 기술의 융합을 연구하며, 창의적인 아이디어를 제시하세요.",
                deadline: "2025-08-15",
                organizer: "한국항공우주산업(KAI)",
                image: "https://via.placeholder.com/300x200"
            },
            {
                title: "디지털 혁신 해커톤 2024",
                description: "참가자들은 48시간 동안 팀을 이루어 문제 해결 프로토타입을 제작하고 발표합니다.",
                deadline: "2025-03-05",
                organizer: "한국정보기술연구원(KISTI) & 한국인터넷진흥원(KISA)",
                image: "https://via.placeholder.com/300x200"
            },
            {
                title: "지속가능한 화학 공정 설계 공모전",
                description: "탄소중립 시대를 위한 친환경 화학 공정과 새로운 재활용 기술을 개발하는 아이디어를 찾는 공모전입니다.",
                deadline: "2024-11-11",
                organizer: "대한화학공학회",
                image: "https://via.placeholder.com/300x200"
            },
            {
                title: "로봇 기반 사회문제 해결 공모전",
                description: "로봇을 활용한 사회적 문제(고령화, 재난 구조, 의료 지원 등) 해결 방안을 제시하는 공모전입니다.",
                deadline: "2024-12-30",
                organizer: "한국로봇산업진흥원",
                image: "https://via.placeholder.com/300x200"
            },
            {
                title: "첨단 나노소재 응용 공모전",
                description: "나노기술을 활용한 첨단 신소재 개발과 응용 사례를 제시하는 공모전입니다.",
                deadline: "2025-01-23",
                organizer: "한국재료학회",
                image: "https://via.placeholder.com/300x200"
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
