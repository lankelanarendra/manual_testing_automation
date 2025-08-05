from selenium import webdriver
from pages.login_page import LoginPage
def test_retest_login_user123():
    driver = webdriver.Chrome()
    driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")

    login = LoginPage(driver)
    login.enter_username("user123")
    login.enter_password("pass123")
    login.click_login()

    assert login.is_dashboard_displayed()
    driver.quit()
