# Задание 1
from queue import PriorityQueue


def make_sentence(words=['This', 'is', 'a', 'sentence']):
    return ' '.join(words) + "."

print(make_sentence())

# Задание 2

def sum_of_squares(*args):
    return sum(arg**2 for arg in args)

print(sum_of_squares(1, 2, 3, 4, 5))

# Задание 3

def greet (name, language="en"):
    if not isinstance(name, str):
        raise TypeError("имя - не является строкой")
    if language == "en":
        print (f"Hello, {name}")
    elif language == "ru":
        print (f"Привет, {name}")
    elif language == "fr":
        print(f"Bonjour, {name}")
    else:
        raise ValueError("Неизвестный язык")
    return greet

print(greet("John","ru"))

# Задание 4

def print_info (**kwargs):
    if not kwargs:
        print("нет данных.")
    else:
        for key, value in kwargs.items():
            print(f"{key}:{value}")


print_info(name="Alex", age=25, city="Amsterdam")

# Задание 5

def print_table(**kwargs):
    if not kwargs:
        print("No data given.")
        return
    print("| Key    | Value      |")
    print("|--------|------------|")
    for key, value in kwargs.items():
        print(f"| {key:<6} | {value:<10} |")

print_table(name="Bob", age=30, city="Amsterdam")

# Задание 6

def calculate(*args, operation="+"):
    if operation == "+":
        result = sum(args)
    elif operation == "-":
        result = args[0]
        for num in args[1:]:
            result -= num
    elif operation == "*":
        result = 1
        for num in args:
            result *= num
    elif operation == "/":
        result = args[0]
        for num in args[1:]:
            result /= num
    else:
        raise ValueError("Invalid operation. Use +, -, *, or /.")
    return result

print(calculate(1, 2, 3, 4, operation="+"))

# Задание 7

def print_triangle(*, height=5):
    if not isinstance(height, int) or height <= 0:
        raise ValueError("ошибка")

    for i in range(1, height + 1):
        spaces = " " * (height - i)
        stars = "*" * (2 * i - 1)
        print(spaces + stars)

print_triangle(height=10)

# Задание 8

def posts(title, content, author, category = "general", **kwargs):
    posts = {
        "title": title,
        "content": content,
        "author": author,
        "category": category,
    }
    return posts

print(posts("My first post", "This is my first blog post", "John Doe"))

# Задание 9

def create_product(name, price, category, rating=0):
    product = {
        "Имя":name,
        "Цена": price,
        "Категория": category,
        "Рейтинг": rating
    }
    return product

print(create_product("iPhone 15", 1000, "Электроника"))

# Задание 10

def student(firstname, lastname, patronymic, group, receipt_date="19.10.2023", **kwargs):
    student = {
        "имя": firstname,
        "фамилия": lastname,
        "отчество": patronymic,
        "group": group,
        "receipt_date": receipt_date
    }

    more_keys = ["avg_grade", "semester", "phone_number", "address"]

    for key in more_keys:
        value = kwargs.get(key)
        if value is not None:
            student[key] = value

    return student


print(student("John", "Doe", "Smith", "2TP", semester=1, address="ул. Пушкина, д. 10"))