from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def enter_username(self, username):
        self.wait.until(EC.visibility_of_element_located((By.NAME, "username"))).send_keys(username)

    def enter_password(self, password):
        self.wait.until(EC.visibility_of_element_located((By.NAME, "password"))).send_keys(password)

    def click_login(self):
        self.wait.until(EC.element_to_be_clickable((By.XPATH, "//button[@type='submit']"))).click()

    def is_login_button_clickable(self):
        return self.wait.until(EC.element_to_be_clickable((By.XPATH, "//button[@type='submit']"))).is_enabled()

    def is_login_page_loaded(self):
        return "OrangeHRM" in self.driver.title

    def is_dashboard_displayed(self):
        return "dashboard" in self.driver.current_url or "Dashboard" in self.driver.page_source
