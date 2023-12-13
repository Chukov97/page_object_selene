from demoqa_tests.pages.registation_page import RegistrationPage
from demoqa_tests.models.user import user
from demoqa_tests.models.constatn import SUBMISSION_MESSAGE


def test_form(browser_management):
    registration_page = RegistrationPage()
    registration_page.open_page()

    registration_page.enter_user_details(user)

    registration_page.assert_submission_message(SUBMISSION_MESSAGE)
    registration_page.assert_form_details(user)

    registration_page.close_modal()
