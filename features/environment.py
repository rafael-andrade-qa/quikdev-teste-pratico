import logging as log

from behave import use_fixture
from behave.model_core import Status

from features.fixtures import config_log, save_screenshot_at_the_end_of_the_failed_tests, web_context


def before_all(context):
    use_fixture(config_log, context)


def before_scenario(context, scenario):
    use_fixture(web_context, context, scenario)
    log.info("========================================== Before Scenario ==========================================")
    log.info(f"Scenario: {scenario.name}")
    log.info("=====================================================================================================")


def after_scenario(context, scenario):
    log.info("========================================== After Scenario ==========================================")
    if scenario.status != Status.passed:
        use_fixture(save_screenshot_at_the_end_of_the_failed_tests, context, scenario.name)
    log.info("====================================================================================================\n")
