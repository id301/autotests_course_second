__author__ = 'id301'

def test_signup_new_account(app):
    username = 'user112'
    password = 'test'
    app.james.ensure_user_exists(username, password)
