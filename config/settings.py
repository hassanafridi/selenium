# Configuration settings for Selenium tests

# Browser settings
BROWSER = "chrome"  # Options: chrome, firefox, edge
HEADLESS = False

# Application settings
BASE_URL = "https://appointment.thespainvisa.com/Global/account"
LOGIN_URL = f"{BASE_URL}/login"

# Authentication credentials
USERNAME = "sarwat110exp@gmail.com"
PASSWORD = "Life@1122"

# Timeouts (in seconds)
IMPLICIT_WAIT = 10
EXPLICIT_WAIT = 20

# Screenshot settings
SCREENSHOT_DIR = "screenshots"
TAKE_SCREENSHOT_ON_FAILURE = True
