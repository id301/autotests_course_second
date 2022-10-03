__author__ = 'id301'

from model.project import Project

def test_add_project(app):
    app.session.login("administrator", "root") #Креды брать откуда-то возможно
    app.project.go_to_manage_project()
    app.project.add_project(Project(name='Test project2', status='release', view_status='private',
                                    description='test descr', inherit_global_categories=True)) #Добавить рандомизации (по аналогии с add из предыдущего проекта)