from flask import Flask
from flask_restx import Api
from login_seongyun import auth_namespace  # 로그인 관련 네임스페이스 import

app = Flask(__name__)
api = Api(app)

# 로그인 관련 네임스페이스를 전체 API에 등록
api.add_namespace(auth_namespace, '/auth')  

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=30000)
