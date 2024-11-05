from flask import session, Blueprint, render_template

logout_bp = Blueprint('logout', __name__)

@logout_bp.route('/logout')
def logout():
    session.clear()  # 세션의 모든 데이터 삭제
    return render_template('logout_homepage.html')