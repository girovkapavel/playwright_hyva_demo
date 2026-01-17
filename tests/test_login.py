from playwright.sync_api import expect


EMAIL = "test1214@gmail.com"
PASSWORD = "1234aqeFs"

FIRSTNAME_INPUT = "test"
LASTNAME_INPUT = "order"
    
PASSWORD_CONFIRM_INPUT = "1234aqeFs"
    
def test_authorization(login):
    login.login(EMAIL, PASSWORD)
    
def test_forgot_password(login):
    login.forgot_password()

def test_register_account(login):
    login.register_account(EMAIL, PASSWORD, FIRSTNAME_INPUT, LASTNAME_INPUT)   
    