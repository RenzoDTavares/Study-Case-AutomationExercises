from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    LOGIN_EMAIL_INPUT = (By.CSS_SELECTOR, "input[data-qa='login-email']")
    LOGIN_PASSWORD_INPUT = (By.CSS_SELECTOR, "input[data-qa='login-password']")
    LOGIN_BUTTON = (By.CSS_SELECTOR, "button[data-qa='login-button']")
    
    URL = "https://automationexercise.com/login"

    def go_to_login_page(self):
        """Acessa a URL de login."""
        self.driver.get(self.URL)

    def fill_login_form(self, email, password):
        """Preenche os campos de email e senha."""
        email_element = self.wait.until(EC.visibility_of_element_located(self.LOGIN_EMAIL_INPUT))
        email_element.clear()
        email_element.send_keys(email)

        password_element = self.driver.find_element(*self.LOGIN_PASSWORD_INPUT)
        password_element.clear()
        password_element.send_keys(password)

    def click_login_button(self):
        """Clica no botão de login."""
        button = self.driver.find_element(*self.LOGIN_BUTTON)
        button.click()
        
class RegisterPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    LOGIN_EMAIL_INPUT = (By.CSS_SELECTOR, "input[data-qa='login-email']")
    LOGIN_PASSWORD_INPUT = (By.CSS_SELECTOR, "input[data-qa='login-password']")
    LOGIN_BUTTON = (By.CSS_SELECTOR, "button[data-qa='login-button']")
    
    URL = "https://automationexercise.com/login"

    def go_to_login_page(self):
        """Acessa a URL de login."""
        self.driver.get(self.URL)

    def fill_login_form(self, email, password):
        """Preenche os campos de email e senha."""
        email_element = self.wait.until(EC.visibility_of_element_located(self.LOGIN_EMAIL_INPUT))
        email_element.clear()
        email_element.send_keys(email)

        password_element = self.driver.find_element(*self.LOGIN_PASSWORD_INPUT)
        password_element.clear()
        password_element.send_keys(password)

    def click_login_button(self):
        """Clica no botão de login."""
        button = self.driver.find_element(*self.LOGIN_BUTTON)
        button.click()