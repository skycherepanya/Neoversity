import re
from typing import Callable, Generator


def generator_numbers(text: str) -> Generator[float, None, None]:
    # Аналізує вхідний текст, знаходить всі дійсні числа та повертає їх як генератор
    pattern = r"\d+\.\d+"
    matches = re.findall(pattern, text)
    # Ітерація по списку знайдених рядків
    for num_str in matches:
        yield float(num_str)


# Ми уточнили тип "func": це функція, яка приймає str і повертає генератор float, тому:
def sum_profit(text: str, func: Callable[[str], Generator[float, None, None]]) -> float:
    # Підсумовує всі числа, отримані від функції-генератора.
    numbers_generator = func(text)
    total = sum(numbers_generator)
    
    return total


text = "Загальний дохід працівника складається з декількох частин: 1000.01 як основний дохід, доповнений додатковими надходженнями 27.45 і 324.00 доларів."
total_income = sum_profit(text, generator_numbers)
print(f"Загальний дохід: {total_income}")
