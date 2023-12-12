from selene import browser, have, be
import os
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
    browser.element('//textarea[@id="currentAddress"]').should(be.blank).type('132, My Street, Bigtown BG23 4YZ')
    browser.element('//input[@id="react-select-3-input"]').type('NCR').press_enter()
    browser.element('//input[@id="react-select-4-input"]').type('Noida').press_enter()
    browser.element('//button[@id="submit"]').press_enter()

    browser.element('//div[@class="modal-header"]').should(have.text('Thanks for submitting the form'))
    browser.element('//table[@class="table table-dark table-striped table-bordered table-hover"]').should(have.text(
        'Ivan Ivanov' and
        'ivanov@gmail.com' and
        'Male' and
        '9100000001' and
        '01 August,1997' and
        'Commerce' and
        'Sports' and
        'picture.png' and
        '132, My Street, Bigtown BG23 4YZ' and
        'NCR Noida'
    ))
    browser.element('//button[@id="closeLargeModal"]').press_enter()
