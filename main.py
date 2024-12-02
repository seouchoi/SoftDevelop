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
    
if __name__ == "__main__":
    app.run(debug=True)