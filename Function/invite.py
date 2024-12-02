from flask import Blueprint, request, jsonify

invite_bp = Blueprint('invite', __name__)

@invite_bp.route('/api/invite', methods=['POST'])
def invite():
    data = request.get_json()
    print(data)
    return jsonify(data), 200