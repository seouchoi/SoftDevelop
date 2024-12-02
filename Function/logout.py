from flask import session, Blueprint, render_template, redirect, url_for

logout_bp = Blueprint('logout', __name__)

@logout_bp.route('/api/logout')
def logout():
    session.pop('key_id', None)  # 현재 접속중인 세션 삭제
    return redirect(url_for('homepage.homepage'))