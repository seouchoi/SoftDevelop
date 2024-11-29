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
        title: "2024년 NIA 지속 가능한 에너지 솔루션 제안 공모전",
        description: "친환경 에너지 및 지속가능한 에너지 솔루션 아이디어를 모집합니다.",
        deadline: "2024-11-30",
        organizer: "한국전력공사(KEPCO)",
        image: "poster/contest1.png",
        url: "https://www.nia.or.kr/site/nia_kor/ex/bbs/View.do?cbIdx=99835&bcIdx=27191&parentSeq=27191"
    },
    {
        title: "2024년 서울 지능형 사물인터넷(AIoT) 해커톤 대회",
        description: "인공지능(AI) 기술을 접목한 IoT 기기 및 시스템을 설계하여 지능형 사물인터넷 솔루션을 개발하세요.",
        deadline: "2024-08-31",
        organizer: "서울특별시",
        image: "poster/contest2.png",
        url: "https://www.seoul.go.kr/news/news_notice.do#view/415895"
    },
    {
        title: "2024년 AI·미디어 융합기술 공모전",
        description: "AI 기술을 활용한 혁신적인 아이디어 공모전입니다.",
        deadline: "2024-09-23",
        organizer: "과학기술정보통신부",
        image: "poster/contest3.png",
        url: "https://www.msit.go.kr/bbs/view.do?sCode=user&mId=129&mPid=224&pageIndex=&bbsSeqNo=100&nttSeqNo=3179039&searchOpt=ALL&searchTxt="
    },
    {
        title: "2024년 항공우주논문상 공모전",
        description: "항공우주 산업과 4차 산업혁명 기술의 융합을 연구하며, 창의적인 아이디어를 제시하세요.",
        deadline: "2024-09-30",
        organizer: "한국항공우주산업(KAI)",
        image: "poster/contest4.png",
        url: "https://m.koreaaero.com/KO/Sustainability/AerospaceJournalPrizeInfo.aspx"
    },
    {
        title: "디지털 혁신 해커톤 2024",
        description: "참가자들은 48시간 동안 팀을 이루어 문제 해결 프로토타입을 제작하고 발표합니다.",
        deadline: "2024-09-06",
        organizer: "고용노동부, 한국기술교육대학교 직업능력심사평가원",
        image: "poster/contest5.png",
        url: "http://k-digitalhackathon.kr/"
    },
    {
        title: "석유 화학 올림피아드",
        description: "탄소중립 시대를 위한 친환경 화학 공정과 새로운 재활용 기술을 개발하는 아이디어를 찾는 공모전입니다.",
        deadline: "2024-11-11",
        organizer: "LG화학, 한국화학공학회",
        image: "poster/contest6.png",
        url: "https://www.lgchem.com/main/index"
    },
    {
        title: "88로봇데이 차세대로봇 아이디어 공모전",
        description: "고령자를 돕거나 지구 환경에 유익한 로봇 아이디어를 제시하는 공모전입니다.",
        deadline: "2024-12-30",
        organizer: "한양대학교 ERICA 지능형로봇사업단",
        image: "poster/contest7.png",
        url: "https://www.etedu.co.kr/shop/item.php?it_id=1657070988"
    },
    {
        title: "나노영챌린지 2024 대학(원)생 나노기술 공모전",
        description: "나노기술을 활용한 첨단 신소재 개발과 응용 사례를 제시하는 공모전입니다.",
        deadline: "2024-04-10",
        organizer: "나노기술연구협회",
        image: "poster/contest8.png",
        url: "https://www.kontrs.or.kr/main/main.php"
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
