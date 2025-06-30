from database import session_maker, init_db
from models import Users, Products, Tickets, Orders
import uuid

current_user = None  # глобальная переменная для авторизации


def main_menu():
    global current_user
    print("""
     === Добро пожаловать в "Не магазин" ===

Здесь вы можете обменивать тикеты для того, чтобы приобретать товары.

Для взаимодействия используйте команды:
    """)

    if current_user:
        print(
        """
> Товары
> Купить <id> <количество>
> Тикет <uuid>
> Профиль
> Выход
        """)
    else:
        print(
        """
> Товары
> Зарегистрироваться
> Войти
> Выход
        """)


def list_products(session):
    products = session.query(Products).filter(Products.count > 0).all()
    print(f"| {'ID':<10} {'Цена':<10} {'Кол-во':<10} {'Название':<15} |")
    print("=" * 52)
    for p in products:
        print(f"| {p.id:<10} {p.cost:<10} {p.count:<10} {p.name:<15} |")


def register(session):
    global current_user
    username = input("Введите логин: ")
    password = input("Введите пароль: ")
    if Users.is_exists(session, username):
        print("Пользователь уже существует!")
    else:
        user = Users(username=username, password=password)
        session.add(user)
        session.commit()
        current_user = user
        print("Регистрация успешна!")


def login(session):
    global current_user
    username = input("Введите логин: ")
    password = input("Введите пароль: ")
    user = session.query(Users).filter_by(username=username, password=password).first()
    if user:
        current_user = user
        print("Вход выполнен.")
    else:
        print("Неверный логин или пароль.")


def use_ticket(session, uuid_str):
    global current_user
    if not current_user:
        print("Сначала войдите в систему")
        return
    if Tickets.valid_ticket(session, uuid_str):
        ticket = session.query(Tickets).filter_by(uuid=uuid_str).first()
        ticket.available = False
        ticket.user_id = current_user.id
        current_user.points += 20
        session.commit()
        print("Тикет успешно активирован. +20 поинтов")
    else:
        print("Тикет недействителен или уже использован.")


def buy_product(session, args):
    global current_user
    if not current_user:
        print("Сначала войдите в систему")
        return
    if len(args) != 3:
        print("Формат: Купить <id> <кол-во>")
        return
    try:
        product_id = int(args[1])
        quantity = int(args[2])
        product = session.query(Products).filter_by(id=product_id).first()
        if not product or product.count < quantity:
            print("Недостаточно товара.")
            return
        total = quantity * product.cost
        if current_user.points < total:
            print("Недостаточно поинтов.")
            return
        order = Orders(user_id=current_user.id, product_id=product.id, count=quantity)
        product.count -= quantity
        current_user.points -= total
        session.add(order)
        session.commit()
        print("Покупка успешна!")
    except ValueError:
        print("Неверный формат.")


def show_profile(session):
    global current_user
    if not current_user:
        print("Сначала войдите в систему")
        return
    print(f"\nПрофиль: {current_user.username}")
    print(f"Поинты: {current_user.points}")
    print("Покупки:")
    for order in current_user.get_orders(session):
        product_name = order.product.name if order.product else "Неизвестно"
        print(f"Товар: {product_name}, Количество: {order.count}")


def run():
    init_db()
    session = session_maker()
    try:
        while True:
            main_menu()
            command = input("Введите команду: ").strip()
            if command.lower() == "выход":
                break
            elif command.lower() == "товары":
                list_products(session)
            elif command.lower() == "зарегистрироваться":
                register(session)
            elif command.lower() == "войти":
                login(session)
            elif current_user:
                if command.lower().startswith("купить "):
                    buy_product(session, command.split())
                elif command.lower().startswith("тикет "):
                    parts = command.split()
                    if len(parts) < 2:
                        print("Формат: Тикет <uuid>")
                    else:
                        uuid_str = parts[1]
                        use_ticket(session, uuid_str)
                elif command.lower() == "профиль":
                    show_profile(session)
            else:
                print("Неизвестная команда.")
    finally:
        session.close()


if __name__ == "__main__":
    run()


