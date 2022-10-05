__author__ = 'id301'

from model.project import Project
import time

class ProjectHelper:

    def __init__(self, app):
        self.app = app

    def go_to_manage_project(self):
        wd = self.app.wd
        wd.find_element_by_link_text('Manage').click()
        wd.find_element_by_link_text('Manage Projects').click()

    def add_project(self, project):
        wd = self.app.wd
        self.go_to_manage_project()
        wd.find_element_by_xpath('//input[@value="Create New Project"]').click()
        #fill project name and decription
        self.change_field_value("name", project.name)
        self.change_field_value("description", project.description)
        #fill checkbox if needed
        if not project.inherit_global_categories:
            wd.find_element_by_name("inherit_global").click()
        #chose list`s values
        wd.find_element_by_xpath("//select[@name='status']/option[text() = '%s']" % project.status).click()
        wd.find_element_by_xpath("//select[@name='view_state']/option[text() = '%s']" % project.view_status).click()
        wd.find_element_by_css_selector('input.button').click()
        return

    def change_field_value(self, field_name, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element_by_name(field_name).click()
            wd.find_element_by_name(field_name).clear()
            wd.find_element_by_name(field_name).send_keys(text)

    def get_projects_link_list(self):
        wd = self.app.wd
        self.go_to_manage_project()
        list = []
        for a in wd.find_elements_by_xpath("//a[@href]"):
            link = a.get_attribute('href')
            if link.count('manage_proj_edit_page') != 0:
                list.append(link)
        return(list)

    def get_projects_list(self):
        wd = self.app.wd
        lst = []
        for link in self.get_projects_link_list():
            wd.get(link)
            name = wd.find_element_by_name('name').get_attribute("value")
            status = wd.find_element_by_xpath('//select[@name="status"]/option[@selected="selected"]').text
            view_status = wd.find_element_by_xpath('//select[@name="view_state"]/option[@selected="selected"]').text
            description = wd.find_element_by_name('description').text
            inherit_global_categories = True if wd.find_element_by_name('inherit_global').get_attribute("checked") == 'true' else False
            lst.append(Project(name=name, status=status, view_status=view_status,
                                    description=description, inherit_global_categories=inherit_global_categories, link=link))
        self.go_to_manage_project()
        return lst

    def del_project(self, project):
        wd = self.app.wd
        wd.get(project.link)
        wd.find_element_by_xpath('//input[@value="Delete Project"]').click()
        wd.find_element_by_xpath('//input[@value="Delete Project"]').click()
