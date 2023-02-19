
from seleniumwire import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from dataclasses import dataclass


@dataclass
class DriverFactory:
    config: object = None

    def get_driver(self):
        driver = webdriver.Chrome(ChromeDriverManager().install())
        driver.set_window_size(1920, 1200, 'current')
        driver.implicitly_wait(5)
        return driver
