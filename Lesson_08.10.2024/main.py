# Задача 1: Класс для работы с книгами
#
# Описание: Создайте класс Book, который будет содержать информацию о книге (название, автор, год издания).
# Создайте методы для отображения информации о книге и для изменения года издания.
#
# Условия:
#
#  • Создайте конструктор, который будет принимать название, автора и год.
#  • Добавьте метод get_info(), который будет выводить информацию о книге.
#  • Добавьте метод для изменения года издания.
import math
from abc import abstractmethod


# class Book:
# 	def __init__(self, name: str, author: str, year: int):
# 		self.name: str = name
# 		self.author: str = author
# 		self.year: int = year
#
# 	def get_info(self):
# 		print(self)
#
# 	def set_year(self, new_year):
# 		self.year = new_year
# 		return self.year
#
# 	def __str__(self):
# 		return f"{self.name} by {self.author}, {self.year}"
#
#
# book = Book('Game of thrones', 'Martin', 2012)
# book.get_info()
# book.set_year(2023)
# book.get_info()


# Задача 2: Класс для банковского счета
#
# Описание: Создайте класс BankAccount, который будет моделировать банковский счёт.
# В классе должны быть методы для пополнения счёта, снятия денег и вывода текущего баланса.
#
# Условия:
#
#  • Конструктор должен принимать начальный баланс.
#  • Метод deposit(amount) для пополнения счёта.
#  • Метод withdraw(amount) для снятия средств (не должно быть возможности уйти в минус).
#  • Метод get_balance() для отображения текущего баланса.

# class BankAccount:
#
# 	def __init__(self, balance: int):
# 		if balance < 0:
# 			raise ValueError('Баланс не может быть меньше нуля')
# 		self.__balance: int = balance
#
# 	def deposit(self, amount: int):
# 		if amount < 0:
# 			raise ValueError('Депозит не может быть отрицательным')
# 		self.__balance += amount
#
# 	def withdraw(self, amount: int):
# 		if 0 < amount >= self.__balance:
# 			raise ValueError('Число не может быть отрицательным и нельзя снять больше чем у тебя есть, хитрец')
# 		self.__balance -= amount
#
# 	def get_balance(self):
# 		return self.__balance
#
# 	def	__str__(self):
# 		return f'Текущий баланс равен - {self.__balance}'
#
#
# balance = BankAccount(250000)
# balance.get_balance()
# balance.deposit(350000)
# balance.get_balance()
# balance.withdraw(333333)
# balance.get_balance()

# Задача 3: Наследование
#
# Описание: Создайте класс Person, который будет хранить информацию о человеке (имя и возраст),
# и класс Student, который наследуется от Person. В классе Student должны быть добавлены поля для
# хранения учебного заведения и среднего балла.
#
# Условия:
#
#  • Конструктор класса Person должен принимать имя и возраст.
#  • Конструктор класса Student должен дополнительно принимать учебное заведение и средний балл.
#  • Добавьте методы для отображения информации о студенте.

# class Person:
#
# 	def __init__(self, name: str, age: int):
# 		self._name: str = name
# 		self._age: int = age
#
# 	def __str__(self):
# 		return f'Человек с именем - {self._name} и возрастом - {self._age}'
#
#
# class Student(Person):
# 	def	__init__(self, name: str, age: int, institution: str, average_score: float):
# 		super().__init__(name, age)
# 		self._institution: str = institution
# 		self._average_score: float = average_score
#
# 	def __str__(self):
# 		return super().__str__() + f' это студент в вузе - {self._institution} со средним баллом - {self._average_score}'
#
#
# a = Student('Pasha-Techik', 32, 'YouTube', 1.5)
# print(a)

# Задача 4: Полиморфизм

# Описание: Создайте классы Rectangle и Circle.
# Оба класса должны иметь метод get_area(), который возвращает площадь фигуры.
# Реализуйте механизм полиморфизма, который позволяет вызвать метод get_area() для объекта любого класса.
#
# Условия:
#
#  • Класс Rectangle должен принимать длину и ширину, а класс Circle — радиус.
#  • Метод get_area() должен возвращать площадь фигуры.





class Figure:

	@abstractmethod
	def get_area(self):
		raise NotImplementedError('Необходимо ввести метод get_area')

class Rectangle(Figure):
	def __init__(self, side: int):
		self.__side: int = side

	def get_area(self):
		area = self.__side ** 2
		return area

	def __str__(self):
		return f'Квадрат со стороной - {self.__side} и площадью - {Rectangle.get_area(self)}'


class Circle(Figure):
	def __init__(self, radius: int):
		self.__radius: int = radius

	def get_area(self):
		area = math.pi * self.__radius ** 2
		return area

	def __str__(self):
		return f'Круг радиусом - {self.__radius} и площадью - {Circle.get_area(self)}'


rectangle = Rectangle(4)
rectangle.get_area()
print(rectangle)
circle = Circle(4)
circle.get_area()
print(circle)

