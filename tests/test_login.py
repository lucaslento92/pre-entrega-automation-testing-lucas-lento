from selenium import webdriver
from selenium.webdriver.common.by import By
import pytest
from pages.login_page import LoginPage
from utils.datos import leer_csv_login

@pytest.mark.parametrize("usuario, contraseña, debe_funcionar",leer_csv_login("datos/data_login.csv"))

def test_login_validation(login_in_driver, usuario, contraseña, debe_funcionar):
    driver = login_in_driver

    if debe_funcionar == True:
        assert "/inventory.html" in driver.current_url, "No se redirigio correctamente a la url inventario"
    elif debe_funcionar == False:
        mensaje_error = LoginPage(driver).catch_error()
        assert "Epic sadface" in mensaje_error, "el mensaje no se muestra"

#py -m pytest tests/test_login.py -v