from flask import Flask, request, jsonify, render_template
import requests

app = Flask(__name__)

# Server URLs
login_url = "http://localhost:30000/auth"
signup_url = "http://localhost:30000/auth/signup"

@app.route('/')
def show_homepage():
    return render_template('logout_homepage.html')  # Render homepage

@app.route('/login', methods=['GET'])
def show_login_page():
    return render_template('login_page.html')

@app.route('/login', methods=['POST'])
def login():
    user_id = request.form['id']
    password = request.form['password']

    # Send login data to server
    response = requests.post(signup_url, json={'id': user_id, 'password': password})

    if response.status_code == 200:
        return jsonify({"message": "로그인 성공", "user_id": user_id}), 200
    else:
        return jsonify({"message": "로그인 실패: " + response.json().get('message')}), response.status_code

@app.route('/login/signup', methods=['GET'])
def show_register():
    return render_template('register_page.html')

@app.route('/login/signup', methods=['POST'])
def register():
    # Retrieve form data from the HTML
    user_data = {
        'user_id': request.json['user_id'],
        'password': request.json['password'],
        'name': request.json['name'],
        'phone': request.json['phone'],
        'email': request.json['email'],
        'region': request.json['region'],
        'category': request.json['category'],
        'task': request.json['task']
    }

    # Send registration data to server
    response = requests.post(signup_url, json=user_data)

    if response.status_code == 200:
        return jsonify({"message": "가입 성공"}), 200
    else:
        return jsonify({"message": "가입 실패: " + response.json().get('message')}), response.status_code

@app.route('/profile')
def show_profile():
    return render_template('profile.html')

@app.route('/question')
def show_question():
    return render_template('question_page.html')

if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)