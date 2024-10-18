# Задание 1
# Есть некоторый словарь, который хранит названия
# стран и столиц. Название страны используется в качестве
# ключа, название столицы в качестве значения. Необходимо
# реализовать: добавление данных, удаление данных, поиск
# данных, редактирование данных, сохранение и загрузку
# данных (используя упаковку и распаковку).



# ctrl + влево/вправо
# Home/End
# ctrl + Home/End
# pageUp/pageDown
# ctrl + d //// alt+shift+вниз/вверх
# ctrl + w


class CountryManager:
	def __init__(self, filename: str):
		self.__countries: dict[str, str] = CountryManager.__from_file(filename)

	@staticmethod
	def __from_file(filename: str) -> dict[str, str]:
		countries: dict[str, str] = {}

		with open(filename, 'r', encoding='utf-8') as f:
			lines: list[str] = f.readlines()
			for line in lines:
				country_name, capital_name = [item.strip() for item in line.split(' ')]
				countries[country_name] = capital_name

		return countries

	def to_file(self, filename: str) -> None:
		with open(filename, 'w', encoding='utf-8') as f:
			f.writelines([f'{country_name} {capital_name}\n' for country_name, capital_name in self.__countries.items()])

	def add(self, country: [str, str]):
		country_name, capital_name = country
		self.__countries[country_name] = capital_name

	def remove(self, country_name: str):
		del self.__countries[country_name]

	def find(self, country_name: str) -> str:
		return self.__countries[country_name]

	def __str__(self) -> str:
		return str(self.__countries)


cm = CountryManager('countries.txt')
cm.add(('Россия', 'Москва'))
print(cm)
cm.to_file('c2.txt')


# Задание 2
# Есть некоторый словарь, который хранит названия
# музыкальных групп(исполнителей) и альбомов. Название группы используется в качестве ключа, название
# альбомов в качестве значения. Необходимо реализовать:
# добавление данных, удаление данных, поиск данных,
# редактирование данных, сохранение и загрузку данных
# (используя упаковку и распаковку).

class MusicService:
	def __init__(self, filename: str):
		self.__music_band: dict[str, str] = MusicService.__from_file(filename)

	@staticmethod
	def __from_file(filename: str) -> dict[str, str]:
		music_band: dict[str, str] = {}

		with open(filename, 'r', encoding='utf-8') as f:
			lines: list[str] = f.readlines()
			for line in lines:
				band_name, album = [item.strip() for item in line.split(' ')]
				music_band[band_name] = album

		return music_band
	def to_file(self, filename: str) -> None:
		with open(filename, 'w', encoding='utf-8') as f:
			f.writelines(f'{self.band_name} {album}\n')

	def add(self, music_band: [str, str]):
		band_name, album = music_band
		self.__music_band[band_name] = album

	def remove(self, band_name: str):
		del self.__music_band[band_name]

	def find(self, album: str) -> str:
		return self.__music_band[album]

	def __str__(self) -> str:
		return str(self.__music_band)


mb = MusicService('Bands.txt')
mb.add(('RHCP','The Getaway'))
mb.add(('Slipknot','The gray chapter'))
mb.add(('RHCP','Californication'))
mb.add(('Korn','Thenothing'))
mb.add(('Metallica','Blackalbum'))
mb.to_file('Bands.txt')
print(mb)