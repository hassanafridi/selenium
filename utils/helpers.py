import os
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.edge.options import Options as EdgeOptions
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from config.settings import BROWSER, HEADLESS, IMPLICIT_WAIT, SCREENSHOT_DIR
from utils.logger import logger

def init_driver():
    """Initialize and return WebDriver instance based on settings"""
    driver = None
    
    try:
        if BROWSER.lower() == 'chrome':
            options = ChromeOptions()
            if HEADLESS:
                options.add_argument('--headless')
            options.add_argument('--start-maximized')
            driver = webdriver.Chrome(options=options)
            
        elif BROWSER.lower() == 'firefox':
            options = FirefoxOptions()
            if HEADLESS:
                options.add_argument('--headless')
            driver = webdriver.Firefox(options=options)
            
        elif BROWSER.lower() == 'edge':
            options = EdgeOptions()
            if HEADLESS:
                options.add_argument('--headless')
            driver = webdriver.Edge(options=options)
            
        else:
            raise ValueError(f"Unsupported browser: {BROWSER}")
        
        driver.implicitly_wait(IMPLICIT_WAIT)
        logger.info(f"Initialized {BROWSER} browser")
        return driver
    
    except Exception as e:
        logger.error(f"Failed to initialize driver: {str(e)}")
        if driver:
            driver.quit()
        raise

def wait_for(driver, by, locator, timeout):
    """Wait for an element to be present on the page"""
    return WebDriverWait(driver, timeout).until(
        EC.presence_of_element_located((by, locator))
    )

def take_screenshot(driver, test_name):
    """Take a screenshot and save it to the screenshots directory"""
    try:
        os.makedirs(SCREENSHOT_DIR, exist_ok=True)
        timestamp = time.strftime("%Y%m%d-%H%M%S")
        filename = f"{SCREENSHOT_DIR}/{test_name}_{timestamp}.png"
        driver.save_screenshot(filename)
        logger.info(f"Screenshot saved to {filename}")
        return filename
    except Exception as e:
        logger.error(f"Failed to take screenshot: {str(e)}")
        return None
