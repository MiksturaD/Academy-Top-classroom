
# Задание 1
# Создайте класс Число (или используйте уже ранее
# созданный вами). Класс число хранит внутри одно
# значение. Используя перегрузку операторов реализуйте
# для него арифметические операции для работы с числом
# (операции +, -, *, /).
from __future__ import annotations
#
#
# class Number:
#
# 	def __init__(self, value: int | float):
# 		self.__value: int | float = value
#
# 	def __str__(self) -> str:
# 		return str(self.__value)
#
# 	def __add__(self, other: Number) -> Number:
# 		return Number(self.__value + other.__value)
#
# 	def __sub__(self, other: Number) -> Number:
# 		return Number(self.__value - other.__value)
#
# 	def __mul__(self, other: Number) -> Number:
# 		return Number(self.__value * other.__value)
#
# 	def __truediv__(self, other: Number) -> Number:
# 		return Number(self.__value / other.__value)
#
#
# a = Number(5)
# b = Number(2)
# print(a + b)
# print(a - b)
# print(a * b)
# print(a / b)
#


from __future__ import annotations
# class Fraction:
# 	def __init__(self, numerator: int, denominator: int, int_part: int = 0):
# 		self.__num: int = numerator + int_part * denominator
# 		self.__den: int = denominator
# 	@property
# 	def num(self) -> int:
# 		return self.__num
#
# 	@num.setter
# 	def num(self, value):
# 		if type(value) == int:
# 			self.__num = value
# 	def __add__(self, fraction: Fraction) -> Fraction:
# 		num = self.__num * fraction.__den + fraction.__num * self.__den
# 		den = self.__den * fraction.__den
# 		return Fraction(num, den)
# 	def __mul__(self, fraction: Fraction) -> Fraction:
# 		num = self.__num * fraction.__num
# 		den = self.__den * fraction.__den
# 		return Fraction(num, den)
# 	def __str__(self) -> str:
# 		num = self.__num
# 		if self.__num > self.__den:
# 			int_part = int(self.__num / self.__den)
# 			num -= int_part * self.__den
# 			return f'{int_part} ({num}/{self.__den})'
# 		elif self.__num == self.__den:
# 			return str(int(self.__num / self.__den))
# 		return f'{self.__num}/{self.__den}'
# 	def __float__(self):
# 		return self.__num / self.__den



