from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class SomeFormPage(BasePage):
    # e.g. the ninth text input in that form
    NINTH_TEXT_INPUT = (By.XPATH, "(//form//input[@type='text'])[9]")     # ← your email_input example
    VERIFY_BUTTON    = (By.ID,   "btnVerify")  \
                      if you prefer ID locator                                   \
                      else (By.XPATH, "//button[normalize-space(text())='Verify']")  # ← your verify_btn example

    def fill_ninth_field(self, value: str):
        self.type(*self.NINTH_TEXT_INPUT, value)

    def click_verify(self):
        # if you defined VERIFY_BUTTON as a tuple you can just do:
        self.click(*self.VERIFY_BUTTON)
        # or inline:
        # self.click(By.XPATH, "//button[normalize-space(text())='Verify']")
        