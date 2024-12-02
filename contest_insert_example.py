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
        "category_id": 6,  # 건축
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
        "category_id": 6,  # 건축
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
        "category_id": 6,  # 건축
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
        "category_id": 6,  # 건축
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
        "category_id": 6,  # 건축
        "organization_website": "https://www.junglimaward.com/",
        "image_path": "poster/poster5.png"
    },
    {
        "contest_name": "2024년 NIA 지속 가능한 에너지 솔루션 제안 공모전",
        "max_participate": 1,
        "application_start": datetime(2024, 9, 1),
        "application_end": datetime(2025, 9, 30),
        "contest_start": datetime(2025, 11, 1),
        "contest_end": datetime(2025, 11, 8),
        "category_id": 5,  # 에너지
        "organization_website": "https://www.nia.or.kr/site/nia_kor/ex/bbs/View.do?cbIdx=99835&bcIdx=27191&parentSeq=27191",
        "image_path": "poster/contest1.png"
    },
    {
        "contest_name": "2024년 서울 지능형 사물인터넷(AIoT) 해커톤 대회",
        "max_participate": 4,
        "application_start": datetime(2024,7, 19),
        "application_end": datetime(2024, 8, 31),
        "contest_start": datetime(2024, 10, 10),
        "contest_end": datetime(2024, 10, 11),
        "category_id": 8,  # 로봇공학 자동화
        "organization_website": "https://www.seoul.go.kr/news/news_notice.do#view/415895",
        "image_path": "poster/contest2.png"
    },
    {
        "contest_name": "2024년 AI·미디어 융합기술 공모전",
        "max_participate": 1,
        "application_start": datetime(2024, 7, 25),
        "application_end": datetime(2024, 9, 23),
        "contest_start": datetime(2024, 7, 25),
        "contest_end": datetime(2024, 9, 23),
        "category_id": 8,  # 로봇공학 자동화
        "organization_website": "https://www.msit.go.kr/bbs/view.do?sCode=user&mId=129&mPid=224&pageIndex=&bbsSeqNo=100&nttSeqNo=3179039&searchOpt=ALL&searchTxt=",
        "image_path": "poster/contest3.png"
    },
    {
        "contest_name": "K-디지털 트레이닝 해커톤 2024",
        "max_participate": 6,
        "application_start": datetime(2024, 8, 19),
        "application_end": datetime(2024, 9, 6),
        "contest_start": datetime(2024, 8, 19),
        "contest_end": datetime(2024, 9, 6),
        "category_id": 8,  #로봇공학 자동화 
        "organization_website": "http://k-digitalhackathon.kr/",
        "image_path": "poster/contest5.png"
    },
    {
        "contest_name": "석유 화학 올림피아드",
        "max_participate": 1,
        "application_start": datetime(2024, 7, 1),
        "application_end": datetime(2024, 7, 6),
        "contest_start": datetime(2024, 7, 12),
        "contest_end": datetime(2024, 8, 12),
        "category_id": 9,  # 화학공학
        "organization_website": "https://www.lgchem.com/main/index",
        "image_path": "poster/contest6.png"
    },
    {
        "contest_name": "나노영챌린지 2024 대학(원)생 나노기술 공모전",
        "max_participate": 1,
        "application_start": datetime(2024, 3, 21),
        "application_end": datetime(2024, 4, 10),
        "contest_start": datetime(2024, 6, 1),
        "contest_end": datetime(2024, 9, 23),
        "category_id": 9,  # 화학공학
        "organization_website": "https://www.kontrs.or.kr/main/main.php",
        "image_path": "poster/contest8.png"
    },
    {
        "contest_name":"Blaybus 실전 앱 개발 경진대회",
        "max_participate":7,
        "application_start":datetime(2024,12,2),
        "application_end":datetime(2024,12,29),
        "contest_start":datetime(2025,1,5),
        "contest_end":datetime(2025,1,17),
        "category_id": 8,
        "organization_website":"https://www.blaybus.com/activities/407/landing",
        "image_path":"poster/contest9.png"
    },
    {
        "contest_name":"2025 전국 대학생 대상 자작미래자동차 경진대회",
        "max_participate":4,
        "application_start":datetime(2024,11,22),
        "application_end":datetime(2024,12,6),
        "contest_start":datetime(2025,1,16),
        "contest_end":datetime(2025,1,17),
        "category_id":1, 
        "organization_website":"https://www.wevity.com/index_university.php?c=find&s=_university&gbn=viewok&gp=4&ix=93575",
        "image_path":"poster/contest10.jpg"
    },
    {
        "contest_name":"원자력 미래기술 아이디어 부트캠프",
        "max_participate":0,
        "application_start":datetime(2024,11,20),
        "application_end":datetime(2024,12,17),
        "contest_start":datetime(2025,1,13),
        "contest_end":datetime(2025,1,24),
        "category_id":5,
        "organization_website":"https://www.konicof.or.kr/neti/html/sub05/0501.html?mode=V&no=2c5658c4e5b49ee04fb7ee30328ebf46",
        "image_path":"poster/contest11.jpg"
    }, 
    {
        "contest_name":"화성시 동부권 공공정원화 설계공모",
        "max_participate":1,
        "application_start":datetime(2024,11,6),
        "application_end":datetime(2024,12,5),
        "contest_start":datetime(2025,1,14),
        "contest_end":datetime(2025,1,14),
        "category_id":5,
        "organization_website":"https://www.c3ka.com/design-contest-for-public-garden-in-the-eastern-district-of-hwaseong-city/",
        "image_path":"poster/contest13.png"
    },
    {
        "contest_name":"제 4회 WONDERCHILD 창의발명대회",
        "max_participate":2,
        "application_start":datetime(2024,11,15),
        "application_end":datetime(2025,1,20),
        "contest_start":datetime(2025,2,7),
        "contest_end":datetime(2025,2,8),
        "category_id":5,
        "organization_website":"https://wonderchild.co.kr/",
        "image_path":"poster/contest16.png"
    },
    {
        "contest_name":"글로벌 청년 임팩트 해커톤",
        "max_participate":1,
        "application_start":datetime(2024,11,18),
        "application_end":datetime(2024,12,8),
        "contest_start":datetime(2024,12,27),
        "contest_end":datetime(2024,12,28),
        "category_id":10,
        "organization_website":"https://wfuna.or.kr/program_global_impact_hackathon_2024",
        "image_path":"poster/contest14.png"
    },
    {
        "contest_name":"제 2회 (주) NovaLoop배 게임 제작 공모전",
        "max_participate":4,
        "application_start":datetime(2024,11,1),
        "application_end":datetime(2024,11,30),
        "contest_start":datetime(2024,11,1),
        "contest_end":datetime(2024,11,30),
        "category_id":2,
        "organization_website":"https://docs.google.com/forms/d/e/1FAIpQLSc_NE3tbZXwgwAtJ2vETeIi1kvGqDeysLXeoA__NAXHFuFYIg/viewform",
        "image_path":"poster/contest17.png"
    },
    {
        "contest_name":"헬로소프트 코스페이시스 작품 공모전",
        "max_participate":1,
        "application_start":datetime(2024,11,17),
        "application_end":datetime(2024,11,30),
        "contest_start":datetime(2024,11,17),
        "contest_end":datetime(2024,11,30),
        "category_id":12,
        "organization_website":"https://cafe.naver.com/cospaces/",
        "image_path":"poster/contest15.png"
    },
    {
        "contest_name":"컴투스 글로벌 게임개발 공모전 ‘컴:온 2024’",
        "max_participate":10,
        "application_start":datetime(2024,11,19),
        "application_end":datetime(2024,12,30),
        "contest_start":datetime(2024,11,19),
        "contest_end":datetime(2024,12,30),
        "category_id":12,
        "organization_website":"https://www.com2us.com/gamecontest",
        "image_path":"poster/contest18.png"
    },
    {
        "contest_name":"2024~2025년 한국석유공사 데이터 분석 공모전",
        "max_participate":4,
        "application_start":datetime(2024,10,14),
        "application_end":datetime(2025,1,22),
        "contest_start":datetime(2024,10,14),
        "contest_end":datetime(2025,1,22),
        "category_id":12,
        "organization_website":"https://www.knoc.co.kr/sub05/sub05_5_5.jsp?page=1&num=243&mode=view&field=&text=&bid=DATA5&ses=USERSESSION&psize=12",
        "image_path":"poster/contest19.png"
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
