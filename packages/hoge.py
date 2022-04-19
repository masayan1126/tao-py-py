from selenium import webdriver
from selenium.webdriver import DesiredCapabilities
from selenium.common.exceptions import SessionNotCreatedException
from packages.twi_automation.env import ENV

from shared.x_logger import XLogger


try:
    driver = webdriver.Remote(
        command_executor="http://docker-python_selenium_1:4444/wd/hub",
        desired_capabilities=DesiredCapabilities.CHROME.copy(),
    )
    title = driver.get("https://qiita.com/advent-calendar/2017/docker")

except SessionNotCreatedException as e:
    # raise e
    XLogger.exception_to_slack(ENV["SLACK_WEBHOOK_URL_TWITTER_AUTOMATION"], e)
finally:
    if "driver" in locals():
        driver.quit()

print("debug")
