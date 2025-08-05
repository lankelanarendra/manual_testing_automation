from selenium import webdriver
from pages.login_page import LoginPage
def test_valid_login():
    driver = webdriver.Chrome()
    driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")

    login = LoginPage(driver)
    login.enter_username("admin")
    login.enter_password("admin123")
    login.click_login()

    assert login.is_dashboard_displayed()
    driver.quit()
