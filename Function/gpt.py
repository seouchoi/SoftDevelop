from flask import Blueprint, jsonify, request, render_template
import os
import openai 
from DBHandler.member_DBHandler import member_DBHandler

##openai.api_key

INSTRUCTIONS = ["1. Extract the competition topic and required number of participants from the provided message.",
                 "2. Ensure the recommended roles match the required number of participants."]
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
                                "1. category - task, 2. category - task, 3. category - task"                                                        
                                 """, *INSTRUCTIONS])

gpt_bp = Blueprint('gpt', __name__)

member_db_handler = member_DBHandler()

@gpt_bp.route("/gpt")
def show_gpt_page():
  return render_template("question_page.html")

@gpt_bp.route("/api/gpt", methods = ["GET", "POST"])
def gpt():
  receive_prompt_json = request.get_json()
  prompt = receive_prompt_json["prompt"]

  response = openai.ChatCompletion.create(
    model="gpt-4o-mini", #모델 지정
    messages = [{"role":"system", "content": f"{system_instruction}"},
        {"role": "user", "content": f"{prompt}"}],
    temperature=0,
  )
  #gpt 답변
  gpt_response = response['choices'][0]['message']['content']

  #아래 코드는 모두 형식에 맞게 바꿔야함
  #DB로부터 분야, 업무에 알맞은 사람들 찾아오는 코드
  sliced_list = gpt_response.split(...) #gpt답변을 DB로 보낼 수 있게 슬라이싱
  searched_member_list = [] #검색된 회원들 정보를 담을 리스트
  for i in range(0, len(sliced_list), 2): #분야 - 업무, 분야 - 업무 ...로 나올것이기 때문에 i를 2씩 건너뛰면서 for문
    query = {'category' : sliced_list[i], 'task' : sliced_list[i + 1]} #쿼리문 작성 
    searched_member = member_db_handler.get_member_data_catgory_and_task(query)
    searched_member_list.extend(searched_member)

  #아래 코드는 받아온 정보를 통해 팀장에게 보여줄 회원들 정보만 보여줄 코드
  filtered_member_list = [] #회원들 정보만 보여줄 리스트
  for member_data in searched_member_list:
    filtered_info = {
        'name': member_data['name'],
        'region': member_data['region'],
        'category': member_data['category'],
        'task': member_data['task']
    }
    filtered_member_list.append(filtered_info)

  return jsonify(filtered_member_list), 200
