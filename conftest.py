import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions


def pytest_addoption(parser):
    parser.addoption('--browser_name', action='store', default='chrome', help="Choose browser: Chrome or Firefox")
    parser.addoption('--language', action='store', default='en', help='Choose language ru, en, fr, es ... etc')

def mybrowserlanguage(request):
    myvariableforlink = request.config.getoption("--language")
    print(myvariableforlink)
    return myvariableforlink

@pytest.fixture(scope="function")
def driver(request):
    browser_name = request.config.getoption("--browser_name")
    browser_language = request.config.getoption("--language")

    if browser_name == "chrome":
        print("\nstart chrome browser for test..")
        chrome_options = ChromeOptions()
        chrome_options.add_experimental_option('prefs', {'intl.accept_languages': browser_language})
        driver = webdriver.Chrome(options=chrome_options)
    elif browser_name == "firefox":
        print("\nstart firefox browser for test..")
        firefox_options = FirefoxOptions()
        firefox_options.set_preference("intl.accept_languages", browser_language)
        driver = webdriver.Firefox(options=firefox_options)
    else:
        raise pytest.UsageError("--browser_name should be chrome or firefox")
    yield driver
    print("\nquit browser..")
    driver.quit()




