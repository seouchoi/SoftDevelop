from flask import session, Blueprint, render_template

logout_bp = Blueprint('logout', __name__)

@logout_bp.route('/api/logout')
def logout():
    session.pop('key_id', None)  # 현재 접속중인 세션 삭제
    return render_template('logout_homepage.html')