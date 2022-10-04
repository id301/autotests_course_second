__author__ = 'id301'

from model.project import Project

def test_add_project(app):
    old_projects = app.project.get_projects_list()
    project = Project(name='Test project9', status='release', view_status='private',
                                    description='test descr', inherit_global_categories=True)
    app.project.add_project(project)
    new_projects = app.project.get_projects_list()
    old_projects.append(project)
    assert sorted(old_projects, key=Project.get_name) == sorted(new_projects, key=Project.get_name)
