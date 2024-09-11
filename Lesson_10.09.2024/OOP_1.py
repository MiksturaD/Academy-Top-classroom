

class City:
	def __init__(self):
		self.cityname: str = ''
		self.region: str = ''
		self.country: str = ''
		self.population: int | None = None
		self.zipcode: int = 0
		self.phonecode: int = 0

	def input_city(self):
		self.city_name = input('Введите название города: ')
		self.region = input('Введите название региона: ')
		self.country = input('Введите название страны: ')
		self.population = input('Введите кол-во жителей: ')
		self.zipcode = input('Введите почтовый индекс: ')
		self.phonecode = input('Введите телефонный код города: ')


	def city_print(self):
		print(f'Название города - {self.city_name}')
		print(f'Название региона - {self.region}')
		print(f'Название страны - {self.country}')
		print(f'Кол-во жителей в городе - {self.population}')
		print(f'Почтовый индекс  - {self.zipcode}')
		print(f'Телефонный код города - {self.phonecode}')

a = City()
a.input_city()
a.city_print()