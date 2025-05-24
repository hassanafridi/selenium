import unittest
import sys
import os
from utils.logger import logger
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from pages.login_page import LoginPage
from config.settings import IMPLICIT_WAIT

def run_tests():
    """Discover and run all tests"""
    try:
        # Get the directory of this script
        script_dir = os.path.dirname(os.path.abspath(__file__))
        
        # Add the script directory to the Python path
        sys.path.insert(0, script_dir)
        
        # Discover tests in the tests directory
        test_dir = os.path.join(script_dir, 'tests')
        test_suite = unittest.defaultTestLoader.discover(test_dir, pattern='test_*.py')
        
        # Run the tests
        logger.info("Starting test run")
        runner = unittest.TextTestRunner(verbosity=2)
        result = runner.run(test_suite)
        
        # Return exit code based on test results
        return 0 if result.wasSuccessful() else 1
    
    except Exception as e:
        logger.error(f"Error running tests: {str(e)}")
        return 1

def create_driver(headless=True):
    options = Options()
    if headless:
        options.add_argument("--headless")
    options.add_argument("--disable-gpu")
    # Updated WebDriver initialization to use the service parameter
    driver = webdriver.Chrome(options=options)
    driver.implicitly_wait(IMPLICIT_WAIT)
    return driver

def main():
    driver = create_driver(headless=False)  # set to True for RPA jobs
    try:
        login_page = LoginPage(driver)
        login_page.open()
        login_page.login()
        logger.info("Login successful!")
        # TODO: chain additional page objects / flows here
    except Exception as e:
        logger.exception("Error during RPA flow")
    finally:
        driver.quit()

if __name__ == "__main__":
    sys.exit(run_tests())
