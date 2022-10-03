__author__ = 'id301'

from model.project import Project
import random

def test_del_project(app):
    app.session.login("administrator", "root")
    app.project.go_to_manage_project()
    #chose project
    projects = app.project.get_projects_list()
    project_link = random.choice(projects)
    #del project
    app.project.del_project_by_link(project_link)