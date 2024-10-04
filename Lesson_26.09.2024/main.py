from abc import abstractmethod


class HomeAnimals:
	def __init__(self, name: str, animal_kind: str):
		self._name = name
		self._animal_kind = animal_kind

	@abstractmethod
	def sound(self):
		raise NotImplemented('Обязательно нужно создать метод для звука животного')

	@abstractmethod
	def show(self):
		raise NotImplemented('Обязательно нужно создать метод для показа имени животного')

	@abstractmethod
	def type(self):
		raise NotImplemented('Обязательно нужно создать метод для показа подвида животного')


class Dog(HomeAnimals):

	def __init__(self, name: str, animal_kind: str):
		super().__init__(name, animal_kind)

	def sound(self):
		print('What a gav gav gav!')

	def show(self):
		print("I'm sutulaya psina")

	def type(self):
		print('Type Mini-dog')

	


class Cat(HomeAnimals):

	def __init__(self, name: str, animal_kind: str):
		super().__init__(name, animal_kind)

	def sound(self):
		print('What a meow meow!')

	def show(self):
		print("I'm Kittycat")

	def type(self):
		print('Type Cats')


class Camel(HomeAnimals):

	def __init__(self, name: str, animal_kind: str):
		super().__init__(name, animal_kind)

	def sound(self):
		print('What a uergh!')

	def show(self):
		print("I'm Camel")

	def type(self):
		print('Type Egypt Camel simple')


class Alien(HomeAnimals):

	def __init__(self, name: str, animal_kind: str):
		super().__init__(name, animal_kind)

	def sound(self):
		print('RrrRrRrraaaaaahhhhh')

	def show(self):
		print("I'm Gizmo")

	def type(self):
		print('Type Mars')


a = Alien('Patrick', 'Planet_alien')
b = Dog('Psina','Shlyapa')
a.sound()
a.show()
a.type()
b.sound()
b.type()
b.show()