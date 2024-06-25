from datetime import datetime

import parse
from behave import given, register_type, then, use_step_matcher, when
from common.constants import info

from features.steps.web.quikdev.quikdev_web_screen import QuikdevWebScreen


@parse.with_pattern(r".*")
def parse_optional_string(text):
    return text if text else None


register_type(OptionalString=parse_optional_string)
use_step_matcher("cfparse")


@given("I am on '{screen}'")
def step_i_am_on_screen(context, screen):
    quikdev_web_screen = QuikdevWebScreen(context.webdriver)
    quikdev_web_screen.access_the_screen(info[screen])


@when(
    "I fill in the fields '{product_name:OptionalString?}', '{price:OptionalString?}' and '{expiry_date:OptionalString?}'"
)
def step_fill_in_the_fields(context, product_name, price, expiry_date):
    quikdev_web_screen = QuikdevWebScreen(context.webdriver)
    quikdev_web_screen.fill_product_name_field(product_name)
    quikdev_web_screen.fill_price_field(price)
    quikdev_web_screen.fill_expiry_date_field(expiry_date)


@when("I try to add")
def step_i_try_to_add(context):
    quikdev_web_screen = QuikdevWebScreen(context.webdriver)
    quikdev_web_screen.click_add_button()


@then("the product should not be added")
def step_the_product_not_added(context):
    quikdev_web_screen = QuikdevWebScreen(context.webdriver)
    quikdev_web_screen.check_product_not_added()


@then(
    "the error message should be displayed in the fields '{product_name:OptionalString?}', '{price:OptionalString?}' and '{expiry_date:OptionalString?}'"
)
def step_the_error_message_should_be_displayed(context, product_name, price, expiry_date):
    quikdev_web_screen = QuikdevWebScreen(context.webdriver)

    if product_name is None or product_name.strip() == "":
        quikdev_web_screen.check_error_message_displayed_in_product_name_field()

    if price is None or price.strip() == "" or float(price) < 0:
        quikdev_web_screen.check_error_message_displayed_in_price_field()

    if expiry_date is None or expiry_date.strip() == "":
        quikdev_web_screen.check_error_message_displayed_in_expiry_date_field()
    else:
        expiry_date_format = datetime.strptime(expiry_date, "%d/%m/%Y")
        if expiry_date_format > datetime.strptime("31/12/2021", "%d/%m/%Y"):
            quikdev_web_screen.check_error_message_displayed_in_expiry_date_field()
