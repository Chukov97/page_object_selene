from selene import browser, have, be, by
from demoqa_tests.resource import path


class RegistrationPage:

    def open_page(self):
        browser.open('/automation-practice-form')
        browser.element('//div[@class="main-header"]').should(have.text('Practice Form'))
        return self

    def enter_first_name(self, first_name):
        browser.element('//input[@id="firstName"]').should(be.blank).type(first_name)
        return self

    def enter_last_name(self, last_name):
        browser.element('//input[@id="lastName"]').should(be.blank).type(last_name)
        return self

    def enter_email(self, email):
        browser.element('//input[@id="userEmail"]').should(be.blank).type(email)
        return self

    def select_gender(self, gender):
        if gender.lower() == 'male':
            browser.element('//input[@id="gender-radio-1"]').double_click()
        elif gender.lower() == 'female':
            browser.element('//input[@id="gender-radio-2"]').double_click()
        else:
            browser.element('//input[@id="gender-radio-3"]').double_click()
        return self

    def enter_phone_number(self, phone_number):
        browser.element('//input[@id="userNumber"]').should(be.blank).type(phone_number)
        return self

    def select_date_of_birth(self, year, month, day):
        browser.element('//input[@id="dateOfBirthInput"]').click()
        browser.element('//select[@class="react-datepicker__month-select"]').click().element(by.text(month)).click()
        browser.element('//select[@class="react-datepicker__year-select"]').click().element(by.text(year)).click()
        browser.element(f'//div[@class="react-datepicker__day react-datepicker__day--0{day}"]').click()
        return self

    def enter_subject(self, subject):
        browser.element('//input[@id="subjectsInput"]').should(be.blank).type(subject).press_enter()
        return self

    def select_hobby(self, hobby):
        if hobby.lower() == "sports":
            browser.element('//label[@for="hobbies-checkbox-1"]').click()
        if hobby.lower() == "reading":
            browser.element('//label[@for="hobbies-checkbox-2"]').click()
        if hobby.lower() == "music":
            browser.element('//label[@for="hobbies-checkbox-3"]').click()
        return self

    def upload_picture(self, picture):
        browser.element('//input[@id="uploadPicture"]').send_keys(path(picture))
        return self
