import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from utils import login

@pytest.fixture
def driver():
    # Configuración de Chrome
    options = webdriver.ChromeOptions()

    # 🔧 Desactivar el administrador de contraseñas y el aviso de seguridad de Google
    prefs = {
        "credentials_enable_service": False,
        "profile.password_manager_enabled": False
    }
    options.add_experimental_option("prefs", prefs)

    # Opcional: abrir Chrome en modo incógnito (evita datos guardados previos)
    options.add_argument("--incognito")

    driver= webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    yield driver
    driver.quit()

@pytest.fixture
def login_in_driver(driver):
    login(driver)
    return driver