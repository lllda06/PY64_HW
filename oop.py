import random
from datetime import datetime
from decimal import Decimal


# Задание 1. Класс «Игровой персонаж»

class GameCharacter(object):
    def __init__(self, name: str, health: int = 100, level: int = 1):
        self.name = name
        self.__health = min(health, 100)
        self.level = level

    @property
    def health(self):
        return self.__health

    @health.setter
    def health(self, value: int):
        # при попытке установить здоровье выше 100 оно
        # автоматически становилось 100
        if value > 100:
            self.__health = 100
        else:
            self.__health = value

    def _level_up(self):
        # защищённый метод _level_up(), который увеличивает уровень на 1
        self.level += 1

    def attack(self, other_character):
        # метод attack(other_character), который уменьшает здоровье другого персонажа на 10
        if isinstance(other_character, GameCharacter):
            other_character.health -= 10

    @classmethod
    # classmethod, который создаёт персонажа с максимальным здоровьем (100) и
    # уровнем 1
    def create_character(cls, name: str):
        return cls(name, health=100, level=1)

    @staticmethod
    # Сделай staticmethod, который сравнивает двух персонажей по уровню и возвращает
    # того, у кого уровень выше.
    def compare_characters(character1: 'GameCharacter', character2: 'GameCharacter'):
        return character1 if character1.level > character2.level else character2

    def __str__(self):
        return f'{self.name} level: {self.level} - health: {self.health} hp'


# Задание 2. Класс «Магазин»

class Store(object):
    def __init__(self, name: str, goods: list = None):
        self.name = name
        self.goods = goods if goods is not None else []

    def add_product(self, name, price, quantity):
        # добавить товар в магазин
        self.goods.append({'name': name, 'price': price, 'quantity': quantity})

    def remove_product(self, name):
        # удалить товар по имени
        for product in self.goods:
            if product['name'] == name:
                self.goods.remove(product)
                break

    def update_price(self, name: str, new_price: float):
        # изменить цену товара
        for product in self.goods:
            if product['name'] == name:
                product['price'] = new_price
                break

    def sell_product(self, name: str, quantity: int):
        # продать указанное количество товара
        # (уменьшить остаток, если хватает)
        for product in self.goods:
            if product['name'] == name:
                if product['quantity'] >= quantity:
                    product['quantity'] -= quantity
                else:
                    raise ValueError(f'Недостаточно товара {name} на складе.')
                break

    def get_inventory(self):
        # вернуть список всех товаров и их количество
        return [(product['name'], product['quantity']) for product in self.goods]

    def find_most_expensive(self):
        # вернуть самый дорогой товар
        if not self.goods:
            return None
        return max(self.goods, key=lambda product: product['price'])

    def find_cheapest(self):
        # вернуть самый дешёвый товар
        if not self.goods:
            return None
        return min(self.goods, key=lambda product: product['price'])

    def __str__(self):
        lines = [f'Магазин: {self.name}', 'Товары: ']
        for product in self.goods:
            lines.append(f'{product["name"]}: {product["price"]} руб - {product["quantity"]} шт.')
        return '\n'.join(lines)


# Задание 3. Класс «Библиотека» и класс «Книга»

class Book(object):
    def __init__(self, name: str, author: str, publishing_year: int):
        self.name = name
        self.author = author
        self.publishing_year = publishing_year
        self.status = 'в библиотеке'

    def info(self):
        # выводит информацию о книге
        return f'Книга: {self.name}, автор: {self.author}, год издания: {self.publishing_year}, статус: {self.status}'

    def mark_as_taken(self):
        # меняет статус на «выдана»
        self.status = 'выдана'

    def mark_as_returned(self):
        # меняет статус на «в библиотеке»
        self.status = 'в библиотеке'


class Library(object):
    def __init__(self, name: str):
        self.name = name
        self.books = []

    def add_book(self, book: Book):
        # добавляет книгу в библиотеку
        self.books.append(book)

    def remove_book(self, book):
        # удаляет книгу из библиотеки
        for book in self.books:
            if book['name'] == book.name:
                self.books.remove(book)
            break

    def find_by_author(self, author: str):
        # находит все книги автора
        return [book for book in self.books if book.author == author]

    def find_by_year(self, year: int):
        # находит все книги указанного года
        return [book for book in self.books if book.year == year]

    def available_books(self):
        # возвращает список всех книг, которые в библиотеке
        return [book for book in self.books if book.status == 'в библиотеке']

    def taken_books(self):
        # возвращает список всех выданных книг
        return [book for book in self.books if book.status == 'выдана']


# Задание 4. Класс «Кошелёк»


class Wallet(object):
    def __init__(self, balance: float = 0):
        self.__balance = Decimal(str(balance))

    @property
    def balance(self):
        # позволяет просматривать баланс
        return self.__balance

    def __apply_bonus(self):
        # добавить 1% бонуса к балансу,
        # вызывается автоматически после каждой операции пополнения
        self.__balance *= Decimal('1.01')

    def deposit(self, amount: float):
        # пополнить кошелёк
        amount = Decimal(str(amount))
        if amount > 0:
            self.__balance += amount
            self.__apply_bonus()

    def withdraw(self, amount: float):
        # снять деньги (если хватает)
        amount = Decimal(str(amount))
        if amount <= self.__balance:
            self.__balance -= amount
        else:
            raise ValueError('Недостаточно средств')

    def transfer_to(self, other_wallet, amount: float):
        # перевести деньги другому кошельку
        amount = Decimal(str(amount))
        if amount <= self.__balance:
            self.withdraw(amount)
            other_wallet.deposit(amount)
        else:
            raise ValueError('Недостаточно средств')


@staticmethod
def wallet_info(wallet: 'Wallet'):
    # выводит краткую информацию о кошельке
    rounded_balance = wallet.balance.quantize(Decimal('0.01'))
    return f'Баланс кошелька: {rounded_balance}'


# Задание 5. Класс «Система заказов»

class Order(object):
    def __init__(self, order_id: int):
        self.order_id = order_id
        self.items = []
        self.status = 'новый'

    def calculate_total(self):
        # возвращает сумму заказа
        return sum(item['price'] for item in self.items)

    def add_item(self, name: str, price: float, quantity: int):
        # добавляет товар в заказ
        self.items.append({'name': name, 'price': price, 'quantity': quantity})

    def remove_item(self, name: str):
        # удаляет товар из заказа
        for item in self.items:
            if item['name'] == name:
                self.items.remove(item)
            break

    def change_status(self, status: str):
        # изменяет статус заказа (например, «новый», «в
        # работе», «завершён»)
        if status == 'новый':
            self.status = status
        elif status == 'в работе':
            self.status = status
        elif self.status == 'завершён':
            self.status = status
        else:
            raise ValueError('Такого статуса нет')

    class OrderSystem(object):
        def __init__(self):
            self.orders = []
            self.next_order_id = 1

        def create_order(self):
            # создаёт новый заказ
            order = Order(self.next_order_id)
            self.orders.append(order)
            self.next_order_id += 1
            return order

        def get_order_by_id(self, order_id: int):
            # возвращает заказ по номеру
            for order in self.orders:
                if order.order_id == order_id:
                    return order
            return None

        def get_total_revenue(self, status: str):
            # возвращает общую сумму по всем завершённым
            # заказам
            total = 0
            for order in self.orders:
                if status == 'завершен':
                    total += order.calculate_total()
            return total

        def list_orders_by_status(self, status: str):
            # возвращает все заказы с определённым статусом
            all_orders = []
            for order in self.orders:
                if order.status == status:
                    all_orders.append(order)
            return all_orders

    # Задание 6. Класс «Автомобиль»

    class Car(object):
        def __init__(self, brand: str, model: str, year: int, fuel: int, mileage: int):
            self.brand = brand
            self.model = model
            self.year = year
            self.fuel = fuel
            self.mileage = mileage

        def drive(self, distance: int):
            # увеличить пробег и уменьшить топливо (расход 0.1 л на 1 км
            if distance > 0:
                fuel_needed = distance * 0.1
                if self.fuel >= fuel_needed:
                    self.mileage += distance
                    self.fuel -= fuel_needed
                else:
                    raise ValueError('Недостаточно топлива!')
            else:
                raise ValueError('Дистанция должна быть больше 0!')

        def refuel(self, liters: int):
            # заправить автомобиль
            if liters > 0:
                self.fuel += liters
            else:
                raise ValueError('Минимум литр топлива!')

        def info(self):
            # вывести состояние автомобиля
            return f'состояние автомобиля - автомобиль бренда: {self.brand}; модель: {self.model}; кол-во топлива: {self.fuel}; пробег автомобиля: {self.mileage}'

        def __check_fuel(self, distance: int):
            # проверяет, хватит ли топлива для поездки
            fuel_needed = distance * 0.1
            return self.fuel >= fuel_needed

        def age(self):
            # возвращает возраст автомобиля
            current_year = datetime.now().year
            return current_year - self.year

        @classmethod
        def from_string(cls, data: dict):
            parts = [part.strip() for part in data.split(',')]
            if len(parts) != 3:
                raise ValueError('Обьект вида: Brand, model, year')
            brand, model, year = parts
            return cls(brand, model, int(year))

    # Задание 7. Класс «Игровой инвентарь»
    class Inventory(object):
        def __init__(self):
            # список предметов (каждый предмет — словарь с полями name, weight,
            # value)
            self.items = []

        def add_item(self, name: str, weight: float, value: float):
            # добавить предмет
            self.items.append({'name': name, 'weight': weight, 'value': value})

        def remove_item(self, name: str):
             # удалить предмет
            for index, item in enumerate(self.items):
                if item["name"] == name:
                        self.items.pop(index)
                        break

        def get_total_weight(self):
            # вернуть общий вес
            return sum(item['weight'] for item in self.items)

        def get_total_value(self):
            # вернуть общую стоимость
            return sum(item['value'] for item in self.items)

        def find_heaviest(self):
            # найти самый тяжёлый предмет
            if not self.items:
                return None
            return max(self.items, key=lambda item: item['weight'])

        def find_most_valuable(self):
            # найти самый дорогой предмет
            if not self.items:
                return None
            return max(self.items, key=lambda item: item['value'])

        def sort_by_value(self):
            # вернуть предметы, отсортированные по стоимости
            return sorted(self.items, key=lambda item: item['value'])

        def sort_by_weight(self):
            # вернуть предметы, отсортированные по весу
            return sorted(self.items, key=lambda item: item['weight'])

    # Задание 8. Класс «Тренажёрный зал»
    class Gym(object):
        def __init__(self, name: str):
            # название зала, список клиентов (имя, возраст, абонемент активен/не
            # активен)
            self.name = name
            self.clients = []

        def add_client(self, name: str, age: int):
            # добавить клиента
            self.clients.append({'name': name, 'age': age, 'active': False})

        def remove_client(self, name: str):
            # удалить клиента
            for client in self.clients:
                if client['name'] == name:
                    self.clients.remove(client)
                    break

        def activate_membership(self, name: str):
            # активировать абонемент клиента
            for client in self.clients:
                if client['name'] == name:
                    client['active'] = True
                    break

        def deactivate_membership(self, name: str):
            # деактивировать абонемент
            for client in self.clients:
                if client['name'] == name:
                    client['active'] = False
                    break

        def get_active_members(self):
            # вернуть список клиентов с активным абонементом
            return [client for client in self.clients if client['active'] == True]

        def find_youngest_client(self):
            # вернуть самого молодого клиента
            if not self.clients:
                return None
            return min(self.clients, key=lambda client: client['age'])

        def find_oldest_client(self):
            # вернуть самого старшего клиента
            if not self.clients:
                return None
            return max(self.clients, key=lambda client: client['age'])

        def average_age(self):
            # средний возраст клиентов
            if not self.clients:
                return 0
            return sum(client['age'] for client in self.clients) / len(self.clients)

        def __str__(self):
            lines = [f'Тренажерный зал: {self.name}, Клиенты: ']
            if not self.clients:
                lines.append('Нет клиентов')
            else:
                for client in self.clients:
                    status = 'активен' if client['active'] == True else 'неактивен'
                    lines.append(f'{client["name"]}, {client["age"]} лет - абонемент: {status}')
                    return '\n'.join(lines)

# Задание 9. Класс «Музыкальный плейлист»

class Playlist(object):
    def __init__(self, playlist_name: str):
        self.playlist_name = playlist_name
        self.tracks = []

    def add_track(self, name:str, artist:str, duration:float):
        # добавить трек
        self.tracks.append({'name': name, 'artist': artist, 'duration': duration})

    def remove_track(self, name:str):
        # удалить трек
        for track in self.tracks:
            if track['name'] == name:
                self.tracks.remove(track)
                break
    def total_duration(self):
        # общая длительность всех треков
        return sum(track['duration'] for track in self.tracks)
    def find_by_artist(self, artist: str):
        # найти все треки исполнителя
        return [track for track in self.tracks if track['artist'] == artist]
    def longest_track(self):
        # найти самый длинный трек
        return max(self.tracks, key = lambda track: track['duration'])
    def shortest_track(self):
        # найти самый короткий трек
        return min(self.tracks, key = lambda track: track['duration'])
    def shuffle(self):
        # перемешать треки в случайном порядке
        random.shuffle(self.tracks)
    def sort_by_duration(self, reverse: bool = False):
        # сортировать треки по длительности
        return sorted(self.tracks, key=lambda track: track['duration'], reverse=reverse)
# Задание 10. Класс «Учебная группа»
class Student(object):
    def __init__(self, name: str):
        self.name = name
        self.grades = []
    def add_grade(self, grade:int):
        # добавить оценку
        self.grades.append(grade)
    def average_grade(self):
        # вернуть среднюю оценку
        if not self.grades:
            return 0
        return sum(self.grades) / len(self.grades)
    def info(self):
        # вывести информацию об ученике
        avg = self.average_grade()
        return f'Ученик: {self.name}, оценки: {self.grades}, средний бал: {avg:2f}'

class StudyGroup(object):
    def __init__(self, name: str):
        self.name = name
        self.students = []
    def add_student(self, student: Student):
        # добавить ученика
        self.students.append(student)
    def remove_student(self, name:str):
        # удалить ученика по имени
        for student in self.students:
            if student.name == name:
                self.students.remove(student)
                break
    def find_best_student(self):
        # найти ученика с лучшей средней оценкой
        if not self.students:
            return None
        return max(self.students, key=lambda student: student.average_grade())

    def group_average(self):
        # средняя оценка по группе
        if not self.students:
            return None
        return sum(student.average_grade() for student in self.students) / len(self.students)

    def list_students(self):
        # вывести список всех студентов
        return [student.info() for student in self.students]






