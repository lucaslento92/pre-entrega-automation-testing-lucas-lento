from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class InventoryPage: 
    _TITLE = (By.CLASS_NAME, "title") 
    _PRODUCTS = (By.CLASS_NAME, "inventory_item")
    _ITEM_NAME = (By.CLASS_NAME, "inventory_item_name")
    _ADD_BUTTONS = (By.CSS_SELECTOR, ".inventory_item button") 
    _CART_BADGE = (By.CLASS_NAME, "shopping_cart_badge") 
    _CART_LINK = (By.CLASS_NAME, "shopping_cart_link") 
    _MENU_BUTTON = (By.ID, "react-burger-menu-btn") 
    _LOGOUT_LINK = (By.ID, "logout_sidebar_link")

    def __init__(self, driver): 
        self.driver = driver 
        self.wait = WebDriverWait(driver, 10)
 
    def obtener_productos(self):
       self.wait.until( 
           EC.visibility_of_element_located(self._PRODUCTS))
       productos = self.driver.find_elements(*self._PRODUCTS) 
       return productos

    def obtener_nombres_productos(self):
        productos = self.driver.find_elements(*self._ITEM_NAME) 
        return [producto_nombre.text for producto_nombre in productos]
    
    def agregar_primer_producto(self):
        productos = self.wait.until(EC.visibility_of_all_elements_located(self._PRODUCTS)) 

        primer_boton_producto = productos[0].find_element(*self._ADD_BUTTONS)
        primer_boton_producto.click() 

    def agregar_producto_por_nombre(self, nombre_producto):
        productos = self.driver.find_elements(*self._PRODUCTS) 
        for producto in productos:
            nombre = producto.find_element(*self._ITEM_NAME).text 
            if nombre == nombre_producto:
                boton_agregar = producto.find_element( 
                    *self._ADD_BUTTONS) 
                boton_agregar.click() 
                return self 
        raise Exception(f"Producto con nombre '{nombre_producto}' no encontrado.")

    def obtener_contador_carrito(self):
        try: 
            badge = self.driver.find_element(*self._CART_BADGE) 
            return int(badge.text) 
        except: 
            return 0 
 
    def ir_al_carrito(self): 
        self.wait.until( 
            EC.element_to_be_clickable(self._CART_LINK)).click() 
        return self
 
    def hacer_logout(self):
        self.driver.find_element(*self._MENU_BUTTON).click() 
        logout_link = self.wait.until( 
            EC.element_to_be_clickable(self._LOGOUT_LINK) 
       ) 
        logout_link.click() 
        from pages.login_page import LoginPage 
        return LoginPage(self.driver)