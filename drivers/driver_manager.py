from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from utils.logger import get_logger 

log = get_logger(__name__)

class DriverManager:
    """Gerencia a criação e encerramento das instâncias do WebDriver."""
    
    @staticmethod
    def get_driver(browser='chrome'):
        """Inicializa e retorna o WebDriver com opções 'limpas'."""
        
        if browser == 'chrome':
            driver_path = ChromeDriverManager().install()
            service = ChromeService(executable_path=driver_path)
            options = webdriver.ChromeOptions()
            options.add_experimental_option("excludeSwitches", ["enable-automation"])
            options.add_experimental_option('useAutomationExtension', False)
            options.add_argument("--log-level=3") 
            
            return webdriver.Chrome(service=service, options=options)
        
    @staticmethod
    def quit_driver(driver):
        """Encerra o WebDriver de forma segura."""
        if driver:
            driver.quit()