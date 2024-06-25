from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.firefox_profile import FirefoxProfile
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager

from features.common.constants import BROWSER, ENVIRONMENT, HEADLESS_MODE, SERVER


def get_webdriver():
    print("\n========================================= Webdriver Settings ==========================================")
    print(f"ENVIRONMENT: {ENVIRONMENT.upper()}")
    print(f"HEADLESS: {str(HEADLESS_MODE).upper()}")
    print(f"BROWSER: {BROWSER.upper()}")
    print(f"SERVER: {SERVER.upper()}")

    if BROWSER == "chrome":
        webdriver_path = ChromeDriverManager().install()
        print(f"WEBDRIVER PATH: {webdriver_path.upper()}")
        options = ChromeOptions()
        options.add_argument("--lang=pt-BR")
        options.add_experimental_option("prefs", {"enable_do_not_track": True})
        options.add_argument("--disable-usb-device-errors")
        webdriver_class = webdriver.Chrome

    else:
        webdriver_path = GeckoDriverManager().install()
        print(f"WEBDRIVER PATH: {webdriver_path.upper()}")
        profile = FirefoxProfile()
        profile.set_preference("intl.accept_languages", "pt-BR")
        profile.set_preference("privacy.trackingprotection.enabled", True)
        options = FirefoxOptions()
        options.profile = profile
        webdriver_class = webdriver.Firefox

    if HEADLESS_MODE:
        options.add_argument("--headless")

    if ENVIRONMENT == "Github Actions":
        webdriver_instance = webdriver_class(options=options)
        webdriver_instance.set_window_size(1920, 1080)
    else:
        webdriver_instance = webdriver_class(options=options)
        webdriver_instance.maximize_window()

    window_size = webdriver_instance.get_window_size()
    formatted_size = {"WIDTH": window_size["width"], "HEIGHT": window_size["height"]}
    print(f"SCREEN RESOLUTION: {formatted_size}")
    print("=======================================================================================================\n")

    return webdriver_instance
