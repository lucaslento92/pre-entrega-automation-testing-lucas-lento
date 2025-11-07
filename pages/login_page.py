from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class LoginPage:
    URL = "https://www.saucedemo.com"

    _USER_INPUT = (By.ID, "user-name")
    _PASS_INPUT = (By.ID, "password")
    _LOGIN_BUTTON = (By.ID, "login-button")

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def abrir_pagina(self):
        self.driver.get(self.URL)
        return self
    
    def login_user(self, usuario):
        input = self.wait.until(EC.visibility_of_element_located(self._USER_INPUT))
        input.clear()
        input.send_keys(usuario)
        return self
    
    def login_password(self, contraseña: str):
        input = self.driver.find_element(*self._PASS_INPUT)
        input.clear()
        input.send_keys(contraseña)
        return self
    
    def login_click_button(self):
        self.driver.find_element(*self._LOGIN_BUTTON).click()
        return self

    def login(self, usuario, contraseña):
        self.login_user(usuario)
        self.login_password(contraseña)
        self.login_click_button()
        return self
    
    def catch_error(self):
        div_error = self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".error-message-container h3")))
        return div_error.text