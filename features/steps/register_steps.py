# features/steps/register_steps.py
import time
from behave import given, when, then, step
from selenium.webdriver.support.ui import WebDriverWait 
from pages.register_page import RegisterPage
from utils.data_generator import generate_address_data, generate_full_name, generate_unique_email, generate_unique_email, generate_password
from utils.logger import get_logger

log = get_logger(__name__)

@given('que estou na página de registro')
def step_impl(context):
    """Navega diretamente para a página de registro (Signup)."""
    register_page = RegisterPage(context.driver)
    register_page.go_to_register_page()
    log.info("Preparação: Usuário na tela de Registro.")
    
@given(u'eu insiro o nome e o e-mail') 
def step_impl(context):
    """Preenche os campos do formulário de registro inicial (nome e email)."""
    register_page = RegisterPage(context.driver)
    generated_name = generate_full_name()
    generated_email = generate_unique_email()
    generated_password = generate_password()
    
    context.signup_name = generated_name
    context.signup_email = generated_email
    context.signup_password = generated_password
    
    register_page.fill_signup_form(generated_name, generated_email)
    log.info(f"Dados iniciais preenchidos: Nome: {generated_name}, Email: {generated_email}")
    
@given(u'clico no botão "Signup"') 
@when('clico no botão "Signup"')
def step_impl(context):
    """Clica no botão 'Signup' inicial."""
    register_page = RegisterPage(context.driver)
    register_page.click_signup_button()


@when('eu preencho os detalhes da conta')
def step_impl(context):
    """Preenche o formulário detalhado de criação de conta com dados DINÂMICOS."""
    register_page = RegisterPage(context.driver)
    
    address_data = generate_address_data()
    address_data['password'] = context.signup_password 
    register_page.fill_account_details(address_data)
    
    context.account_details = address_data 

@when('clico no botão de criar conta')
def step_impl(context):
    """Clica no botão final de criação de conta."""
    register_page = RegisterPage(context.driver)
    register_page.click_create_account_button()

@then('a mensagem de confirmação "{message}" deve ser exibida')
def step_impl(context, message):
    """Verifica se a mensagem de conta deletada é exibida."""
    register_page = RegisterPage(context.driver)
    register_page.is_confirmation_message_visible(message)

@then(u'clico no botão "Continue"')
@when(u'clico no botão "Continue"')
def step_impl(context):
    register_page = RegisterPage(context.driver)
    register_page.click_continue_button()
    

@then(u'a mensagem Logged in as "{username}" deve estar visível no header')
def step_impl(context, username):
    """
    Valida a exibição do nome do usuário logado no header.
    Usa o nome de usuário salvo no contexto.
    """
    register_page = RegisterPage(context.driver)
    
    user_to_validate = getattr(context, 'username', username) 

    register_page.is_user_logged_in(user_to_validate)
    
@when(u'eu clico no link "Delete Account"')
def step_impl(context):
    """Clica no link 'Delete Account'."""
    register_page = RegisterPage(context.driver)
    register_page.click_delete_account_link()

@then('confirmo que estou deslogado')
def step_impl(context):
    """Verifica se o usuário está deslogado."""
    register_page = RegisterPage(context.driver)
    register_page.is_logged_out_visible()
