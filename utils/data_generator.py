# utils/data_generator.py
import random
import string
import time

def generate_unique_email(domain="test.com"):
    """
    Gera um email único com timestamp, ideal para testes de cadastro.
    """
    timestamp = int(time.time())
    unique_part = f"user_{timestamp}"
    return f"{unique_part}@{domain}"

def generate_cpf():
    """
    Gera um número de CPF válido (formato brasileiro).
    """
    def calculate_digit(digits):
        sum_ = sum(int(digit) * weight for digit, weight in zip(digits, range(len(digits)+1, 1, -1)))
        remainder = sum_ % 11
        return '0' if remainder < 2 else str(11 - remainder)

    base = ''.join(random.choices(string.digits, k=9))
    first_digit = calculate_digit(base)
    second_digit = calculate_digit(base + first_digit)
    return f"{base}{first_digit}{second_digit}"