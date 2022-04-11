import pytest
from selenium import webdriver
from lib_testbed.gui.gui_lib import GuiLib


@pytest.fixture(scope='session')
def browser(request):
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--disable-gpu')
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('window-size=1024,768')
    browser = webdriver.Chrome(options=chrome_options)
    browser.implicitly_wait(30)

    def close():
        try:
            browser.quit()
        except (ImportError, AttributeError):
            pass

    request.addfinalizer(close)
    return browser


@pytest.fixture(scope="class")
def driver(request, browser):
    request.cls.driver = GuiLib(browser)

@pytest.fixture(scope='session')
def a(request):
    return 1

@pytest.fixture(scope="class")
def b(request, a):
    request.cls.b = a