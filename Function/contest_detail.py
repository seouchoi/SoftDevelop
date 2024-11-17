#선택된 공모전의 정보를 넘겨주는 코드
from flask import Blueprint, render_template, request
from DBHandler.Contest_DBhandler import Contest_DBHandler

contest_db_handler = Contest_DBHandler()

contest_detail_bp = Blueprint('contest_detail', __name__)

@contest_detail_bp.route('/contests/<contest_id>', methods = ["GET"]) #<contest_id>를 <contest_name>으로 사용할 수 있는 방법 생각해보기
def contest_detail(contest_id):
    contest_data = contest_db_handler.get_contest_by_id(contest_id)
    return render_template('contest_detail_page.html', contest_data = contest_data)
