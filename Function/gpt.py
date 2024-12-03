from flask import Blueprint, jsonify, request, render_template
import os
import openai
from DBHandler.member_DBHandler import member_DBHandler
from utils.login_required import login_required
# OpenAI API 키 설정 (필요한 경우)
#openai.api_key

INSTRUCTIONS = [
    "1. Extract the competition topic and required number of participants from the provided message.",
    "2. Ensure the recommended roles match the required number of participants."
]
system_instruction = "\n".join(["""You will be provided with a message that contains a competition description and the number of participants needed. Your task is to do the following:
Based on the competition topic, thoroughly research online to accurately identify the necessary fields,
and then suggest relevant fields and roles from given list.:
[AI - 기획자, 엔지니어
IT -  기획자, 개발자, UI/UX 디자이너
기계/제조 - 기획자, 엔지니어, 품질관리
전기/전자 - 기획자, 설계 엔지니어, 개발자
재료/나노 - 기획자, 엔지니어, 개발자
생명과학/생명공학 - 기획자, 데이터 분석, 실험 관리자
에너지/환경 - 기획자, 엔지니어, 데이터 분석
건축/토목 - 기획자, 설계 엔지니어
항공/우주 - 기획자, 엔지니어, 개발자
로봇공학/자동화 - 기획자, 하드웨어 엔지니어, 소프트웨어 엔지니어
화학공학 - 기획자, 공정설계, 실험 관리자
자연과학 - 기획자, 연구원, 자료 분석가]

If you determind fields and task, you must response following example:
"1. category - task
2. category - task
3. category - task"  
Provide an answer tailored to the number of people.""", *INSTRUCTIONS])

gpt_bp = Blueprint('gpt', __name__)

member_db_handler = member_DBHandler()

@gpt_bp.route("/gpt")
@login_required
def show_gpt_page():
    contest_id = request.args.get('contest_id')  # 쿼리 파라미터에서 contest_id 추출
    return render_template("question_page.html", contest_id=contest_id)

@gpt_bp.route("/api/gpt", methods=["GET", "POST"])
def gpt():
    receive_prompt_json = request.get_json()
    prompt = receive_prompt_json["prompt"]
    contest_id = receive_prompt_json["contest_id"]
    print(f"Contest ID: {contest_id}")  # contest_id를 출력해서 확인

    response = openai.ChatCompletion.create(
        model="gpt-4o-mini",  # 모델 지정
        messages=[
            {"role": "system", "content": f"{system_instruction}"},
            {"role": "user", "content": f"{prompt}"}
        ],
        temperature=0,
    )
    # GPT 답변
    gpt_response = response['choices'][0]['message']['content']
    print("GPT 응답:\n", gpt_response)

    # GPT 응답 파싱하여 카테고리와 태스크 추출
    sliced_list = []  # GPT 답변을 DB로 보낼 수 있게 슬라이싱
    lines = gpt_response.strip().split("\n")
    for line in lines:
        if line.strip():  # 빈 줄이 아닌 경우만 처리
            try:
                _, content = line.split(". ", 1)
                category, task = content.split(" - ")
                sliced_list.append({'category': category.strip(), 'task': task.strip()})
            except ValueError:
                print(f"라인 파싱 오류: {line}")
                continue
    print("파싱된 카테고리와 태스크 목록:", sliced_list)

    # 회원 검색 및 정보 수집
    searched_member_list = []  # 검색된 회원들 정보를 담을 리스트
    for item in sliced_list:
        category = item['category']
        task = item['task']
        print(f"검색 쿼리: category='{category}', task='{task}'")
        members = member_db_handler.recommend_members(category, task, contest_id)
        print(members)
        for member_data in members:
            print(member_data)
            # 필요한 정보만 추출하여 filtered_info에 저장
            filtered_info = {
                'key_id': member_data['key_id'],
                'name': member_data['name'],
                'region': member_data['region'],
                'category': member_data['category'],
                'task': member_data['task']
            }
            searched_member_list.append(filtered_info)

    # 결과 출력 또는 반환
    print("추천된 회원 목록:")
    for member in searched_member_list:
        print(member)

    # 필터링된 회원들 정보를 JSON 형태로 반환
    return jsonify(searched_member_list), 200
