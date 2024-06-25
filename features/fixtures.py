import logging.config
import pathlib
import re

from behave import fixture

from features.common.webdriver import get_webdriver
from features.helpers.selenium_helpers import save_screenshot


@fixture
def save_screenshot_at_the_end_of_the_failed_tests(context, scenario_name):
    if hasattr(context, "webdriver"):
        FAILED_TESTS_FOLDER = "./reports/screenshots"
        pathlib.Path(FAILED_TESTS_FOLDER).mkdir(parents=True, exist_ok=True)
        image_name = re.sub(r"[^a-zA-Z]", "_", scenario_name).lower()
        file_name = f"./reports/screenshots/{image_name}.png"
        save_screenshot(context.webdriver, file_name)


@fixture
def config_log(context):
    LOGS_FOLDER = "./reports/logs"
    pathlib.Path(LOGS_FOLDER).mkdir(parents=True, exist_ok=True)
    logging.config.fileConfig("./logging.ini")


@fixture
def web_context(context, scenario):
    if "web" in scenario.effective_tags:
        context.webdriver = get_webdriver()
        yield context
        context.webdriver.quit()
    else:
        yield context
