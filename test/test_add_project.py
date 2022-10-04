__author__ = 'id301'

from model.project import Project

def test_add_project(app):
    app.session.login("administrator", "root")
    app.project.add_project(Project(name='Test project3', status='release', view_status='private',
                                    description='test descr', inherit_global_categories=True))