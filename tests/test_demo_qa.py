from selene import browser, have, be
import os


def test_form(browser_management):
    browser.open('/automation-practice-form')
    browser.element('//div[@class="main-header"]').should(have.text('Practice Form'))
    browser.element('//input[@id="firstName"]').should(be.blank).type('Ivan')
    browser.element('//input[@id="lastName"]').should(be.blank).type('Ivanov')
    browser.element('//input[@id="userEmail"]').should(be.blank).type('ivanov@gmail.com')
    browser.element('//input[@id="gender-radio-1"]').double_click()
    browser.element('//input[@id="userNumber"]').should(be.blank).type('9100000001')
    browser.element('//input[@id="dateOfBirthInput"]').click()
    browser.element('//select[@class="react-datepicker__month-select"]').click().element('//option[@value="7"]').click()
    browser.element('//select[@class="react-datepicker__year-select"]').click().element(
        '//option[@value="1997"]').click()
    browser.element('//div[@class="react-datepicker__day react-datepicker__day--001"]').click()
    browser.element('//input[@id="subjectsInput"]').should(be.blank).type('Commerce').press_enter()
    browser.element('//label[@for="hobbies-checkbox-1"]').click()
    browser.element('//input[@id="uploadPicture"]').send_keys(os.path.abspath('pict/ciwlCWa.png'))
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
        'ciwlCWa.png' and
        '132, My Street, Bigtown BG23 4YZ' and
        'NCR Noida'
    ))
    browser.element('//button[@id="closeLargeModal"]').press_enter()
