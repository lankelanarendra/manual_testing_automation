from selenium import webdriver
from pages.login_page import LoginPage

def test_login_button_clickable():
    driver = webdriver.Chrome()
    driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")

    login = LoginPage(driver)
    assert login.is_login_button_clickable()
    driver.quit()
