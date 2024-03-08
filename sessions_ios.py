from appium import webdriver
from os import path
from appium.options.common import AppiumOptions

# CUR_DIR = path.dirname(path.abspath(__file__))
# APP = path.join(CUR_DIR, 'TheApp.app.zip')
APP = "https://github.com/appium-pro/TheApp/releases/download/v1.12.0/TheApp.app.zip"
APPIUM = "http://localhost:4723"

CAPS = {
    "platformName": "iOS",
    "appium:options": {
        "platformVersion": "17.4",
        "deviceName": "iPhone 15 Pro Max",
        "automationName": "XCUITest",
        "app": APP,
        "showXcodeLog": True
    }
}

OPTIONS = AppiumOptions().load_capabilities(CAPS)

driver = webdriver.Remote(
    command_executor=APPIUM,
    options=OPTIONS
)
driver.quit()
