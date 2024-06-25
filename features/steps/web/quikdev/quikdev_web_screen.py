from features.common.element_locators import SELECTORS
from features.helpers.selenium_helpers import (
    assert_element_displayed_xpath,
    assert_no_elements_in_list_xpath,
    click_element_xpath,
    navigate_to_url,
    send_keys_xpath,
)


class QuikdevWebScreen:
    def __init__(self, webdriver):
        self.webdriver = webdriver
        self.name_input_selector = SELECTORS["form"]["name_input"]
        self.price_input_selector = SELECTORS["form"]["price_input"]
        self.expiry_date_input_selector = SELECTORS["form"]["expiry_date_input"]
        self.add_button_selector = SELECTORS["form"]["add_button"]
        self.table_row_selector = SELECTORS["table"]["row"]
        self.error_message_name_invalid_selector = SELECTORS["error_message"]["name_invalid_feedback_label"]
        self.error_message_price_invalid_selector = SELECTORS["error_message"]["price_invalid_feedback_label"]
        self.error_message_expiry_date_invalid_selector = SELECTORS["error_message"][
            "expiry_date_invalid_feedback_label"
        ]

    def access_the_screen(self, url):
        navigate_to_url(self.webdriver, url)

    def fill_product_name_field(self, product_name):
        send_keys_xpath(self.webdriver, self.name_input_selector, product_name)

    def fill_price_field(self, price):
        send_keys_xpath(self.webdriver, self.price_input_selector, price)

    def fill_expiry_date_field(self, expiry_date):
        send_keys_xpath(self.webdriver, self.expiry_date_input_selector, expiry_date)

    def click_add_button(self):
        click_element_xpath(self.webdriver, self.add_button_selector)

    def check_product_not_added(self):
        assert_no_elements_in_list_xpath(self.webdriver, self.table_row_selector)

    def check_error_message_displayed_in_product_name_field(self):
        assert_element_displayed_xpath(self.webdriver, self.error_message_name_invalid_selector)

    def check_error_message_displayed_in_price_field(self):
        assert_element_displayed_xpath(self.webdriver, self.error_message_price_invalid_selector)

    def check_error_message_displayed_in_expiry_date_field(self):
        assert_element_displayed_xpath(self.webdriver, self.error_message_expiry_date_invalid_selector)
