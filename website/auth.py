from flask import Blueprint

auth = Blueprint('auth', __name__)


@auth.route('/login')
def login():
     return "<p>Sayfaya giriş yapın</p>"

@auth.route('logout')
def logout():
    return '<p>Sayfadan çıkış yapın</p>'

@auth.route('/sign-up')
def signup():
    return '<p>Kullanıcı kaydı oluştur</p>'