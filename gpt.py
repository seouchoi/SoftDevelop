from flask import Blueprint, jsonify, request
import os
import openai 

#openai.api_key

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

@gpt_bp.route("/gpt", methods = ["GET", "POST"])
def gpt():
  receive_prompt_json = request.get_json()
  prompt = receive_prompt_json["prompt"]

  response = openai.ChatCompletion.create(
    model="gpt-4o-mini", #모델 지정
    messages = [{"role":"system", "content": f"{system_instruction}"},
        {"role": "user", "content": f"{prompt}"}],
    temperature=0,
  )

  gpt_response = response['choices'][0]['message']['content']

  
  return jsonify({"message": gpt_response}), 200
