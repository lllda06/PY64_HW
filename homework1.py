# Сумма трех чисел
import math
from itertools import count

a = 1
b = 2
c = 3
print("Сумма переменных a, b, c: ", a+b+c)
# второй способ с использованием input
a2 = int(input("Введите первое число: "))
b2 = int(input("Введите второе число: "))
c2 = int(input("Введите третье число: "))
print(f"Сумма трех чисел {a}, {b} и {c} = {a+b+c}")

# Следующее и предыдущее
number = 10
print("Следующее за числом 10 число: ", number+1)
print("Для числа 10 предыдущее число: ", number-1)
# второй способ использованием input
number2 = int(input("введите число: "))
print(f"Для числа {number2} предыдущее число: {number2-1}")
print(f"Следующее за числом {number2} число: : {number2+1}")

# Расстояние в метрах
distans_centimeter = 3561
distans_meter = distans_centimeter // 100
print(distans_meter, " метров")
# второй способ в линию с использованием input
print(int(input("введите расстояние в см: "))//100, "метров")

# Пересчет временного интервала
min = int(input("введи сколько минут"))
hour = min // 60
min2 = min - hour*60
print(f"{min} мин - это {hour} час(a) и {min2} минут")

# второй способ

min3 = int(input("введи сколько минут"))
print(f"{min3} мин - это {min3 // 60} час(а) {min3 - (min3 // 60)*60} минут")

# Трехзначное число
num = 132
num1 = num // 100          # сотни
num2 = (num // 10) % 10    # десятки
num3 = num % 10            # единицы
print(num1)
print("Сумма цифр = ", num1 + num2 + num3)
print("Произведение цифр = ", num1 * num2 * num3)

# второй способ:
numm = int(input("введите трехзначное число: "))
print(f"сумма цифр вашего трехзначного числа: {numm // 100 + (numm // 10) % 10 + numm % 10},\n а произведение цифр = {(numm // 100) * ((numm // 10) % 10) * (numm % 10)}")

# Четное или нечетное?

if_numbers = input("Введите трехзначное число: ")
if len(if_numbers) == 3:
    if_number = int(if_numbers)
    if (if_number % 2==0) :
        print("Четное")
    else:
        print("Нечетное")
else:
    print("ошибка")

# Квадрат

side = int(input("введи сторону квадрата: "))
print("Периметр равен: ", side*4)
print("Площадь равна: ", side**2)
print("Диагональ квадрата равна: ", side*math.sqrt(2))

# СПИСКИ

#1
list = [1, "Hello", True]
print(list)

# 2
list.append("Wie geht es dir")
print(list)

# 3
list.insert(0, 2)
print(list)

#4
list.append([True, "Bye", False])
print(list)

# 5
list.insert(1, (6,7,8,True))
print(list)

# 6
print(list[0])

# 7
del list[0]
print(list)

# СЛОВАРИ

# 1
phone = {
    "фирма": "apple",
    "модель": "iphone 15",
    "цвет" : "black",
    "аккумулятор" : 81,
    "память" : 256,
    "состояние" : "б/y"
}
print(phone)

# 2
phone["хозяин"] = True
print(phone)

# 3
key = ("имя хозяина", "фамилия хозяина", "номер телефона")
phone[key] = ["Петр", "Пупкин", "+375291111111"]
print(phone)

# 4
print(phone["память"])
print("имя хозяина: ", phone[key][0])

# Задание 1

# Имеется структура данных пользователя.

user1 = {
    "userId": 2,
    "username": "janedoe",
    "email": "janedoe@example.com",
    "profile": {
        "firstName": "Jane",
        "lastName": "Doe",
        "birthDate": "1992-04-12",
        "gender": "female",
        "avatarUrl": "https://example.com/avatars/janedoe.jpg",
        "bio": "Digital marketer and blogger."
    },
    "preferences": {
        "language": "fr",
        "theme": "light",
        "notifications": {
            "email": False,
            "sms": True,
            "push": True
        },
        "privacy": {
            "showOnlineStatus": True,
            "profileVisibility": "public"
        }
    },
    "accountStatus": {
        "isActive": True,
        "lastLogin": "2025-01-10T09:15:00Z",
        "createdAt": "2023-03-20T11:00:00Z"
    },
    "activityLogs": [
        {
            "timestamp": "2025-01-09T18:30:00Z",
            "activity": "Commented on a post"
        },
        {
            "timestamp": "2025-01-08T16:45:00Z",
            "activity": "Liked a post"
        }
    ]
}

# Уменьшите день рождения пользователя на 1 день.

import datetime

birth_date = user1["profile"]["birthDate"]
birth_date_dt = datetime.datetime.strptime(birth_date, "%Y-%m-%d")

new_birth_date = birth_date_dt - datetime.timedelta(days=1)
user1["profile"]["birthDate"] = new_birth_date.strftime("%Y-%m-%d")

print(user1["profile"])

# Измените язык пользователя на "ru".

new_lang = user1["preferences"]["language"]
new_lang = "ru"
user1["preferences"]["language"] = new_lang
print(user1["preferences"])

# Измените тему на "dark".

new_theme = user1["preferences"]["theme"]
new_theme = "dark"
user1["preferences"]["theme"] = new_theme
print(user1["preferences"])


# Измените статус активности на "false".

new_status = user1["accountStatus"]["isActive"]
new_status = False
user1["accountStatus"]["isActive"] = new_status
print(user1["accountStatus"])

# Добавьте новую запись в историю активности пользователя.

new_activity = user1["activityLogs"]
new_activity = {
            "timestamp": "2020-01-09T11:00:00Z",
            "activity": "Followed"
        }
user1["activityLogs"].append(new_activity)
print(user1["activityLogs"])

# Задание 2

# Имеется структура данных продукта.


product1 = {
    "productId": 1001,
    "productName": "Wireless Headphones",
    "description": "Noise-cancelling wireless headphones with Bluetooth 5.0 and 20-hour battery life.",
    "brand": "SoundPro",
    "category": "Electronics",
    "price": 199.99,
    "currency": "USD",
    "stock": {
        "available": True,
        "quantity": 50
    },
    "images": [
        "https://example.com/products/1001/main.jpg",
        "https://example.com/products/1001/side.jpg"
    ],
    "variants": [
        {
            "variantId": "1001_01",
            "color": "Black",
            "price": 199.99,
            "stockQuantity": 20
        },
        {
            "variantId": "1001_02",
            "color": "White",
            "price": 199.99,
            "stockQuantity": 30
        }
    ],
    "dimensions": {
        "weight": "0.5kg",
        "width": "18cm",
        "height": "20cm",
        "depth": "8cm"
    },
    "ratings": {
        "averageRating": 4.7,
        "numberOfReviews": 2
    },
    "reviews": [
        {
            "reviewId": 501,
            "userId": 101,
            "username": "techguy123",
            "rating": 5,
            "comment": "Amazing sound quality and battery life!"
        },
        {
            "reviewId": 502,
            "userId": 102,
            "username": "jane_doe",
            "rating": 4,
            "comment": "Great headphones but a bit pricey."
        }
    ]
}

# Уменьшите цену товара на 10%.

new_price = round(product1["price"]*0.9, 3)
product1["price"] = new_price
print(product1)

# Уменьшите количество единиц товара черного цвета на 7 (не забудьте пересчитать общее количество единиц).

product1["variants"][0]["stockQuantity"] -= 7
product1["stock"]["quantity"] -= 7
print(product1["variants"])
print("общее кол-во на складе = ", product1["stock"]["quantity"])

# Добавьте изображение товара.
product1["images"].append("https://example.com/products/1001/new_image.jpg")
print(product1["images"])

# Добавьте review для товара с рейтингом 2.

new_review = product1["reviews"]
new_review =   {
            "reviewId": 503,
            "userId": 103,
            "username": "lllda06",
            "rating": 2,
            "comment": "Low quality but very cheap!"
        }
product1["reviews"].append(new_review)
print(product1["reviews"])

# Пересчитайте среднюю оценку товара и количество отзывов.

count_review = len(product1["reviews"])
print("Количество отзывов: ",count_review)

total_rating = sum(review["rating"] for review in product1["reviews"])
avg_review = round(total_rating / count_review, 2)

print("Средняя оценка товара: ",avg_review)