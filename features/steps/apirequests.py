from features.steps.constants import Constants
from faker import Faker
import requests
import json


class Request:
    def __init__(self, status_code):
        self.status_code = status_code


class ProjectRequest(Request):

    def __init__(self, project, status_code):
        super().__init__(status_code)
        self.project = project


class Project:

    def __init__(self, name, identifier, pid='', description='', home_page='', is_public=True):
        self.name = name
        self.id = pid
        self.identifier = identifier
        self.description = description
        self.home_page = home_page
        self.is_public = is_public


class ApiRequests:
    headers = {
        'X-Redmine-API-Key': Constants.API_KEY,
        'Content-Type': Constants.CONTENT_TYPE
    }

    @staticmethod
    def create_project(name, identifier, description='') -> ProjectRequest:

        body = {
            'project': {
                'name': name,
                'identifier': identifier,
                'description': description
            }
        }

        r = requests.post(Constants.BASE_URL + 'projects.json', data=json.dumps(body), headers=ApiRequests.headers)
        r_json = r.json()
        project = Project(name, identifier, description=description, id=r_json.get('project').get('id'))
        project_request = ProjectRequest(project, r.status_code)

        return project_request

    @staticmethod
    def create_project_without_modules() -> ProjectRequest:

        fake = Faker()
        project_name = fake.name()
        project_description = fake.text()
        project_identifier = project_name.replace(' ', '-').lower()

        body = {
            'project': {
                'name': project_name,
                'identifier': project_identifier,
                'description': project_description
            }
        }

        r = requests.post(Constants.BASE_URL + 'projects.json', data=json.dumps(body), headers=ApiRequests.headers)
        r_json = r.json()
        project = Project(project_name, project_identifier, description=project_description,
                          id=r_json.get('project').get('id'))
        project_request = ProjectRequest(project, r.status_code)

        return project_request

    @staticmethod
    def update_project_by_identifier(identifier, name='', description='') -> Request:

        body = {
            'project': {

            }
        }

        if name:
            body['project']['name'] = name
        if description:
            body['project']['description'] = description

        r = requests.put('{}projects/{}.json'.format(Constants.BASE_URL, identifier),
                         data=json.dumps(body),
                         headers=ApiRequests.headers)

        return Request(r.status_code)

    @staticmethod
    def get_project_by_id(project_id):

        r = requests.get('{}projects/{}.json'.format(Constants.BASE_URL, project_id))

        try:
            r_json = r.json()
        except json.decoder.JSONDecodeError:
            return Request(r.status_code)

        project_json = r_json.get('project')
        project = Project(project_json.get('name'), project_json.get('identifier'))
        project.description = project_json.get('description')
        project.id = project_json.get('id')
        project.home_page = project_json.get('homepage')
        project.is_public = project_json.get('is_public')
        project_request = ProjectRequest(project, r.status_code)

        return project_request

    @staticmethod
    def get_project_by_identifier(project_identifier):

        r = requests.get('{}projects/{}.json'.format(Constants.BASE_URL, project_identifier))

        try:
            r_json = r.json()
        except json.decoder.JSONDecodeError:
            return Request(r.status_code)

        project_json = r_json.get('project')
        project = Project(project_json.get('name'), project_json.get('identifier'))
        project.description = project_json.get('description')
        project.id = project_json.get('id')
        project.home_page = project_json.get('homepage')
        project.is_public = project_json.get('is_public')
        project_request = ProjectRequest(project, r.status_code)

        return project_request

    @staticmethod
    def delete_project(project_id) -> Request:
        r = requests.delete('{}projects/{}.json'.format(Constants.BASE_URL, project_id), headers=ApiRequests.headers)
        return Request(r.status_code)
