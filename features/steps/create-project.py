from behave import given, when, then
from assertpy import assert_that, soft_assertions
from features.steps.constants import Constants
from features.steps.apirequests import ApiRequests


@when('I create a new project without modules')
def step_impl(context):
    context.project_request = ApiRequests.create_project_without_modules()


@then('I should see a successful creation code and I should be able to find the created project')
def step_impl(context):
    context.identifier = context.project_request.project.identifier
    with soft_assertions():
        assert context.project_request.status_code == Constants.StatusCode.CREATED.value
        project_request = ApiRequests.get_project_by_id(context.project_request.project.id)
        project = project_request.project
        assert_that(project).has_id(context.project_request.project.id)
        assert_that(project).has_name(context.project_request.project.name)
        assert_that(project).has_identifier(context.project_request.project.identifier)
        assert_that(project).has_description(context.project_request.project.description)
        assert_that(project).has_is_public(context.project_request.project.is_public)
        assert_that(project).has_home_page(context.project_request.project.home_page)
