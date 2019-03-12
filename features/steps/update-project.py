from behave import given, when, then
from assertpy import assert_that, soft_assertions
from features.steps.constants import Constants
from features.steps.apirequests import ApiRequests


@given('a "{name}" Project with "{identifier}" identifier')
def step_impl(context, name, identifier):
    context.identifier = identifier
    context.new_project = ApiRequests.create_project(name, identifier)


@when('I modify the name to "{new_name}"')
def step_impl(context, new_name):
    context.new_name = new_name
    context.updated_project = ApiRequests.update_project_by_identifier(context.new_project.project.identifier, name=new_name)


@then('I should see a successful update code and the new name in the project')
def step_impl(context):

    project_request = ApiRequests.get_project_by_identifier(context.new_project.project.identifier)

    with soft_assertions():
        assert_that(project_request.status_code).is_equal_to(Constants.StatusCode.OK.value)
        assert_that(project_request.project).has_name(context.new_name)
