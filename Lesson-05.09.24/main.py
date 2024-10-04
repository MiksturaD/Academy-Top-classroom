from __future__ import annotations
class Fraction:

	def __init__(self, numerator: int, denominator: int, int_part: int = 0):
		self.__num: int = numerator + int_part * denominator
		self.__den: int = denominator
		self.count: int = 0
		self.count+=1
	@property
	def num(self) -> int:
		return self.__num

	@num.setter
	def num(self, value):
		if type(value) == int:
			self.__num = value
	def add(self, fraction: Fraction) -> Fraction:
		num = self.__num * fraction.__den + fraction.__num * self.__den
		den = self.__den * fraction.__den
		return Fraction(num, den)
	def multiply(self, fraction: Fraction) -> Fraction:
		num = self.__num * fraction.__num
		den = self.__den * fraction.__den
		return Fraction(num, den)
	def __str__(self) -> str:
		num = self.__num
		if self.__num > self.__den:
			int_part = int(self.__num / self.__den)
			num -= int_part * self.__den
			return f'{int_part} ({num}/{self.__den})'
		elif self.__num == self.__den:
			return str(int(self.__num / self.__den))
		return f'{self.__num}/{self.__den}'
	def __float__(self):
		return self.__num / self.__den

	def count_obj(self):
		print(self.count)


a = Fraction()
# f1 = Fraction(2, 3, int_part=3)
f2 = Fraction(3, 3)
#
# f3: Fraction = f1.add(f2)
# f4: Fraction = f3.add(f1)
print(f2)
# print(f.get_num())
a.count_obj()
