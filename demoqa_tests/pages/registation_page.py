from selene import browser, have, be, by
from demoqa_tests.resource import path
from demoqa_tests.enums.gender import Gender
from demoqa_tests.enums.hobby import Hobby
from demoqa_tests.models.constatn import PRACTICE_FORM, OPEN_PAGE_URL


class RegistrationPage:

    def open_page(self):
        browser.open(OPEN_PAGE_URL)
        browser.element('//div[@class="main-header"]').should(have.text(PRACTICE_FORM))
        return self

    def enter_user_details(self, user):
        browser.element('//input[@id="firstName"]').should(be.blank).type(user.first_name)
        browser.element('//input[@id="lastName"]').should(be.blank).type(user.last_name)
        browser.element('//input[@id="userEmail"]').should(be.blank).type(user.email)

        gender_mapping = {
            Gender.MALE: '//input[@id="gender-radio-1"]',
            Gender.FEMALE: '//input[@id="gender-radio-2"]',
            Gender.OTHER: '//input[@id="gender-radio-3"]'
        }

        selected_gender = Gender(user.gender)
        browser.element(gender_mapping.get(selected_gender, gender_mapping[Gender.OTHER])).double_click()

        browser.element('//input[@id="userNumber"]').should(be.blank).type(user.phone_number)
        browser.element('//input[@id="dateOfBirthInput"]').click()
        browser.element('//select[@class="react-datepicker__month-select"]').click().element(
            by.text(user.month)).click()
        browser.element('//select[@class="react-datepicker__year-select"]').click().element(by.text(user.year)).click()
        browser.element(f'//div[@class="react-datepicker__day react-datepicker__day--0{user.day}"]').click()
        browser.element('//input[@id="subjectsInput"]').should(be.blank).type(user.subject).press_enter()

        hobby_mapping = {
            Hobby.SPORTS: '//label[@for="hobbies-checkbox-1"]',
            Hobby.READING: '//label[@for="hobbies-checkbox-2"]',
            Hobby.MUSIC: '//label[@for="hobbies-checkbox-3"]'
        }

        selected_hobby = Hobby(user.hobby)
        browser.element(hobby_mapping.get(selected_hobby)).double_click()

        browser.element('//input[@id="uploadPicture"]').send_keys(path(user.picture))
        browser.element('//textarea[@id="currentAddress"]').should(be.blank).type(user.address)
        browser.element('//input[@id="react-select-3-input"]').type(user.state).press_enter()
        browser.element('//input[@id="react-select-4-input"]').type(user.city).press_enter()
        browser.element('//button[@id="submit"]').press_enter()

        return self

    def assert_submission_message(self, message):
        browser.element('//div[@class="modal-header"]').should(have.text(message))
        return self

    def assert_form_details(self, user):
        browser.element('//table[@class="table table-dark table-striped table-bordered table-hover"]').should(have.text(
            f'{user.first_name} {user.last_name}' and
            user.email and
            user.gender and
            user.phone_number and
            f'{user.day} {user.month},{user.year}' and
            user.subject and
            user.hobby and
            user.picture and
            user.address and
            f'{user.state} {user.city}'
        ))
        return self

    def close_modal(self):
        browser.element('//button[@id="closeLargeModal"]').press_enter()
        return self
