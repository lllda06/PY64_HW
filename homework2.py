# Задание 1
from random import randint

list1 = ['apple', 'banana', 'cherry']

# Через цикл вывести в консоль все элементы списка.
for item in list1:
    print("Элементы списка: ", item)

# Используя цикл, вывести в консоль все элементы списка в обратном порядке.
for item in list1[::-1]:
    print("В обратном порядке: ", item)

# Используя цикл, вывести в консоль все элементы списка, а их буквы в обратном порядке.
for item in list1:
    print("Буквы в обратном порядке: ", item[::-1])

# Задание 2

dict1 = {
    "name": "John",
    "age": 30,
    "city": "New York"
}

# Используя цикл, вывести в консоль все ключи словаря.
for key in dict1:
    print("Ключи: ", key)

# Используя цикл, вывести в консоль все ключи и значения словаря.
for key, value in dict1.items():
    print("Ключ: ", key,"; Значение: ", value)

# Задание 3
# На вход пользователь вводит целое число (использовать функцию input).
number = int(input("Введите целое число: "))
# Используя цикл, вывести в консоль все числа от 1 до введенного числа включительно.
print("все числа от 1 до введенного числа включительно")
for i in range(1,number+1):
    print(i)
# Используя цикл, вывести в консоль все числа от введенного числа до 1 включительно.
print("все числа от введенного числа до 1 включительно")
for i in range(number, 0,-1):
    print(i)
# Используя цикл, вывести в консоль все числа от 1 до введенного числа включительно, которые делятся на 3 без остатка.
print("все числа от 1 до введенного числа включительно, которые делятся на 3 без остатка")
for i in range(1,number+1, 1):
    if i % 3 == 0:
        print(i)

# Задание 4

# На вход пользователь вводит предложение (использовать функцию input).
sentence = str(input("Введите предложение: "))

# Посчитайте количество слов в предложении и выведите результат в консоль.
print("Количество слов в предложении: ", len(sentence.split()))

# Используя цикл, выведите в консоль все слова предложения в обратном порядке.
for word in sentence.split()[::-1]:
    print(word)

# Используя цикл, создайте словарь, где ключами являются длина слов,
# а значениями - список слов в предложении с такой длиной.

words = sentence.split()

sentence_dict = {}

for word in words:
    length = len(word)
    if length not in sentence_dict:
        sentence_dict[length] = []
    sentence_dict[length].append(word)
for length, word_list in sentence_dict.items():
    print(f"{length}:{word_list}")

# Задание 5

# На вход пользователь должен ввести username, email, имя и фамилию по очереди (использовать функцию input).
# Для каждого параметра: если введенные данные не соответствуют требованиям
# (например, username должен быть длиной от 3 до 20 символов)
# выведите сообщение об ошибке и попросите ввести данные заново.
while True:
    username = input("Введи ник: ")
    if len(username) >= 3 and len(username) < 20:
        break
    else:
        print("Ошибка: username должен быть от 3 до 20 символов")
while True:
    email = input("Введи электронную почту: ")
    if "@" in email and "." in email and len(email) >= 5:
        break
    else:
        print("Ошибка: некорректный email")
while True:
    name = input("Введи имя: ")
    if isinstance(name, str) and len(name) > 2:
        break
    else:
        print("Ошибка: имя должно иметь тип string и быть не короче 2 символов")
while True:
    surname = input("Введи фамилию: ")
    if isinstance(surname, str) and len(surname) > 2:
        break
    else:
        print("Ошибка: фамилия должна иметь тип string и быть не короче 2 символов")

# Создайте словарь с данными пользователя и выведите его в консоль
dict = {
    "username":username,
    "email":email,
    "name":name,
    "surname":surname
}
print(dict)

# Задание 6*

import random

# Напишите в коде случайное число от 1 до 100.
num = random.randint(1, 100)

print("Я загадала число от 1 до 100, твоя задача угадать число")

# Пользователь должен угадать это число.
# Используя цикл, попросите пользователя ввести число до тех пор, пока он не угадает.
while True:
    guess = input("Твой вариант: ")

    # Если пользователь ввел не число, выведите сообщение "Вы ввели не число".
    if not guess.isdigit():
        print("Вы ввели не число")
        continue

    guess = int(guess)

    # Если пользователь ввел число, которое не попало в диапазон от 1 до 100, выведите сообщение "Число не входит в диапазон от 1 до 100".
    if guess < 1 or guess > 100:
        print("Число не входит в диапазон от 1 до 100")
        continue

    # Если пользователь ввел число больше загаданного, выведите сообщение "Загаданное число меньше".
    if guess > num:
        print("Загаданное число меньше")
    # Если пользователь ввел число меньше загаданного, выведите сообщение "Загаданное число больше".
    elif guess < num:
        print("Загаданное число больше")
    # Если пользователь угадал число, выведите сообщение "Вы угадали!" и завершите программу.
    else:
        print("Вы угадали!")
        break


# Задание 7*
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

# Используя цикл, выведите все активности по логам пользователя в консоль со временем и описанием.

for log in user1["activityLogs"]:
    print("Время:", log["timestamp"], "; Описание:", log["activity"])

# Если пользователь активен, выведите сообщение "Пользователь активен", иначе выведите "Пользователь не активен".

    if user1["accountStatus"]["isActive"]:
        print("Пользователь активен")
    else:
        print("Пользователь не активен")

# Если у пользователя есть аватар, то выведите его в консоль, если нет, то выведите "Нет аватара".

if "avatarUrl" in user1["profile"] and user1["profile"]["avatarUrl"]:
    print(user1["profile"]["avatarUrl"])
else:
    print("Нет аватара")


# Задание 8*

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
        "quantity": 0
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
            "price": 198.99,
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

# Сейчас кол-во товара на складе равно 0. Посчитайте кол-во исходя из вариантов товара на складе.


for variant in product1["variants"]:
    product1["stock"]["quantity"] += variant["stockQuantity"]


print((product1)["stock"]["quantity"])

# Выведите через цикл все варианты товара на складе в виде строки в формате: "Название - цена (кол-во на складе)".
for i in product1["variants"]:
    name = i["variantId"]
    price = i["price"]
    stock = i["stockQuantity"]
    print("Название - ", name,"; Цена - ", price," (кол-во на складе - ", stock, ")")

# Используя цикл, найдите вариант товара с максимальной ценой и выведите его название и цену в консоль.
max_price = 0
max_name = ""
for i in product1["variants"]:
    if i["price"] > max_price:
        max_price = i["price"]
        max_name = i["variantId"]

print("Название - ", max_name, "; цена - ", max_price)

# Выведите через цикл все отзывы о товаре в виде строки в формате: "Пользователь - Оценка - Комментарий".
for i in product1["reviews"]:
    username = i["username"]
    rating = i["rating"]
    comment = i["comment"]
    print("Пользователь: ", username, " - Оценка: ", rating, " - Комментарий: ",comment)

# Посчитайте через цикл количество отзывов с оценкой 5 и выведите их количество в консоль.
rating_five = 5
count_rating_five = 0
for review in product1["reviews"]:
    if review["rating"] == rating_five:
        count_rating_five += 1
print(count_rating_five)

# Через цикл выведите только названия файлов картинок (например, "main.jpg" и "side.jpg") товара в консоль.
for image in product1["images"]:
    file_name = image.split("/")[-1]
    print(file_name)

# Используя цикл, найдите и выведите в консоль все отзывы пользователя с именем "techguy123".
for i in product1["reviews"]:
    if i["username"] == "techguy123":
        print(i)