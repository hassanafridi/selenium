from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from config.settings import LOGIN_URL, USERNAME, PASSWORD, TEST_USERNAME, TEST_PASSWORD

class LoginPage(BasePage):
    # Locators
    URL             = LOGIN_URL
    USER_FIELD      = (By.ID,      "username")
    PASS_FIELD      = (By.XPATH,   "//input[@type='password']")                                # ← your password_input example
    SUBMIT_BUTTON   = (By.XPATH,   "//button[normalize-space(text())='Submit']") 
    ERROR_MESSAGE = (By.CSS_SELECTOR, ".error-message")
    
    def __init__(self, driver):
        super().__init__(driver)
    
    def open(self):
        self.visit(self.URL)
    
    def login(self, username: str = None, password: str = None):
        username = username or TEST_USERNAME
        password = password or TEST_PASSWORD
        self.type(*self.USER_FIELD, username)
        self.type(*self.PASS_FIELD, password)
        self.click(*self.SUBMIT_BUTTON)

    
    def get_error_message(self):
        """Get error message if present, otherwise return None"""
        try:
            elem = self.find(*self.ERROR_MESSAGE)
            return elem.text
        except:
            return None
    
    def is_logged_in(self):
        # This method should be customized based on how you determine 
        # whether a user is logged in on your application
        # For example, checking for a dashboard element:
        dashboard_element = (By.ID, "dashboard")
        return self.is_element_visible(dashboard_element)
