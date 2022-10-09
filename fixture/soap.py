__author__ = 'id301'

from suds.client import Client
from suds import WebFault

class SoapHelper:

    def __init__(self, app):
        self.app = app

    def can_login(self, username, password):
        client = Client(self.app.config['web']['baseUrl'] + "api/soap/mantisconnect.php?wsdl")
        try:
            client.service.mc_login(username, password)
            return True
        except WebFault:
            return False

    def get_projects_list(self):
        client = Client(self.app.config['web']['baseUrl'] + "api/soap/mantisconnect.php?wsdl")
        try:
            lst = client.service.mc_projects_get_user_accessible(self.app.config['webadmin']['username'], self.app.config['webadmin']['password'])
            return lst
        except WebFault:
            print("Error occured")
            return None