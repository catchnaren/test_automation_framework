import json
from pytest import fixture
from config import Config
from selenium import webdriver

data_path = 'data\\test_data.json'


def load_user_data(path):
    with open(path) as data_file:
        data = json.load(data_file)
        return data


def pytest_addoption(parser):
    parser.addoption(
        "--env",
        action="store",
        help="Environment to run tests"
    )


@fixture(params=load_user_data(data_path))
def user_data(request):
    data = request.param
    return data


@fixture(scope="session")
def env(request):
    return request.config.getoption("--env")


@fixture(scope="session")
def app_config(env):
    cng = Config(env)
    return cng


@fixture(scope='session')
def chrome_browser():
    browser = webdriver.Chrome()
    # browser.maximize_window()
    yield browser
    print("TEAR_DOWN!!!!")


@fixture(params=[webdriver.Chrome, webdriver.Firefox])
def browser(request):
    driver = request.param
    drvr = driver()
    # drvr.maximize_window()
    yield drvr
    drvr.quit()
