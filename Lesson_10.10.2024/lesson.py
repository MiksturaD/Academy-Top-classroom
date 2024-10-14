# Задача 1: Система управления библиотекой
# Описание: Реализуйте систему управления библиотекой. В библиотеке могут быть книги и журналы.
# У каждого предмета есть уникальный ID, название, автор (для книг) или издатель (для журналов),
# и информация о том, доступен ли он для выдачи. Необходимо реализовать возможность добавления,
# удаления и поиска предметов, а также возможность "взять на время" и "вернуть" предмет.
#
# Условия:
# - Создайте класс LibraryItem, который будет базовым для Book и Magazine.
# - В классе LibraryItem должно быть поле для уникального ID, названия и статуса доступности.
# - В классе Book добавьте поле для автора, а в классе Magazine — для издателя.
# - Добавьте методы для поиска предметов по названию или ID, для добавления и удаления предметов.
# - Реализуйте методы для "взять на время" и "вернуть" предмет.
from __future__ import annotations

from time import time


class Item:
	def __init__(self, id: int, name: str, taken: bool = False):
		self.__id: int = id
		self._name: str = name
		self.__taken: bool = taken

	@property
	def id(self):
		return self.__id

	def __status(self):
		return self.__taken

	def change_status(self):
		self.__taken = not self.__taken


class Book(Item):
	def __init__(self, id: int, name: str, author: str):
		super().__init__(id, name)
		self.__author: str = author

	def __str__(self):
		return (f'{self.id}: (Книга) {self.__author} - '
						f'{self._name} ({"Не доступен" if self.__status() else "Доступен"})')


class Magazine(Item):
	def __init__(self, id: int, name: str, publisher: str):
		super().__init__(id, name)
		self.__publisher: str = publisher

	def __str__(self):
		return (f'{self.id}: (Журнал) {self.__publisher} - '
						f'{self._name} ({"Не доступен" if self.__status() else "Доступен"})')


class Library:
	def __init__(self):
		self.__items: list[Item] = []

	def add(self, item: Item):
		self.__items.append(item)

	def find(self, id: int) -> Item:
		for item in self.__items:
			if item.id == id:
				return item
		raise Exception(f'Предмет с id {id} не найден')

	def take(self, id: int):
		item = self.find(id)
		if not item.__status():
			item.change_status()
		else:
			raise Exception(f'Предмет {id} уже взяли')

	def bring_back(self, id: int):
		item = self.find(id)
		if item.__status():
			item.change_status()
		else:
			raise Exception(f'Предмет {id} на месте, что вы пытаетесь вернуть?')

	def __str__(self):
		return '\n'.join([str(item) for item in self.__items])


### Задача: Система управления видеотекой

# Описание: Разработайте систему управления видеотекой, где можно брать в аренду фильмы.
# В системе есть различные виды контента, такие как фильмы, сериалы и документальные фильмы.
# У каждого контента есть уникальный ID, название, режиссер, длительность и информация о доступности для аренды.
# Пользователи могут брать в аренду контент, а затем возвращать его.
# Также пользователи могут просматривать историю арендованных фильмов и оставлять оценки для контента.


class Video:
	def __init__(self, id: int, name: str, director: str, duration: int, rented: bool = False):
		self.__id: int = id
		self.__name: str = name
		self.__director: str = director
		self.__duration: int = duration
		self.__rented: bool = rented

	@property
	def id(self):
		return self.__id

	@property
	def duration(self) -> str:
		return f'{self.__duration // 60}:{self.__duration % 60}'

	def is_rented(self) -> bool:
		return self.__rented

	def change_status(self):
		self.__rented = not self.__rented

	def __str__(self):
		return (f'{self.__id}: {self.__director} - {self.__name} '
						f'({self.duration}) - {not self.__rented}')


class VideoManager:
	def __init__(self):
		self.__videos: list[Video] = []

	def add(self, video: Video):
		self.__videos.append(video)

	def find(self, id: int) -> Video:
		for video in self.__videos:
			if video.id == id:
				return video
		raise Exception(f'Видео с id {id} не найдено')

	def rent(self, id: int):
		video = self.find(id)
		if not video.is_rented():
			video.change_status()
		else:
			raise Exception(f'Уже арендовано!')

	def bring_back(self, id: int):
		video = self.find(id)
		if video.is_rented():
			video.change_status()
		else:
			raise Exception(f'Еще не взяли в аренду')


vm = VideoManager()

a = Video(1, 'Name1', 'lastname1', 1440)

vm.add(a)
vm.add(Video(2, 'Name2', 'lastname2', 1740))
vm.add(Video(3, 'Name3', 'lastname3', 1121))

v1 = vm.find(3)
print(v1)
v2 = vm.find(1)
print(v2)

vm.rent(2)
vm.bring_back(2)