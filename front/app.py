from flask import Flask, request, jsonify, render_template

app = Flask(__name__)

@app.route('/')
def homepage():
    return render_template('logout_homepage.html')  # 홈페이지를 렌더링

@app.route('/login', methods=['GET'])
def login_page():
    return render_template('login_page.html')  # 로그인 페이지를 렌더링

@app.route('/api/login', methods=['POST'])
def login():
    data = request.json  # JSON 형식으로 받은 데이터 처리
    user_id = data.get('id')
    password = data.get('password')

    # 로그인 정보를 수신한 후, 콘솔에 출력합니다.
    print(f"Received ID: {user_id}, Password: {password}")

    # 성공적으로 데이터를 받았음을 응답
    return jsonify({"message": "로그인 정보가 수신되었습니다."}), 200

@app.route('/login/register')
def register():
    return render_template('register_page.html')

@app.route('/profile')
def profile():
    return render_template('profile.html')

@app.route('/question')
def profile():
    return render_template('question_page.html')

if __name__ == '__main__':
    app.run('0.0.0.0', port=80, debug=True)
