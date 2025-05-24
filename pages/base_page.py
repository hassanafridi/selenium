from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from utils.helpers import wait_for, take_screenshot
from config.settings import EXPLICIT_WAIT
from utils.logger import logger

class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def visit(self, url):
        logger.info(f"Navigating to {url}")
        self.driver.get(url)
        print("👉 Opening:", url)

    def find(self, by, locator):
        logger.debug(f"Waiting for element: {locator}")
        try:
            return wait_for(self.driver, by, locator, EXPLICIT_WAIT)
        except TimeoutException:
            path = take_screenshot(self.driver, f"timeout_{locator}")
            logger.error(f"Element {locator!r} not found at URL {self.driver.current_url}. Saved screenshot ➜ {path}")
            # also dump HTML for quick inspection
            with open("page_source.html", "w", encoding="utf-8") as f:
                f.write(self.driver.page_source)
            raise

    def click(self, by, locator):
        elem = self.find(by, locator)
        elem.click()

    def type(self, by, locator, text):
        elem = self.find(by, locator)
        elem.clear()
        elem.send_keys(text)
