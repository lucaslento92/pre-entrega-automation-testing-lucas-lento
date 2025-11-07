from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import pytest
from pages.inventory_page import InventoryPage

@pytest.mark.parametrize("usuario, contraseña", [("standard_user", "secret_sauce")])
def test_inventory(login_in_driver, usuario, contraseña):
    try:
        driver = login_in_driver

        inventory_page = InventoryPage(driver)

        #Verificar titulo de la página de inventario
        assert driver.title == "Swag Labs"

        #Verifica que hay productos visibles        
        assert len(inventory_page.obtener_productos()) > 0, "No hay productos visibles"

        #Verificar carrito de compras vacio
        assert inventory_page.obtener_contador_carrito() == 0, "El carrito de compras no está vacío al iniciar sesión"

        #Agrega producto al carrito
        assert inventory_page.agregar_primer_producto() is inventory_page, "No se pudo agregar el primer producto al carrito"
        
        #Verifica que el contador del carrito incrementa 1
        assert inventory_page.obtener_contador_carrito == "1", f"El contador del carrito debería mostrar 1, pero muestra {inventory_page.text}"

        #Verifica que el carrito contiene el producto
       # driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()
       # 
       # cart_item = WebDriverWait(driver, 10).until(
       #     EC.visibility_of_element_located((By.CLASS_NAME, 
       #     "cart_item"))
       # )

    except Exception as e:
        print(f"Error en test_inventory: {e}")
        raise
    finally:
        driver.quit()

#py -m pytest tests/test_inventory.py -v