from flask import session, redirect, url_for, request
from functools import wraps

#로그인이 필요한 페이지인데, 그것을 판별할 때 사용하는 함수(여기저기서 사용됨)
def login_required(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        if 'key_id' not in session:
            session['next'] = request.path
            return redirect(url_for('login.show_login_page'))
        return func(*args, **kwargs)
    return wrapper