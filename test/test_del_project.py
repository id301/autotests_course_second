__author__ = 'id301'

from model.project import Project
import random

def test_del_project(app):
    app.session.login("administrator", "root")
    #chose project
    projects = app.project.get_projects_list()
    if len(projects) == 0:
        project = Project(name='Test project', status='release', view_status='private',
                                    description='test descr', inherit_global_categories=True)
        app.project.add_project(project)
        projects.append(app.project.get_projects_list())
    project = random.choice(projects)
    #del project
    app.project.del_project(project)