#contests 페이지에 공모전들 나열함
from flask import Blueprint, render_template, request
from DBHandler.contest_DBhandler import Contest_DBHandler
from DBHandler.category_DBhandler import Category_DBHandler
from urllib.parse import unquote

contest_db_handler = Contest_DBHandler()
category_db_handler = Category_DBHandler()

category_bp = Blueprint('category', __name__)

@category_bp.route('/category', methods = ["POST"])
def arrange_contests():
    category_name = request.form.get("category_name")
    category_data = category_db_handler.get_category_id_by_name(category_name)
    category_id = int(category_data['key_id'])

    contests_data = contest_db_handler.get_contest_by_category_id(category_id) #해당 카테고리 공모전 모두 가져옴)
    return render_template('category_page.html', contests_data = contests_data) #공모전 정보들을 contests.html에 모두 넘겨줌(마무리는 웹에서 나열)
