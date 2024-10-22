from flask import Flask, request, jsonify, render_template

app = Flask(__name__)

@app.route('/')
def show_homepage():
    return render_template('logout_homepage.html')  # Render homepage

@app.route('/login')
def show_login_page():
    return render_template('login_page.html')

@app.route('/login/signup')
def show_register():
    return render_template('signup_page.html')

@app.route('/profile')
def show_profile():
    return render_template('profile.html')

@app.route('/question')
def show_question():
    return render_template('question_page.html')

if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)