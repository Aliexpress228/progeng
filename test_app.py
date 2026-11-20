from app import get_greeting, add_numbers

def test_greeting():
    """Тест 1: Проверка строки."""
    assert get_greeting() == "Hello, MIREA CI!"

def test_addition():
    """Тест 2: Проверка математики."""
    assert add_numbers(2, 2) == 4
