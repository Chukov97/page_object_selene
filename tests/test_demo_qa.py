import allure
from demoqa_tests.pages.registation_page import RegistrationPage
from demoqa_tests.models.user import user
from demoqa_tests.models.constatn import SUBMISSION_MESSAGE


@allure.title("Successful fill form")
def test_form(browser_management):
    registration_page = RegistrationPage()
    with allure.step("Open registrations form"):
        registration_page.open_page()
    with allure.step("Fill form"):
        registration_page.enter_user_details(user)
    with allure.step('Submit form'):
        registration_page.assert_submission_message(SUBMISSION_MESSAGE)
    with allure.step("Check form results"):
        registration_page.assert_form_details(user)
    with allure.step('Close the form'):
        registration_page.close_modal()
