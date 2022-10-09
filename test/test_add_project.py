__author__ = 'id301'

from model.project import Project
from generators.simple_generator import testdata

def test_add_project(app):
    old_projects = app.soap.get_projects_list()
    old_projects = app.project.convert_ProjectData_list_to_Project_list(old_projects)
    project = testdata
    app.project.add_project(project)
    new_projects = app.soap.get_projects_list()
    new_projects = app.project.convert_ProjectData_list_to_Project_list(new_projects)
    old_projects.append(project)
    assert sorted(old_projects, key=Project.get_name) == sorted(new_projects, key=Project.get_name)
