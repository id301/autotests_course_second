__author__ = 'id301'

class Project:

    def __init__(self, name=None, status=None, view_status=None, description=None, inherit_global_categories=None, link=None):
        self.name = name
        self.status = status
        self.view_status = view_status
        self.description = description
        self.inherit_global_categories = inherit_global_categories
        self.link = link

    def __repr__(self):
        return f"{self.name};{self.status};{self.view_status};{self.description};{self.inherit_global_categories};" \
               f"{self.link}"

    def __eq__(self, other):
        return self.name == other.name and (self.link == other.link or self.link is None or other.link is None)

    def get_name(self):
        return self.name
