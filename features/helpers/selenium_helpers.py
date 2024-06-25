import logging as log
import time

from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


def navigate_to_url(webdriver, url, wait_time=10):
    """Navigate to the specified URL and set a timeout for page load"""
    try:
        webdriver.set_page_load_timeout(wait_time)
        webdriver.get(url)
        log.info(f"Successfully navigated to URL: {url}")
    except TimeoutException as e:
        log.error(f"Timeout while navigating to URL: {url}")
        raise e


def wait_element_xpath(webdriver, selector, wait_time=10):
    """Wait for an element to be visible and return it."""
    try:
        wait = WebDriverWait(webdriver, wait_time)
        element = wait.until(EC.visibility_of_element_located((By.XPATH, selector)))
        log.info(f"Element with selector '{selector}' found and visible.")
        return element
    except TimeoutException:
        log.error(f"Element with selector '{selector}' was not found or not visible.")
        return None


def click_element_xpath(webdriver, selector, wait_time=10):
    """Wait for an element to be clickable and click on it."""
    try:
        wait = WebDriverWait(webdriver, wait_time)
        element = wait.until(EC.visibility_of_element_located((By.XPATH, selector)))
        time.sleep(1)
        element.click()
        log.info(f"Clicked element with selector '{selector}'.")
    except TimeoutException as e:
        log.error(f"Element with selector '{selector}' was not clickable.")
        raise e


def send_keys_xpath(webdriver, selector, keys, wait_time=10):
    """Wait for an element to be visible and send keys to it."""
    try:
        wait = WebDriverWait(webdriver, wait_time)
        element = wait.until(EC.visibility_of_element_located((By.XPATH, selector)))
        if keys is not None:
            element.send_keys(keys)
        log.info(f"Sent keys '{keys}' to element with selector '{selector}'.")
    except TimeoutException as e:
        log.error(f"Element with selector '{selector}' was not found or not visible.")
        raise e


def assert_element_displayed_xpath(webdriver, selector, wait_time=10):
    """Verifies if the element is displayed on the page."""
    try:
        wait = WebDriverWait(webdriver, wait_time)
        element = wait.until(EC.visibility_of_element_located((By.XPATH, selector)))
        assert element.is_displayed(), f"Element with selector '{selector}' is not displayed."
        log.info(f"Element with selector '{selector}' is displayed.")
    except (TimeoutException, AssertionError) as e:
        log.error(f"Element with selector '{selector}' is not displayed.")
        raise e


def assert_no_elements_in_list_xpath(webdriver, selector_list):
    """Asserts that no elements exist in the list identified by selector_list."""
    try:
        elements = webdriver.find_elements(By.XPATH, selector_list)
        if len(elements) == 0:
            log.info(f"No elements found with selector: '{selector_list}'")
        else:
            log.warning(f"Found {len(elements)} element(s) with selector: '{selector_list}'")
            assert False, f"Elements were found with the selector: '{selector_list}'"
    except AssertionError as ae:
        raise ae
    except Exception as e:
        log.error(f"Error asserting absence of elements in list: {e}")
        raise e


def save_screenshot(webdriver, file_name):
    """Save a screenshot using the WebDriver instance."""
    try:
        webdriver.save_screenshot(file_name)
        log.info(f"Screenshot saved as {file_name}")
    except Exception as e:
        log.error(f"Error saving screenshot: {e}")
        raise e
