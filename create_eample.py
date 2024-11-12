import requests
import json

# 서버 URL 설정 (로컬 서버에서 실행할 경우)
url = "http://127.0.0.1:5000/signup"

# 회원가입에 사용할 예시 데이터
member_data = {
    "member_id": "testuser123",  # 아이디
    "member_password": "testpassword123",  # 비밀번호
    "member_phone_number": "010-1234-5678",  # 전화번호
    "region": "Seoul",  # 지역
    "task_name": "Software Development"  # 업무명
}

# JSON 형식으로 데이터 보내기
response = requests.post(url, json=member_data)

# 서버 응답 출력
if response.status_code == 201:
    print("회원가입 성공!")
else:
    print(f"회원가입 실패: {response.json()['message']}")
