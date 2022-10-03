__author__ = 'id301'

class Project:

    def __init__(self, name=None, status=None, view_status=None, description=None, inherit_global_categories=None):
        self.name = name
        self.status = status
        self.view_status = view_status
        self.description = description
        self.inherit_global_categories = inherit_global_categories
