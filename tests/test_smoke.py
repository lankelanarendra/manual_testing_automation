import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from pages.login_page import LoginPage

def test_smoke_login():
    driver = webdriver.Chrome()
    driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    driver.maximize_window()
    login = LoginPage(driver)
    assert login  # Check if page loads
    driver.quit()
