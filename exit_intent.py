
import unittest
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.action_chains import ActionChains


class TestExitIntent(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())
        self.driver.implicitly_wait(3)
        self.base_url = "https://the-internet.herokuapp.com/exit_intent"

    def test_exit_intent(self):
        driver = self.driver
        driver.get(self.base_url)
        time.sleep(3)
        # Mouse
        body = driver.find_element(By.TAG_NAME, 'body')
        chains = ActionChains(driver)
        chains.move_to_element_with_offset(body, 0, 500).perform()
        time.sleep(3)
        modal = driver.find_element(By.ID, 'ouibounce-modal')
        self.assertTrue(modal.is_displayed())

    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()
