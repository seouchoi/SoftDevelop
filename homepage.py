from flask import Blueprint, render_template, jsonify

homepage_bp = Blueprint('homepage', __name__)

#아래는 전체 공모전을 받아와야함.(데이터베이스를 통해서)
data = {
    'IT': [{'name': 'AI 프로젝트'}, {'name': '웹 개발'}, {'name': '데이터 분석'}],
    'Marketing': [{'name': '디지털 마케팅'}, {'name': '브랜드 전략'}, {'name': '광고 캠페인'}]
}

#처음 켰을 때 보여지는 홈페이지
@homepage_bp.route("/")
def homepage():
    return render_template("homepage.html")

#홈페이지 안에서 다른 페이지로 이동하는 코드들#####
@homepage_bp.route("/register")
def register_page():
    return render_template("register_page.html")

@homepage_bp.route("/question")
def question_page():
    return render_template("question_page.html")
################################################



#홈페이지 안에서의 작동되는 기능################
@homepage_bp.route('/get_items/<category>')
def get_items(category):
    items = data.get(category, [])  # 해당 카테고리의 데이터 가져오기
    return jsonify(items)


################################################