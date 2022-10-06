__author__ = 'id301'

def test_login(app):
    app.session.login("administrator", "root") #for correct use comment login in conftest.py
    assert app.session.is_logged_in_as("administrator")