from DBHandler.team_DBHandler import Team_DBHandler  # Team_DBHandler import
from DBHandler.member_DBHandler import member_DBHandler  # member_DBHandler import
from DBHandler.contest_DBhandler import Contest_DBHandler  # Contest_DBHandler import
from datetime import datetime

# DBHandler 인스턴스 생성
team_db_handler = Team_DBHandler()
member_db_handler = member_DBHandler()
contest_db_handler = Contest_DBHandler()

def test_create_team():
    # 예시로 사용할 데이터
    team_name = "AI 공모전 팀"
    team_leader_id = 1  # 팀장의 member_id (여기서는 임의의 값 사용)
    contest_id = 2  # 공모전 ID (임의의 값 사용)
    team_subject = "AI 기술을 활용한 혁신적인 솔루션 개발"

    # 팀 생성
    result = team_db_handler.create_team(team_name, team_leader_id, contest_id, team_subject)

    # 결과 출력
    if result:
        print(f"'{team_name}' 팀이 성공적으로 생성되었습니다.")
    else:
        print(f"'{team_name}' 팀 생성에 실패했습니다.")

def test_add_team_member():
    # 예시로 사용할 팀 ID와 팀원 ID
    team_id = 1  # 이미 생성된 팀의 ID
    member_id = 2  # 팀에 추가할 팀원 ID (임의의 값 사용)

    # 팀에 팀원 추가
    result = team_db_handler.add_team_member(team_id, member_id)

    # 결과 출력
    if result:
        print(f"팀 ID {team_id}에 팀원 ID {member_id}가(이) 성공적으로 추가되었습니다.")
    else:
        print(f"팀 ID {team_id}에 팀원 ID {member_id} 추가에 실패했습니다.")

# 팀 생성 테스트 실행
test_create_team()

# 팀원 추가 테스트 실행
#test_add_team_member()
