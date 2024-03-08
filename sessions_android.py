from appium import webdriver
# from os import path
from appium.options.common import AppiumOptions

# CUR_DIR = path.dirname(path.abspath(__file__))
# APP = path.join(CUR_DIR, 'TheApp-v1.10.0.apk')
APP = "https://github.com/appium-pro/TheApp/releases/download/v1.12.0/TheApp.apk"
APPIUM = "http://localhost:4723"

CAPS = {
    "platformName": "Android",
    "appium:options": {
        "platformVersion": "14.0",  # optional
        "deviceName": "Android Emulator",
        "automationName": "UiAutomator2",
        "app": APP
    }
}

OPTIONS = AppiumOptions().load_capabilities(CAPS)

driver = webdriver.Remote(
    command_executor=APPIUM,
    options=OPTIONS
)
driver.quit()
