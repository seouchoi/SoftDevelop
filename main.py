from flask import Flask, render_template, jsonify
from Function.signup import signup_bp  # 회원가입 블루프린트 불러오기
from Function.gpt import gpt_bp  # AI 메시지 블루프린트 불러오기
from Function.homepage import homepage_bp
from Function.login import login_bp
from Function.profil import profil_bp
from Function.logout import logout_bp
from Function.build_team import build_team_bp
from Function.contest_detail import contest_detail_bp
from Function.category import category_bp
from Function.invite import invite_bp
from Function.favorite import favorite_bp
from Function.invite_detail import invite_detail_bp 
from Function.accept_deny import accept_deny_bp
from Function.member_application import member_application_bp
from Function.application_detail import application_detail_bp
from Function.add_career import add_career_bp
import os

app = Flask(__name__,static_folder='front/static', template_folder='front/templates')
app.secret_key = os.urandom(24) #서버를 재시작할때마다 키를 바꿔서 세션을 삭제시킴.

app.register_blueprint(login_bp)
app.register_blueprint(signup_bp)
app.register_blueprint(gpt_bp)
app.register_blueprint(logout_bp)
app.register_blueprint(build_team_bp)
app.register_blueprint(contest_detail_bp)
app.register_blueprint(profil_bp)
app.register_blueprint(homepage_bp)
app.register_blueprint(category_bp)
app.register_blueprint(invite_bp)
app.register_blueprint(favorite_bp)
app.register_blueprint(invite_detail_bp)
app.register_blueprint(accept_deny_bp)
app.register_blueprint(member_application_bp)
app.register_blueprint(application_detail_bp)
app.register_blueprint(add_career_bp)


if __name__ == "__main__":
    app.run(debug=True)