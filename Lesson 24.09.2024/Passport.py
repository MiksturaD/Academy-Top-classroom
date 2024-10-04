

class Passport:
	def __init__(self, first_name: str, last_name: str, date_birth: str):
		self._first_name = first_name
		self._last_name = last_name
		self._date_birth = date_birth

	def __str__(self):
		return f'Данные паспорта Имя - {self._first_name} Фамилия - {self._last_name} Дата рождения - {self._date_birth}'


class ForeignPassport(Passport):
	def __init__(self, first_name: str, last_name: str, date_birth: str, visa: str):
		super().__init__(first_name, last_name, date_birth)
		self._visa = visa

	def __str__(self):
		return super().__str__() + f' Visa - {self._visa}'


