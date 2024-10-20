
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def homepage():
  return render_template('logout_homepage.html')

@app.route('/login')
def login():
  return render_template('login_page.html')

@app.route('/login/register')
def register():
  return render_template('register_page.html')

@app.route('/profile')
def profile():
  return render_template('profile.html')

if __name__ == '__main__':
  app.run('0.0.0.0',port=80,debug=True)