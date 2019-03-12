import requests
from faker import Faker
import json
from features.steps.apirequests import ApiRequests


if __name__ == '__main__':

    base_url = 'http://192.168.64.2/'
    api_key = 'c278b5e3cca993d48a760aae98c8c81e108bb64f'
    content_type = 'application/json'

    headers = {
        'X-Redmine-API-Key': api_key,
        'Content-Type': content_type
    }
    #
    # # r = requests.get(base_url + 'projects.json')
    # # print(r.text)
    #
    # fake = Faker()
    # project_name: str = fake.name()
    # print(project_name)
    #
    # body = {
    #     'project': {
    #         'name': project_name,
    #         'identifier': project_name.replace(' ', '-').lower()
    #     }
    # }
    #
    # print(json.dumps(body))
    #
    # r = requests.post(base_url + 'projects.json', data=json.dumps(body), headers=headers)
    #
    # print(r.text)

    r = ApiRequests.get_project_by_id('564')
    print(r.status_code)
