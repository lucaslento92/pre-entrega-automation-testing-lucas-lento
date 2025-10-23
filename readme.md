Descripción del Proyecto:

Este proyecto forma parte de la pre-entrega del curso de Automatización QA, donde se aplican los conceptos aprendidos hasta la Clase 8.
El objetivo es automatizar flujos básicos del sitio https://www.saucedemo.com, incluyendo inicio de sesión, validación de elementos en la página de inventario y la interacción con el carrito de compras utilizando Python, Selenium WebDriver y Pytest.

Funcionalidades Automatizadas:

* Login Automático con credenciales válidas.
* Validación de acceso a la página de inventario.
* Verificación de productos visibles y título de página.
* Agregar un producto al carrito y validar el contador.
* Navegar al carrito y comprobar el producto agregado.

Tecnologías Utilizadas:

* Python: Lenguaje principal.
* Selenium WebDriver: Automatización del navegador.
* Pytest: Framework de testing.
* WebDriver Manager: Manejo automático del driver.
* Git & GitHub: Control de versiones y repositorio.
* Pytest-HTML: Generación de reportes HTML.

Estructura del proyecto:

preentrega-lucas-lento/
│
├── tests/
│   └── test_login.py
│   └── test_inventory.py
│
├── utils.py #Funciones auxiliares y setup
│
├── report.html  #Reporte generado por pytest
│
├── assets/
│   └── style.css
│
├── conftest.py
│
├── run_test.py #Argumentos para ejecutar pruebas: archivos + reporte HTML
│
├── README.md

Instalar dependencias:

* pip install selenium
* pip install pytest
* pip install webdriver-manager
* pip install pytest-html

Ejecutar todos los tests con reporte HTML:

* pytest -v --html=reports/report.html --self-contained-html

Ejecutar un test específico:

* pytest tests/test_inventory.py -v

Reporte de Resultados:

Al finalizar la ejecución, se genera un reporte HTML con el detalle de:
* Casos ejecutados.
* Resultados (passed/failed).
* Tiempos de ejecución.
* Capturas en caso de error (si corresponde).

Objetivo del Proyecto:

El propósito de esta automatización es:
* Aplicar buenas prácticas en Selenium WebDriver.
* Utilizar Pytest con una estructura modular.
* Validar el comportamiento del sitio web desde la perspectiva del usuario.
* Preparar el entorno para futuras automatizaciones avanzadas.

Próximos pasos (Entrega Final):

* Implementar Page Object Model (POM).
* Agregar manejo de logs y screenshots automáticas.
* Incorporar validaciones más avanzadas y flujos completos de compra.

Autor:
    Lucas Lento - Proyecto realizado para la materia Automatización QA