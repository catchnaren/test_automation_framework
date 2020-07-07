from faker import Faker
from pytest import mark
from pages.login.login_page import LoginPage
from pages.signup.signup_page import SignupPage
from pages.dashboard.dashboard_page import DashboardPage


@mark.smoke
@mark.signup
def test_signup(browser, app_config, user_data):
    url = app_config.base_url
    email = fake.company_email()
    login_page = LoginPage(driver=browser, base_url=url)
    login_page.go()
    login_page.signup_link.click()
    signup_page = SignupPage(driver=browser, base_url=url)
    signup_page.signup_email_field.input_text(email)
    signup_page.check_box.click()
    signup_page.start_free_trial_button.click_by_offset(0, 0)
    success_message = signup_page.success_message.text
    assert success_message == 'Success'
