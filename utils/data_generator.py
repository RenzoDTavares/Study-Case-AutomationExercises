# utils/data_generator.py
import random
import string
import time
from typing import Dict
from datetime import date, timedelta

# --- Listas de dados semi-realistas para Mock ---
FIRST_NAMES = ['Arthur', 'Beatriz', 'Carlos', 'Diana', 'Eduardo', 'Fernanda', 'Gustavo', 'Helena']
LAST_NAMES = ['Silva', 'Pereira', 'Oliveira', 'Santos', 'Costa', 'Rodrigues', 'Almeida']
STREETS = ['Avenida Central', 'Rua das Flores', 'Alameda dos Anjos', 'Praça da Liberdade']
CITIES = ['New York', 'Los Angeles', 'Chicago', 'Houston', 'Miami']

def generate_unique_email(prefix="qa_user", domain="test.com"):
    """
    Gera um email único com prefixo e timestamp, ideal para testes de cadastro.
    """
    timestamp = int(time.time())
    unique_part = f"{prefix}_{timestamp}"
    return f"{unique_part}@{domain}"

def generate_full_name() -> str:
    """
    Gera um nome completo aleatório a partir de listas predefinidas.
    """
    first_name = random.choice(FIRST_NAMES)
    last_name = random.choice(LAST_NAMES)
    return f"{first_name} {last_name}"

def generate_random_date_of_birth(min_age=25, max_age=40) -> date:
    """
    Gera uma data de nascimento aleatória para garantir que o usuário tenha entre
    min_age e max_age anos.
    """
    end_date = date.today() - timedelta(days=365 * min_age)
    start_date = date.today() - timedelta(days=365 * max_age)
    
    time_between_dates = end_date - start_date
    days_between_dates = time_between_dates.days
    random_number_of_days = random.randrange(days_between_dates)
    
    random_date = start_date + timedelta(days=random_number_of_days)
    return random_date

def generated_unique_email() -> str:
    """Gera um email único usando timestamp."""
    timestamp = int(time.time())
    return f"qa_user_{timestamp}@test.com"

def generate_password (length=10) -> str:
    """Gera uma senha aleatória com letras e dígitos."""
    characters = string.ascii_letters + string.digits
    return ''.join(random.choice(characters) for _ in range(length))

def generate_address_data() -> Dict[str, str]:
    """
    Gera um dicionário completo com dados dinâmicos de endereço, contato e DOB.
    """
    first_name = random.choice(FIRST_NAMES)
    last_name = random.choice(LAST_NAMES)
    
    # Geração da Data de Nascimento
    dob = generate_random_date_of_birth()
    
    # Formatação do Mobile Number
    mobile_number = f"+1{random.randint(100, 999)}{random.randint(100, 999)}{random.randint(1000, 9999)}"
    
    return {
        "first_name": first_name,
        "last_name": last_name,
        "company": "QA Tech Solutions",
        "address1": f"{random.randint(10, 999)} {random.choice(STREETS)}",
        "address2": "Apt 2B",
        "country": "Canada",
        "state": "Quebec",
        "city": random.choice(CITIES),
        "zipcode": str(random.randint(10000, 99999)),
        "mobile_number": mobile_number,
        
        # CHAVES CRÍTICAS PARA DOB (RESOLVENDO O DEFEITO DE ARQUITETURA)
        "dob_day": str(dob.day),
        "dob_month": dob.strftime('%B'), # Ex: 'May' (Assumindo que o site usa o nome completo do mês)
        "dob_year": str(dob.year)
    }

def generate_cpf():
    """ [Não usado no cenário AE, mantido por histórico] """
    def calculate_digit(digits):
        sum_ = sum(int(digit) * weight for digit, weight in zip(digits, range(len(digits)+1, 1, -1)))
        remainder = sum_ % 11
        return '0' if remainder < 2 else str(11 - remainder)

    base = ''.join(random.choices(string.digits, k=9))
    first_digit = calculate_digit(base)
    second_digit = calculate_digit(base + first_digit)
    return f"{base}{first_digit}{second_digit}"