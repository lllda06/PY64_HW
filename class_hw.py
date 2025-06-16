
#                   ООП ЗАДАНИЕ 1.pdf

# Задание 1
class Soda:
    def __init__(self, addition=None):
        if isinstance(addition, str):
            self.addition = addition
        else:
            self.addition = None
    def show_my_drink(self):
        if self.addition:
            print(f"Газировка и {self.addition}")
        else:
            print("Обычная газировка")

drink_with_addition = Soda("cola")
drink_with_addition.show_my_drink()

drink_without_addition = Soda()
drink_without_addition.show_my_drink()

# Задание 2
class TriangleChecker:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c
    def is_triangle(self):
        if not isinstance(self.a, (int, float)) or \
                not isinstance(self.b, (int, float)) or \
                not isinstance(self.c, (int, float)):
            return "Нужно вводить только числа!"
        if self.a <= 0 or self.b <= 0 or self.c <= 0:
            return "С отрицательными числами ничего не выйдет!"
        if (self.a + self.b > self.c and
                self.a + self.c > self.b and
                self.b + self.c > self.a):
            return "Ура, можно построить треугольник!"
        else:
            return "Жаль, но из этого треугольник не сделать"

triangle1 = TriangleChecker(7,2,6)
print(triangle1.is_triangle())

triangle2 = TriangleChecker(0,2,6)
print(triangle2.is_triangle())

# Задание 3
# ВЕРСИЯ БЕЗ @PROPERTY
class KgToPounds:
    def __init__(self, kilogram):
        if isinstance(kilogram, (int, float)):
            self.__kilogram = kilogram
        else:
            raise ValueError("Вес передаем только числами!")
    def to_pounds(self):
        return self.__kilogram * 2.205
    def set_kilogram(self, value):
        if isinstance(value, (int, float)):
            self.__kilogram = value
        else:
            print("Вес передаем только числами!")
    def get_kilogram(self):
        return self.__kilogram

obj1 = KgToPounds(20)
print(obj1.to_pounds())
obj1.set_kilogram(15)
print(obj1.get_kilogram())

# ВЕРСИЯ C @PROPERTY

class KgToPounds:
    def __init__(self, kilogram):
        self.__kilogram = kilogram
    @property
    def kilogram(self):
        return self.__kilogram
    @kilogram.setter
    def kilogram(self, value):
        if isinstance(value, (int, float)):
            self.__kilogram = value
        else:
            print("Вес передаем только числами!")
    def to_pounds(self):
        return self.__kilogram * 2.205

obj2 = KgToPounds(10)
print(obj2.to_pounds())
obj2.kilogram = 20
print(obj2.kilogram)

# Задание 4
class RealString:
    def __init__(self, string):
        if not isinstance(string, str):
            raise TypeError("Передаем только строки")
        self.__string = string

    def __len__(self):
        return len(self.__string)

    def __str__(self):
        return self.__string

    def __eq__(self, other):
        return len(self) == self._get_length(other)

    def __ne__(self, other):
        return len(self) != self._get_length(other)

    def __lt__(self, other):
        return len(self) < self._get_length(other)

    def __le__(self, other):
        return len(self) <= self._get_length(other)

    def __gt__(self, other):
        return len(self) > self._get_length(other)

    def __ge__(self, other):
        return len(self) >= self._get_length(other)

    def _get_length(self, other):
        if isinstance(other, RealString):
            return len(other)
        elif isinstance(other, str):
            return len(other)
        else:
            raise TypeError("Сравнение возможно только со строкой или обьектом realstring")

a = RealString("Apple")
b = RealString("Яблоко")

print(a==b)
print(a!=b)
print(a>b)
print(a>=b)
print(a<b)
print(a<=b)

# Задание 5
class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height
    def __str__(self):
        return f"Прямоугольник с шириной {self.width} и высотой {self.height}"
    def get_area(self):
        return self.width * self.height
    def get_perimeter(self):
        return 2 * self.width + 2 * self.height
    @property
    def is_square(self):
        return self.width == self.height

r1 = Rectangle(5,10)
print(r1)
print(r1.get_area())
print(r1.get_perimeter())
print(r1.is_square)

# Задание 6

class Person:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = int(age)
        self.gender = gender
    def __str__(self):
        return f"Имя: {self.name}, Возраст: {self.age}, Пол: {self.gender}."
    @property
    def get_name(self):
        return self.name
    def set_name(self, new_name):
        if isinstance(new_name, str):
            self.name = new_name
        else:
            raise ValueError("Имя должно быть строкой")
    @staticmethod
    def is_adult(age):
        return age >= 18
    @classmethod
    def create_from_string(cls, s):
        name, age, gender = s.split("-")
        return cls(name, int(age), gender)

p1 = Person("Анна", 30, "женский")
print(p1.name)
p1.name = "Ольга"
print(p1.name)
print(Person.is_adult(13))
print(p1)

# ----------------------------------------------------------

#                   ООП ЗАДАНИЕ 2.pdf
# МАТРИЦЫ
class Matrix:
    def __init__(self, values: list[list[int]]) -> None:
        self.values = values
        self.rows = len(values)
        self.cols = len(values[0]) if values else 0

        for row in values:
            if len(row) != self.cols:
                raise ValueError("Все строки должны быть одинаковой длины")
    def __str__(self) -> str:
        return '\n'.join(['\t'.join(map(str, row)) for row in self.values])
    def __hash__(self) -> int:
        return hash(tuple(tuple(row) for row in self.values))
    def __eq__(self, other: any) -> bool:
        return isinstance(other, Matrix) and self.values == other.values
    def size(self) -> tuple[int, int]:
        return (self.rows, self.cols)
    def count(self) -> int:
        return self.rows * self.cols
    def total(self) -> int:
        return sum(sum(row) for row in self.values)

    def __add__(self, other: "Matrix") -> "Matrix":
        if self.size() != other.size():
            raise ValueError("Размеры матриц не совпадают")
        result = [
            [self.values[i][j] + other.values[i][j] for j in range(self.cols)]
            for i in range(self.rows)
        ]
        return Matrix(result)
    def __sub__(self, other: "Matrix") -> "Matrix":
        if self.size() != other.size():
            raise ValueError("Размеры матриц не совпадают")
        result = [
            [self.values[i][j] - other.values[i][j] for j in range(self.cols)]
            for i in range(self.rows)
        ]
        return Matrix(result)
    def __mul__(self, scalar: int) -> "Matrix":
        result = [[value * scalar for value in row] for row in self.values]
        return Matrix(result)
    def transpose(self) -> "Matrix":
        transposed = [[self.values[j][i] for j in range(self.rows)] for i in range(self.cols)]
        return Matrix(transposed)
    def without_negatives(self) -> "Matrix":
        result = [[max(0, value) for value in row] for row in self.values]
        return Matrix(result)

    @classmethod
    def identity(cls, m: int, n: int) -> "Matrix":
        return cls([[1 if i == j else 0 for j in range(n)] for i in range(m)])

    @classmethod
    def zeros(cls, m: int, n: int) -> "Matrix":
        return cls([[0 for _ in range(n)] for _ in range(m)])

    @classmethod
    def diagonal(cls, values: list[int]) -> "Matrix":
        size = len(values)
        return cls([[values[i] if i == j else 0 for j in range(size)] for i in range(size)])

