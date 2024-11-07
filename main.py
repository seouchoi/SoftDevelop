from flask import Flask, render_template, jsonify
from signup import signup_bp  # 회원가입 블루프린트 불러오기
from gpt import gpt_bp  # AI 메시지 블루프린트 불러오기
from homepage import homepage_bp
from login import login_bp
from profil import profil_bp
from logout import logout_bp
#from build_team import build_team_bp 
import os

app = Flask(__name__, template_folder='front/templates')
app.secret_key = os.urandom(24) #서버를 재시작할때마다 키를 바꿔서 세션을 삭제시킴.

app.register_blueprint(login_bp, url_prefix = '/api')
app.register_blueprint(signup_bp, url_prefix = '/api')
app.register_blueprint(gpt_bp, url_prefix = '/api')
app.register_blueprint(logout_bp, url_prefix = '/api')
#app.register_blueprint(build_team_bp, url_prefix = '/api')
app.register_blueprint(profil_bp)
app.register_blueprint(homepage_bp)

    
if __name__ == "__main__":
    app.run(debug=True)