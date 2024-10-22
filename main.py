from flask import Flask, render_template, jsonify
from signup import signup_bp  # 회원가입 블루프린트 불러오기
from gpt import gpt_bp  # AI 메시지 블루프린트 불러오기
from homepage import homepage_bp
from login import login_bp

app = Flask(__name__)
app.secret_key = '12345'

app.register_blueprint(login_bp, url_prefix = '/api')
app.register_blueprint(signup_bp, url_prefix = '/api')
app.register_blueprint(gpt_bp, url_prefix = '/api')
app.register_blueprint(homepage_bp)

    
if __name__ == "__main__":
    app.run(debug=True)