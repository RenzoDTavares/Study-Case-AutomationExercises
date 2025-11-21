# pages/register_page.py
import time
from typing import Dict
from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from utils.data_generator import generate_address_data
from utils.logger import get_logger

log = get_logger(__name__)

class RegisterPage(BasePage):
    """Page Object para a tela de Registro e Detalhes da Conta."""
    
    URL_LOGIN = "login"
    SIGNUP_NAME_INPUT = (By.CSS_SELECTOR, "input[data-qa='signup-name']")
    SIGNUP_EMAIL_INPUT = (By.CSS_SELECTOR, "input[data-qa='signup-email']")
    SIGNUP_BUTTON = (By.CSS_SELECTOR, "button[data-qa='signup-button']")
    PASSWORD_INPUT = (By.CSS_SELECTOR, "input[data-qa='password']")
    DATE_DROPDOWN = (By.CSS_SELECTOR, "select[data-qa='days']")
    MONTH_DROPDOWN = (By.CSS_SELECTOR, "select[data-qa='months']")
    YEAR_DROPDOWN = (By.CSS_SELECTOR, "select[data-qa='years']")
    FIRST_NAME_INPUT = (By.CSS_SELECTOR, "input[data-qa='first_name']")
    LAST_NAME_INPUT = (By.CSS_SELECTOR, "input[data-qa='last_name']")
    ADDRESS_INPUT = (By.CSS_SELECTOR, "input[data-qa='address']")
    COUNTRY_DROPDOWN = (By.ID, "country")
    STATE_INPUT = (By.CSS_SELECTOR, "input[data-qa='state']")
    CITY_INPUT = (By.CSS_SELECTOR, "input[data-qa='city']")
    ZIPCODE_INPUT = (By.CSS_SELECTOR, "input[data-qa='zipcode']")
    MOBILE_NUMBER_INPUT = (By.CSS_SELECTOR, "input[data-qa='mobile_number']")
    CREATE_BUTTON = (By.CSS_SELECTOR, "button[data-qa='create-account']")
    ACCOUNT_CREATED_MESSAGE = (By.CSS_SELECTOR, "h2[data-qa='account-created']")
    CONTINUE_BUTTON = (By.CSS_SELECTOR, "a[data-qa='continue-button']")
    LOGOUT_LINK = (By.CSS_SELECTOR, "a[href='/logout']")
    DELETE_ACCOUNT_LINK = (By.CSS_SELECTOR, "a[href='/delete_account']")
    ACCOUNT_DELETED_MESSAGE = (By.CSS_SELECTOR, "h2[data-qa='account-deleted']")
    SIGNUP_LOGIN_LINK = (By.CSS_SELECTOR, "a[href='/login']")
    TITLE_MR = (By.ID, "id_gender1")
    DOB_DAY = (By.ID, "days")
    DOB_MONTH = (By.ID, "months")   
    DOB_YEAR = (By.ID, "years")
    
    
    def __init__(self, driver):
        super().__init__(driver) 

    def go_to_register_page(self):
        """Método para navegar para a página onde o signup é iniciado."""
        self.driver.get(f"{self.base_url}{self.URL_LOGIN}") 
        log.info("Navegou para a página de Login/Signup.")

    def fill_signup_form(self, name, email):
        """Preenche os campos de Nome e Email na seção New User Signup!"""
        self.wait_for_element_and_send_keys(self.SIGNUP_NAME_INPUT, name)
        self.wait_for_element_and_send_keys(self.SIGNUP_EMAIL_INPUT, email)
        log.info(f"Dados de Signup preenchidos: {name}, {email}")

    def  click_signup_button(self):
        """Clica no botão 'Signup' inicial."""
        self.click_element(self.SIGNUP_BUTTON)
        log.info("Botão Signup inicial clicado.")
        
    def fill_account_details(self, data: Dict[str, str]):
        """
        Preenche o formulário detalhado de criação de conta com dados DINÂMICOS.
        Recebe o dicionário 'data' do Step Definition.
        """
        self.click_element(self.TITLE_MR)
        
        self.select_from_dropdown(self.DOB_DAY, data['dob_day'])
        self.select_from_dropdown(self.DOB_MONTH, data['dob_month'])
        self.select_from_dropdown(self.DOB_YEAR, data['dob_year'])
        self.select_from_dropdown(self.COUNTRY_DROPDOWN, data['country'])
        
        self.wait_for_element_and_send_keys(self.PASSWORD_INPUT, data['password'])
        
        self.wait_for_element_and_send_keys(self.FIRST_NAME_INPUT, data['first_name'])
        self.wait_for_element_and_send_keys(self.LAST_NAME_INPUT, data['last_name'])
        self.wait_for_element_and_send_keys(self.ADDRESS_INPUT, data['address1'])
        self.wait_for_element_and_send_keys(self.STATE_INPUT, data['state'])
        self.wait_for_element_and_send_keys(self.CITY_INPUT, data['city'])
        self.wait_for_element_and_send_keys(self.ZIPCODE_INPUT, data['zipcode'])
        self.wait_for_element_and_send_keys(self.MOBILE_NUMBER_INPUT, data['mobile_number'])
        
        log.info(f"Detalhes da conta preenchidos com dados dinâmicos para {data['first_name']}.")
        
    def click_create_account_button(self):
        """Clica no botão final 'Create Account'."""
        self.click_element(self.CREATE_BUTTON)

    def is_confirmation_message_visible(self, expected_message: str) -> bool:
        """Verifica se a mensagem de confirmação (ACCOUNT CREATED! ou ACCOUNT DELETED!) está visível."""
        try:
            actual_text = self.get_element_text(self.Exp)
            log.info(f"Mensagem de confirmação encontrada: {actual_text}")
            return expected_message in actual_text
        except Exception as e:
            log.error(f"Mensagem de confirmação não encontrada: {e}")
            return False
    
        
    def click_continue_button(self):
        """Clica no botão 'Continue' após o sucesso ou deleção."""
        self.click_element(self.CONTINUE_BUTTON)
        log.info("Botão Continue clicado.")
    
    def is_user_logged_in(self, msg: str) -> bool:
        """Verifica se a mensagem 'Logged in as {username}' está visível no header."""
        locator = (By.XPATH, f"//li/a[contains(text(), 'Logged in as {msg}')]")
        try:
            self.wait_for_element(locator)
            log.info(f"Usuário logado confirmado no header: {msg}")
            
            return True
        except Exception as e:
            log.error(f"Usuário logado não encontrado no header: {e}")
            return False
        
    def click_delete_account_link(self):
        """Clica no link 'Delete Account'."""
        self.click_element(self.DELETE_ACCOUNT_LINK)
        log.info("Link Delete Account clicado.")
        
    def is_message_visible(self, expected_message: str) -> bool:
        """Verifica se uma mensagem específica está visível na página."""
        locator = (By.XPATH, f"//*[contains(text(), '{expected_message}')]")
        try:
            self.wait_for_element(locator)
            log.info(f"Mensagem visível na página: {expected_message}")
            return True
        except Exception as e:
            log.error(f"Mensagem não encontrada na página: {e}")
            return False
 
    
    def is_logged_out_visible(self) -> bool:
        """Verifica se o usuário está deslogado, checando a presença do link Signup/Login."""
        try:
            self.wait_for_element(self.SIGNUP_LOGIN_LINK)
            log.info("Usuário está deslogado, link Signup/Login encontrado.")
            return True
        except Exception as e:
            log.error(f"Usuário não está deslogado: {e}")
            return False