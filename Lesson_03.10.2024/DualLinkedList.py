from __future__ import annotations


class Item:
	def __init__(self, value: int, prev: Item | None = None, nxt: Item | None = None):
		self.prev: Item = prev
		self.value: int = value
		self.next: Item = nxt

	def __str__(self) -> str:
		return f'[{self.value} | {self.next}]'


class DualLinkedList:
	def __init__(self):
		self.__start: Item | None = None
		self.__current: Item | None = None
		self.__last: Item | None = None

	def add(self, value: int):
		if self.__start is None:
			item: Item = Item(value)
			self.__start = item
			self.__current = item
			self.__last = item
		else:
			item: Item = Item(value, prev=self.__last)
			self.__last.next = item
			self.__last = item

	def get(self):
		if self.__current is None:
			raise Exception('Конец, больше нет элементов в списке')

		return self.__current.value

	def next(self):
		self.__current = self.__current.next

	def prev(self):
		self.__current = self.__current.prev