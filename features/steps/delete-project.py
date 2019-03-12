from behave import given, when, then
from assertpy import assert_that, soft_assertions
from features.steps.constants import Constants
from features.steps.apirequests import ApiRequests


@given('a new project created')
def step_impl(context):
    context.project = ApiRequests.create_project_without_modules().project


@when('I delete this project')
def step_impl(context):
    context.request = ApiRequests.delete_project(context.project.id)


@then("I should see a successful delete code and I shouldn't be able to find the project")
def step_impl(context):
    with soft_assertions():
        assert context.request.status_code == Constants.StatusCode.OK.value
        project_request = ApiRequests.get_project_by_id(context.project.id)
        assert project_request.status_code == Constants.StatusCode.NOT_FOUND.value
