import unittest
import pytest
from utils.helpers import init_driver, take_screenshot
from pages.login_page import LoginPage
from utils.logger import logger
from config.settings import USERNAME, PASSWORD, TEST_USERNAME, TEST_PASSWORD
from selenium import webdriver
from run import create_driver

@pytest.fixture
def driver():
    driver = create_driver(headless=False)
    yield driver
    driver.quit()

class TestLogin(unittest.TestCase):
    
    def setUp(self):
        logger.info("Setting up test")
        self.driver = init_driver()
        self.login_page = LoginPage(self.driver)
    
    def tearDown(self):
        logger.info("Tearing down test")
        if self.driver:
            # Take screenshot if test fails
            if hasattr(self, '_outcome') and not self._outcome.success:
                take_screenshot(self.driver, self._testMethodName)
            self.driver.quit()
    
    def test_valid_login(self):
        """Test logging in with valid credentials"""
        logger.info("Running test_valid_login")
        self.login_page.open()
        self.login_page.login()
        self.assertTrue(self.login_page.is_logged_in(), "Failed to login with valid credentials")
        self.login_page.login(TEST_USERNAME, TEST_PASSWORD)
    
    def test_invalid_login(self):
        """Test logging in with invalid credentials"""
        logger.info("Running test_invalid_login")
        self.login_page.open()
        self.login_page.login("invalid_user", "invalid_password")
        self.assertFalse(self.login_page.is_logged_in(), "Logged in with invalid credentials")
        error_message = self.login_page.get_error_message()
        self.assertIsNotNone(error_message, "No error message displayed for invalid login")

def test_successful_login(driver):
    page = LoginPage(driver)
    page.open()
    page.login()
    assert "Dashboard" in driver.title
