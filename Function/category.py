#contests 페이지에 공모전들 나열함
from flask import Blueprint, render_template, request
from DBHandler.Contest_DBhandler import Contest_DBHandler

contest_db_handler = Contest_DBHandler()

category_bp = Blueprint('category', __name__)

@category_bp.route('/category', methods = ["POST"])
def arrange_contests():
    category_id = request.get_data() #웹으로부터 선택된 category_id들고옴(해당 분야 공모전 나열하기 위함, 알맞게 수정)
    contests_data = contest_db_handler.get_contest_by_category_id(category_id) #해당 카테고리 공모전 모두 가져옴

    return render_template('category_page.html', contests_data = contests_data) #공모전 정보들을 contests.html에 모두 넘겨줌(마무리는 웹에서 나열)
