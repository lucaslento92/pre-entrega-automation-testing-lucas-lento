from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import pytest
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage

@pytest.mark.parametrize("usuario, contraseña", [("standard_user", "secret_sauce")])
def test_cart(login_in_driver, usuario, contraseña):
    try:
        driver = login_in_driver
        inventory_page = InventoryPage(driver)
        #Agregar un producto al carrito
        inventory_page.agregar_primer_producto()
        #Ir al carrito
        inventory_page.ir_al_carrito()
        #Validar producto en el carrito
        cart_page = CartPage(driver)

        productos_en_carrito = cart_page.obtener_items_carrito()
        assert len(productos_en_carrito) == 1

    except Exception as e:
        print(f"Error en test_cart: {e}")
        raise
    finally:
        driver.quit()