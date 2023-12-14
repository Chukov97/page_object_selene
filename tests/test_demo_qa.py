from demoqa_tests.pages.registation_page import RegistrationPage


def test_form(browser_management):
    registration_page = RegistrationPage()
    registration_page.open_page()

    registration_page.enter_first_name('Ivan')
    registration_page.enter_last_name('Ivanov')
    registration_page.enter_email('ivanov@gmail.com')
    registration_page.select_gender('Female')
    registration_page.enter_phone_number('9100000001')
    registration_page.select_date_of_birth('1997', 'August', '11')
    registration_page.enter_subject('Commerce')
    registration_page.select_hobby('Sports')
    registration_page.upload_picture('picture.png')
    registration_page.enter_address('132, My Street, Bigtown BG23 4YZ')
    registration_page.select_location('NCR', 'Noida')
    registration_page.submit_form()

    registration_page.assert_submission_message('Thanks for submitting the form')
    registration_page.assert_form_details('Ivan Ivanov',
                                          'ivanov@gmail.com',
                                          'Female',
                                          '9100000001',
                                          '11 August,1997',
                                          'Commerce',
                                          'Sports',
                                          'picture.png',
                                          '132, My Street, Bigtown BG23 4YZ',
                                          'NCR Noida')

    registration_page.close_modal()
    