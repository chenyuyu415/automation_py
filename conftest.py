import pytest
from selenium import webdriver
from lib_testbed.gui.gui_lib import GuiLib

model = 'CODA-5519'


def pytest_addoption(parser):
    parser.addoption('--config', action='store', dest='config_name', help="Testbed config file name")
    parser.addoption('--browser', action='store', default='chrome', dest='browser_name',
                     help="The browser which you want to test")


@pytest.hookimpl(tryfirst=True)
def pytest_collection_modifyitems(items):
    new_items = []
    for item in items:
        for marker in item.iter_markers(name='model'):
            if model in marker.args:
                new_items.append(item)
    items[:] = new_items


def pytest_runtest_setup(item):
    for marker in item.iter_markers(name='topology'):
        if 'client1' not in marker.args:
            pytest.skip('skip')


@pytest.fixture(scope='session')
def config(request):
    return request.config.getoption("config_name")


@pytest.fixture(scope="class", autouse=True)
def config_name(request, config):
    request.cls.config_name = config


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
