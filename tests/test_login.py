import time
from pytest import mark
from pages.login.login_page import LoginPage
from pages.dashboard.dashboard_page import DashboardPage


@mark.smoke
@mark.login
def test_login(browser, app_config, user_data):
    url = app_config.base_url
    login_page = LoginPage(driver=browser, base_url=url)
    login_page.go()
    login_page.client_id_field.input_text(user_data[0])
    login_page.username_field.input_text(user_data[1])
    login_page.password_field.input_text(user_data[2])
    login_page.login_button.click()
    dashboard_page = DashboardPage(driver=browser, base_url=url)
    my_workflow_text = dashboard_page.my_workflows.text
    assert my_workflow_text == 'My Workflows'
