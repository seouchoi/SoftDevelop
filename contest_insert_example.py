from DBHandler.contest_DBhandler import Contest_DBHandler
from datetime import datetime

# Contest_DBHandler 인스턴스 생성
contest_db_handler = Contest_DBHandler()

# 공모전 정보 리스트
contests = [
    {
        "contest_name":"2025 전국 대학생 대상 자작미래자동차 경진대회",
        "max_participate":4,
        "application_start":datetime(2024,11,22),
        "application_end":datetime(2024,12,6),
        "contest_start":datetime(2025,1,16),
        "contest_end":datetime(2025,1,17),
        "category_id":1, 
        "contest_master":"영남대학교 미래자동차 공학과",
        "organization_website":"https://www.wevity.com/index_university.php?c=find&s=_university&gbn=viewok&gp=4&ix=93575",
        "image_path":"poster/contest10.jpg"
    },
    {
        "contest_name":"서울시 기계금속 제조지원센터 협업 공모전",
        "max_participate":4,
        "application_start":datetime(2024,11,15),
        "application_end":datetime(2024,12,3),
        "contest_start":datetime(2024,11,15),
        "contest_end":datetime(2024,12,3),
        "category_id":1, 
        "contest_master":"서울시기계금속제조지원센터",
        "organization_website":"https://gbmakers.or.kr/network_program/?q=YToxOntzOjEyOiJrZXl3b3JkX3R5cGUiO3M6MzoiYWxsIjt9&bmode=view&idx=126732426&t=board",
        "image_path":"poster/contest20.png"
    },
    {
        "contest_name":"제 16회 대학생 공작기계 창의 아이디어 공모전",
        "max_participate":4,
        "application_start":datetime(2024,3,4),
        "application_end":datetime(2024,4,30),
        "contest_start":datetime(2024,5,1),
        "contest_end":datetime(2024,10,30),
        "category_id":1, 
        "contest_master":"한국공작기계산업협회",
        "organization_website":"https://blog.naver.com/kommacontest/223366639736",
        "image_path":"poster/contest21.png"
    },
    {
        "contest_name":"제14회 전국학생설계경진대회",
        "max_participate":4,
        "application_start":datetime(2024, 4, 8),
        "application_end":datetime(2024,5, 3),
        "contest_start":datetime(2024,8,26),
        "contest_end":datetime(2024,9,23),
        "category_id":1, 
        "contest_master":"대한기계학회",
        "organization_website":"http://kscdc.ksme.or.kr/",
        "image_path":"poster/contest22.png"
    },
    {
        "contest_name":"2024 엔지니어링산업 경진대회",
        "max_participate":4,
        "application_start":datetime(2024,3,4),
        "application_end":datetime(2024,4,3),
        "contest_start":datetime(2024, 4,15),
        "contest_end":datetime(2024, 5, 17),
        "category_id":1, 
        "contest_master":"산업통상자원부",
        "organization_website":"https://www.engcontest.or.kr/",
        "image_path":"poster/contest23.jpg"
    },
    {
        "contest_name":"2024 소공인 기술 경진대회",
        "max_participate":4,
        "application_start":datetime(2024,8,28),
        "application_end":datetime(2024,9,27),
        "contest_start":datetime(2024,10,16),
        "contest_end":datetime(2024,10,18),
        "category_id":1, 
        "contest_master":"서울경제진흥원",
        "organization_website":"https://sba.all-con.co.kr/",
        "image_path":"poster/contest24.png"
    }, #------------------1. 기계

    {
        "contest_name":"제 2회 (주) NovaLoop배 게임 제작 공모전",
        "max_participate":4,
        "application_start":datetime(2024,11,1),
        "application_end":datetime(2024,11,30),
        "contest_start":datetime(2024,11,1),
        "contest_end":datetime(2024,11,30),
        "category_id":2,
        "contest_master":"㈜NovaLoop",
        "organization_website":"https://docs.google.com/forms/d/e/1FAIpQLSc_NE3tbZXwgwAtJ2vETeIi1kvGqDeysLXeoA__NAXHFuFYIg/viewform",
        "image_path":"poster/contest17.png"
    },
    {
        "contest_name":"2024 전국 대학생 대상 자작전기자동차 경진대회",
        "max_participate":4,
        "application_start":datetime(2023, 12, 15),
        "application_end":datetime(2024, 1,5),
        "contest_start":datetime(2024,1, 25),
        "contest_end":datetime(2024,1, 26),
        "category_id":2,
        "contest_master":"영남대학교 미래자동차 공학과",
        "organization_website":"https://drive.google.com/drive/folders/1XIoWiHMufE1jLQ15ufHtpzWJKzix6rSd",
        "image_path":"poster/contest25.jpg"
    },
    {
        "contest_name":"2024 전기에너지 대국민 아이디어 공모전",
        "max_participate":3,
        "application_start":datetime(2024,6, 3),
        "application_end":datetime(2024, 7, 31),
        "contest_start":datetime(2024,6, 3),
        "contest_end":datetime(2024, 7, 31),
        "category_id":2,
        "contest_master":"대한전기협회, 한국에너지공단",
        "organization_website":"https://www.kea.kr/sub_news/notice.php?mode=view&number=3884&b_name=notice",
        "image_path":"poster/contest26.jpg"
    },
    {
        "contest_name":"I.E. 경진대회 (Intelligent Electronics Competition)",
        "max_participate":5,
        "application_start":datetime(2024, 5, 1),
        "application_end":datetime(2024, 5, 23),
        "contest_start":datetime(2024, 7, 2),
        "contest_end":datetime(2024, 7, 2),
        "category_id":2,
        "contest_master":"전력전자학회, 산업통상자원부",
        "organization_website":"https://conf.kipe.or.kr/2024s/pages/IE.vm",
        "image_path":"poster/contest27.jpg"
    },
    {
        "contest_name":"전자신문 ICT 논문 공모대제전",
        "max_participate":3,
        "application_start":datetime(2024,4,1),
        "application_end":datetime(2024,10,18),
        "contest_start":datetime(2024,11, 18),
        "contest_end":datetime(2024,12,24),
        "category_id":2,
        "contest_master":"전자신문사, 웹케시그룹, 과학기술정보통신부",
        "organization_website":"https://contest.etnews.com/16th/",
        "image_path":"poster/contest28.jpg"
    },
    {
        "contest_name":"전기사랑 미디어콘텐츠대전",
        "max_participate":4,
        "application_start":datetime(2024,3,11),
        "application_end":datetime(2024,10,4),
        "contest_start":datetime(2024,3,11),
        "contest_end":datetime(2024,10,4),
        "category_id":2,
        "contest_master":"서한국전기안전공사",
        "organization_website":"https://www.wevity.com/?c=find&s=1&gbn=viewok&gp=6&ix=87784",
        "image_path":"poster/contest29.jpg"
    }, #--------------2. 전기전자

    {
        "contest_name":"나노영챌린지 2024",
        "max_participate":4,
        "application_start":datetime(2024,3,21),
        "application_end":datetime(2024,4,10),
        "contest_start":datetime(2024,7,3),
        "contest_end":datetime(2024,7,5),
        "category_id":3,
        "contest_master":"나노기술연구협의회",
        "organization_website":"https://www.kontrs.or.kr/news/notice.php?admin_mode=read&no=669",
        "image_path":"poster/contest30.png"
    },
    {
        "contest_name":"제5회 부식 사례 포스터 공모전",
        "max_participate":1,
        "application_start":datetime(2024,4,1),
        "application_end":datetime(2024,9,30),
        "contest_start":datetime(2024,4,1),
        "contest_end":datetime(2024,9,30),
        "category_id":3,
        "contest_master":"	한국부식방식학회",
        "organization_website":"http://www.corrosionkorea.org/board/notice/?id=notice&ss=on&sn=off&sc=off&search=&ct=&page=&ctype=&no=3320",
        "image_path":"poster/contest32.jpg"
    },
    {
        "contest_name":"제3회 양자나노과학연구단 미술공모전",
        "max_participate":4,
        "application_start":datetime(2023,11,29),
        "application_end":datetime(2024,2,29),
        "contest_start":datetime(2024,5,15),
        "contest_end":datetime(2024,5,16),
        "category_id":3,
        "contest_master":"양자과학연구단, 이화여자대학교 기초과학연구원",
        "organization_website":"https://www.ibs.re.kr/cop/bbs/BBSMSTR_000000000736/selectBoardArticle.do?nttId=24464&pageIndex=1&searchCnd=&searchWrd=",
        "image_path":"poster/contest33.jpg"
    },
    {
        "contest_name":"제8회 한국전기전자재료학회 재료사진 공모전",
        "max_participate":1,
        "application_start":datetime(2024,4,19),
        "application_end":datetime(2021, 4,19),
        "contest_start":datetime(2024,6,24),
        "contest_end":datetime(2024,6,25),
        "category_id":3,
        "contest_master":"한국전기전자재료학회",
        "organization_website":"https://www.kieeme.or.kr/06_informations/informations01.htm?Item=board3&mode=view&s_t=1&No=396",
        "image_path":"poster/contest35.jpg"
    },
    {
        "contest_name":"2021 나노 콘테스트",
        "max_participate":1,
        "application_start":datetime(2021,9,17),
        "application_end":datetime(2021,10,4),
        "contest_start":datetime(2021, 9, 17),
        "contest_end":datetime(2021, 10,4),
        "category_id":3,
        "contest_master":"경상남도, 밀양시 / 경남테크노파크, 한국재료연구원",
        "organization_website":"https://www.wevity.com/index_university.php?c=find&s=_university&gbn=viewok&gp=885&ix=55868",
        "image_path":"poster/contest31.jpg"
    },
    {
        "contest_name":"재료공학 동영상 공모대회",
        "max_participate":4,
        "application_start":datetime(2021,8,1),
        "application_end":datetime(2021,8,15),
        "contest_start":datetime(2021, 9,1),
        "contest_end":datetime(2021,10,8),
        "category_id":3,
        "contest_master":"대한금속재료학회",
        "organization_website":"https://kim.or.kr/main/",
        "image_path":"poster/contest36.jpg"
    }, #------------3. 재료/나노
    
    {
        "contest_name":"2024 생명연구자원 AI활용 경진대회",
        "max_participate":3,
        "application_start":datetime(2024,8,28),
        "application_end":datetime(2024,10,11),
        "contest_start":datetime(2024,8,28),
        "contest_end":datetime(2024,10,11),
        "category_id":4,
        "contest_master":"과학기술정보통신부, 한국생명공학연구원, 국가생명연구자원정보센터",
        "organization_website":"https://dacon.io/competitions/official/236355/overview/rules",
        "image_path":"poster/contest37.jpg"
    },
    {
        "contest_name":"한국바이오안전성정보센터 블로그 제9기 SMART LMO 기자단 모집",
        "max_participate":1,
        "application_start":datetime(2022,4,11),
        "application_end":datetime(2022,5,8),
        "contest_start":datetime(2022,5,1),
        "contest_end":datetime(2022,11,30),
        "category_id":4,
        "contest_master":"한국생명공학연구원 바이오안전성정보센터",
        "organization_website":"https://blog.naver.com/lmoman/222697344964",
        "image_path":"poster/contest39.jpg"
    },
    {
        "contest_name":"2024 KBCH 시민패널 모집",
        "max_participate":1,
        "application_start":datetime(2024,4,8),
        "application_end":datetime(2024,4,24),
        "contest_start":datetime(2024,5,1),
        "contest_end":datetime(2024,10,31),
        "category_id":4,
        "contest_master":"한국생명공학연구원 바이오안전성정보센터",
        "organization_website":"https://www.biosafety.or.kr/portal/page/h_07?bbscttPid=5481&bbsPid=8",
        "image_path":"poster/contest38.jpg"
    },
    {
        "contest_name":"유전자검사 서포터즈 젠토커 2기 모집",
        "max_participate":6,
        "application_start":datetime(2024,9,24),
        "application_end":datetime(2024,10,4),
        "contest_start":datetime(2024,10,11),
        "contest_end":datetime(2025,1,31),
        "category_id":4,
        "contest_master":"마크로젠",
        "organization_website":"https://gentok.net/",
        "image_path":"poster/contest40.jpg"
    },
    {
        "contest_name":"2024년 한국생명공학연구원 제5기 온라인 서포터즈",
        "max_participate":4,
        "application_start":datetime(2024,1,24),
        "application_end":datetime(2024,2,12),
        "contest_start":datetime(2024,2,26),
        "contest_end":datetime(2024,12,15),
        "category_id":4,
        "contest_master":"한국생명공학연구원",
        "organization_website":"https://www.kribb.re.kr/kor/sub03/sub03_01_03_view.jsp?keyField=b_title&page=1&nowBlock=0&b_idx=33601",
        "image_path":"poster/contest41.jpg"
    },
    {
        "contest_name":"서울바이오허브 아이디어 부트캠프",
        "max_participate":2,
        "application_start":datetime(2023,12,20),
        "application_end":datetime(2024,1,7),
        "contest_start":datetime(2024,1,12),
        "contest_end":datetime(2024,2,17),
        "category_id":4,
        "contest_master":"서울특별시, 한국과학기술연구원, 고려대학교",
        "organization_website":"https://docs.google.com/forms/d/e/1FAIpQLSdp1lyyeAWEsqTOvUr6MeG1GTom6b5g5EXKjPgc4JPl4W4HCA/closedform",
        "image_path":"poster/contest42.jpg"
    }, #-----------------4. 생명과학

    {
        "contest_name": "2024년 NIA 지속 가능한 에너지 솔루션 제안 공모전",
        "max_participate": 1,
        "application_start": datetime(2024, 9, 1),
        "application_end": datetime(2025, 9, 30),
        "contest_start": datetime(2025, 11, 1),
        "contest_end": datetime(2025, 11, 8),
        "category_id": 5,  
        "contest_master":"NIA 한국지능정보사회진흥원",
        "organization_website": "https://www.nia.or.kr/site/nia_kor/ex/bbs/View.do?cbIdx=99835&bcIdx=27191&parentSeq=27191",
        "image_path": "poster/contest1.png"
    },
    {
        "contest_name":"원자력 미래기술 아이디어 부트캠프",
        "max_participate":1,
        "application_start":datetime(2024,11,20),
        "application_end":datetime(2024,12,17),
        "contest_start":datetime(2025,1,13),
        "contest_end":datetime(2025,1,24),
        "category_id":5,
        "contest_master":"한국원자력협력재단",
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
        "contest_master":"화성시",
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
        "contest_master":"매일경제 MBN, M매경미디어그룹, 매경비즈",
        "organization_website":"https://wonderchild.co.kr/",
        "image_path":"poster/contest16.png"
    },
    {
        "contest_name":" 2024 전기에너지 대국민 아이디어 공모전",
        "max_participate":3,
        "application_start":datetime(2024,6,3),
        "application_end":datetime(2025,7,31),
        "contest_start":datetime(204,6,3),
        "contest_end":datetime(2024,7,31),
        "category_id":5,
        "contest_master":"대한전기협회, 한국에너지공단",
        "organization_website":"https://www.kea.kr/sub_news/notice.php?mode=view&number=3884&b_name=notice",
        "image_path":"poster/contest43.jpg"
    },
    {
        "contest_name":"2024 제7기 청년 에너지 드림 리그",
        "max_participate":5,
        "application_start":datetime(2024,3,25),
        "application_end":datetime(2024,4,12),
        "contest_start":datetime(2024,3,25),
        "contest_end":datetime(2024,9,26),
        "category_id":5,
         "contest_master":"한국중부발전",
        "organization_website":"https://www.komipo.co.kr/kor/board/BRD_000020/boardView.do?mnCd=FN100101&boardSeq=18081&pageIndex=1",
        "image_path":"poster/contest44.jpg"
    },#------------5. 에너지

    {
        "contest_name": "제 19회 2024년 한국공간디자인 전국공모전",
        "max_participate": 4,
        "application_start": datetime(2024, 11, 1),
        "application_end": datetime(2025, 11, 22),
        "contest_start": datetime(2025, 12, 3),
        "contest_end": datetime(2025, 12, 3),
        "category_id": 6,  # 건축
        "contest_master":"한국공간디자인협회",
        "organization_website": "http://www.kosda.org/bbs/board.php?bo_table=v4_01&wr_id=80",
        "image_path":"poster/poster1.png"
    },
    {
        "contest_name": "공공주택 설계개선 업무노하우 공모전",
        "max_participate": 5,
        "application_start": datetime(2024, 11, 1),
        "application_end": datetime(2025, 11, 15),
        "contest_start": datetime(2025, 3, 10),
        "contest_end": datetime(2025, 4, 10),
        "category_id": 6,  # 건축
        "contest_master":"LH 설계검증처",
        "organization_website": "https://www.lh.or.kr/board.es?mid=a10601020000&bid=0034&list_no=721497&act=view",
        "image_path": "poster/poster2.jpg"
    },
    {
        "contest_name": "증권박물관 이전 건립 설계공모",
        "max_participate": 2,
        "application_start": datetime(2024, 11, 25),
        "application_end": datetime(2024, 12, 11),
        "contest_start": datetime(2025, 1, 14),
        "contest_end": datetime(2025, 1, 27),
        "category_id": 6,  # 건축
        "contest_master":"(재)케이에스디나눔재단",
        "organization_website": "https://ksdmuseum-design.kr/bbs/board.php?bo_table=notice&wr_id=15",
        "image_path": "poster/poster3.jpeg"
    },
    {
        "contest_name": "비홈 네이밍 공모전",
        "max_participate": 1,
        "application_start": datetime(2024, 11, 14),
        "application_end": datetime(2024, 11, 30),
        "contest_start": datetime(2024, 11, 30),
        "contest_end": datetime(2024, 11, 30),
        "category_id": 6,  # 건축
        "contest_master":"비홈컴퍼니",
        "organization_website": "https://linkareer.com/activity/209422",
        "image_path": "poster/poster4.png"
    },
    {
        "contest_name": "2025 정림학생건축상(고고학자와_발명가)",
        "max_participate": 3,
        "application_start": datetime(2024, 11, 4),
        "application_end": datetime(2025, 1, 9),
        "contest_start": datetime(2025, 1, 13),
        "contest_end": datetime(2025, 1, 16),
        "category_id": 6,  # 건축
        "contest_master":"정림건축문화재단",
        "organization_website": "https://www.junglimaward.com/",
        "image_path": "poster/poster5.png"
    }, #---------6. 건축
    
    {
        "contest_name": "2024년 서울 지능형 사물인터넷(AIoT) 해커톤 대회",
        "max_participate": 4,
        "application_start": datetime(2024,7, 19),
        "application_end": datetime(2024, 8, 31),
        "contest_start": datetime(2024, 10, 10),
        "contest_end": datetime(2024, 10, 11),
        "category_id": 8,  # 로봇공학 자동화
        "contest_master":"",
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
        "contest_master":"",
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
        "contest_master":"",
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
        "contest_master":"",
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
        "contest_master":"",
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
        "contest_master":"",
        "organization_website":"https://www.blaybus.com/activities/407/landing",
        "image_path":"poster/contest9.png"
    },

    {
        "contest_name":"글로벌 청년 임팩트 해커톤",
        "max_participate":1,
        "application_start":datetime(2024,11,18),
        "application_end":datetime(2024,12,8),
        "contest_start":datetime(2024,12,27),
        "contest_end":datetime(2024,12,28),
        "category_id":10,
        "contest_master":"",
        "organization_website":"https://wfuna.or.kr/program_global_impact_hackathon_2024",
        "image_path":"poster/contest14.png"
    },

    {
        "contest_name":"헬로소프트 코스페이시스 작품 공모전",
        "max_participate":1,
        "application_start":datetime(2024,11,17),
        "application_end":datetime(2024,11,30),
        "contest_start":datetime(2024,11,17),
        "contest_end":datetime(2024,11,30),
        "category_id":12,
        "contest_master":"",
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
        "contest_master":"",
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
        "contest_master":"",
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
        contest['contest_master'],
        contest['organization_website'], 
        image_path=contest['image_path']
    )
