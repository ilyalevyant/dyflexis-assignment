import json

from page_objects import PageObject, PageElement

class StartPage(PageObject):

    __name_input_submit_message: PageElement = PageElement(xpath="//*[@*='name']")
    __email_input_submit_message: PageElement = PageElement(xpath="//*[@*='email']")
    __phone_input_submit_message: PageElement = PageElement(xpath="//*[@*='phone']")
    __subject_input_submit_message: PageElement = PageElement(xpath="//*[@*='subject']")
    __message_input_submit_message: PageElement = PageElement(xpath="//*[@*='description']")
    __submit_btn: PageElement = PageElement(xpath="//*[@*='submitContact']")
    __confirm_submit_msg: PageElement = PageElement(xpath="//*[contains(text(),'Thanks for getting in touch')]")
    __default_confirmation_message = 'Thanks for getting in touch '

    def submit_message(self, name: str = 'test name', email: str = 'test@email.com', phone: str = '123456789123',
                       subject: str = 'Test subject', message: str = 'Default test message'):
        self.__name_input_submit_message.click()
        self.__name_input_submit_message.send_keys(name)
        self.__email_input_submit_message.click()
        self.__email_input_submit_message.send_keys(email)
        self.__phone_input_submit_message.click()
        self.__phone_input_submit_message.send_keys(phone)
        self.__subject_input_submit_message.click()
        self.__subject_input_submit_message.send_keys(subject)
        self.__message_input_submit_message.click()
        self.__message_input_submit_message.send_keys(message)
        self.__submit_btn.click()

    def validate_message_submit(self, name: str = 'test name', email: str = 'test@email.com', phone: str = '123456789123',
                       subject: str = 'Test subject', message: str = 'Default test message'):
        self.validate_ui(name)
        self.validate_network(name, email, phone, subject, message)

    def validate_ui(self, name: str):
        confirmation_message = self.w.find_element_by_xpath("//div[@*='row contact']/div/div/h2").text
        assert confirmation_message == f'{self.__default_confirmation_message}{name}!'

    def validate_network(self, name, email, phone, subject, message):
        request = self.w.wait_for_request(".*/message")
        assert request, 'Request for message submit was not sent'
        assert request.method == 'POST', 'Request for message submit was not POST'
        actual_request_body = json.loads(request.body)
        assert actual_request_body == {'name': name, 'email': email, 'phone': phone, 'subject': subject, 'description': message}, \
            'Request body for message submit is not as expected'
