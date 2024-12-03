from flask import request, jsonify, Blueprint
from DBHandler.member_DBHandler import member_DBHandler
from utils.login_required import login_required
from DBHandler.favorite_contest import FavoriteContests_DBHandler

member_db_handler = member_DBHandler()
favorite_db_handler = FavoriteContests_DBHandler()

favorite_bp = Blueprint('favorite', __name__)

@favorite_bp.route('/api/favorite', methods = ["POST"])
def favorite():
    data = request.get_json()
    print(data)
    favorite_db_handler.add_favorite_contest(data['key_id'], data['contest_id'])    
    return jsonify(data), 200