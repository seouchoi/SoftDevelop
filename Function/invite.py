from flask import Blueprint, request, jsonify
from DBHandler.invite_DBHandler import invite_DBHandler

invite_db_handler = invite_DBHandler()

invite_bp = Blueprint('invite', __name__)

@invite_bp.route('/api/invite', methods=['POST'])
def invite():
    data = request.get_json()
    invite_db_handler.insert_invite(data['sender_id'], int(data['team_id']) , data['receiver_id'], data['message'], data['contest_id'])
    return jsonify(data), 200