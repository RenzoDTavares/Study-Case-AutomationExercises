# pages/base_page.py
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from utils.logger import get_logger 
log = get_logger(__name__)

class BasePage:
    """
    Classe base para Page Objects. Contém métodos reutilizáveis para 
    interação estável com o Selenium WebDriver e tratamento de esperas.
    """
    
    def __init__(self, driver: WebDriver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 15)

    def wait_for_element(self, locator: tuple):
        """Espera até que um elemento esteja visível e o retorna."""
        try:
            element = self.wait.until(EC.visibility_of_element_located(locator))
            return element
        except TimeoutException:
            log.error(f"Timeout: Elemento não visível: {locator}")
            raise TimeoutException(f"Elemento não visível após 15s: {locator}")

    def click_element(self, locator: tuple):
        """Espera até que um elemento esteja clicável e clica nele."""
        element = self.wait_for_element(locator)
        self.wait.until(EC.element_to_be_clickable(element)).click()
        log.info(f"Clicado no elemento: {locator}")
    
    def wait_for_element_and_send_keys(self, locator: tuple, text: str):
        """Espera até que o elemento esteja presente, limpa e envia o texto."""
        element = self.wait_for_element(locator)
        element.clear()
        element.send_keys(text)
        log.info(f"Texto enviado para {locator}")

    def get_element_text(self, locator: tuple) -> str:
        """Retorna o texto de um elemento após esperar por ele."""
        element = self.wait_for_element(locator)
        return element.text.strip()