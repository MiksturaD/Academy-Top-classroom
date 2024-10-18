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