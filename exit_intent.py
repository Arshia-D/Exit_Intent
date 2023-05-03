from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains


driver = webdriver.Firefox()

driver.get("https://the-internet.herokuapp.com/exit_intent")

modal = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "ouibounce-modal")))

#Mouse
exit_intent_area = driver.find_element(By.CSS_SELECTOR, "div#content")
driver.execute_script("arguments[0].scrollIntoView();", exit_intent_area)
actions = ActionChains(driver)
actions.move_to_element(exit_intent_area)
actions.perform()

modal_displayed = WebDriverWait(driver, 10).until(EC.visibility_of(modal))

modal_close_button = driver.find_element(By.CSS_SELECTOR, "div#ouibounce-modal div.modal-footer p")
modal_close_button.click()

driver.quit()
