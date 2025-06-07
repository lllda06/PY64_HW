# Задание 1

list1 = [1, 2, 3, 4, 5]
list2 = list(filter(lambda x: x%2==0, list1))
print(list2)

#Задание 2

people = [("Иван", 25), ("Мария", 17), ("Алексей", 50)]
new_people = sorted(people, key= lambda x: x[1])
print(new_people)

#Задание 3

words = ["привет", "арбуз", "бутылка", "очки", "мышка", "энциклопедия"]
vowels = "аеёиоуыэюяAEIOUYaeiouy"
words2 = list(filter(lambda x:x[0].lower() in vowels, words))
print(words2)

#Задание 4

list1 = [1,2,3,4,5]
list2 = list(map(lambda x:x**2,list1))
print(list2)

# Задание 5

words = ["привет", "арбуз", "бутылка", "очки", "мышка", "энциклопедия"]
new_words = list(sorted(words, key = lambda x:len(x), reverse=True))
print(new_words)

# Задание 6

sentence1 = "hello world how are you"
letters_python = list(filter(lambda x:x.lower() in "python", sentence1))
print(letters_python)

# Задание 7

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
def number_multiply_ten(x):
    return x * 10
new_numbers = list(map(number_multiply_ten, numbers))
print(new_numbers)

# Задание 8

list_of_words = ['computer', 'keyboard', 'phone', 'clock', 'apple']
new_list_of_words = list(sorted(list_of_words))
print(new_list_of_words)

# Задание 9

words = ["apple","madam", "Python", "hello", "notebook", "orange", "table"]
def words_pallindrom (words):
    return list(filter(lambda x:x.lower() == x.lower()[::-1],words))
print(words_pallindrom(words))

# Задание 10

words = ["apple","madam", "sun", "hello","fun", "notebook", "orange", "table"]
def count_vowels(word):
    vowels = "аеёиоуыэюяAEIOUYaeiouy"
    count = 0
    for letter in word:
        if letter in vowels:
            count += 1
    return count

print(sorted(words, key=lambda x: count_vowels(x)))
# -----------------------------------------------------
def count_vowels(words):
    vowels = "аеёиоуыэюяAEIOUYaeiouy"
    return sorted(words, key = lambda x: sum(1 for letter in x.lower() if letter in vowels))
print(count_vowels(words))

# Задание 11

words_list = ['hello', 'morning', 'bye', 'night']
print(list(map(lambda x:x.upper(), words_list)))

# Задание 12

name_list = ['Вася', 'Петя', 'Маша']
print(list(map(lambda x:"Hello"+x, name_list)))

# Задание 13

list_words = ['ананас', 'сок', 'авокадо', 'автомобиль']
print( list(sorted(list_words, key = lambda x:sum( 1 for letter in x.lower() if letter in 'а'))))

# ----------------------------------------------------------------------------

list_words = ['ананас', 'сок', 'авокадо', 'автомобиль']
print("Задание 13")
print(list(sorted(list_words, key = lambda x: x.lower().count('а'))))
# Задание 14

words3 = ['мама', 'папа', 'молоко', 'программа', 'мм']
print(list(sorted(words3, key = lambda x: len(set(x.lower())))))

# Задание 15

# def my_decorator(func):
#     def wrapper():
#         print("Запуск функции")
#         res = func()
#         print("Функция завершается")
#         return res
#     return wrapper
#     @my_decorator
#     def my_function():
#         print("Внутри функции")
#
#     print(my_function())
#

def retry_five(func):
    def wrapper(*args, **kwargs):
        print("Запуск функции")
        results = []
        for i in range(5):
            print(f"Вызов #{i+1}:")
            result = func(*args, **kwargs)
            results.append(result)
        print("Функция завершилась")
        return results
    return wrapper


@retry_five
def greed(name):
    print(f"Привет, {name}")

print(greed("Лада"))