from behave import fixture, use_fixture
from behave.model_core import Status
from features.steps.apirequests import ApiRequests


def before_scenario(context, scenario):
    pass


def after_step(context, step):
    pass


def after_scenario(context, scenario):
    if 'delete.new.project' in scenario.tags:
        ApiRequests.delete_project(context.identifier)

