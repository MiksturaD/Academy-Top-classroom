### Задача: Система управления курсами и студентами

# Описание: Разработайте систему управления курсами в университете.
# В системе могут быть курсы, студенты и преподаватели.
# Студенты могут записываться на курсы, просматривать свои оценки и получать уведомления о новых заданиях.
# Преподаватели могут добавлять задания, выставлять оценки и отправлять уведомления.
# Курсы могут содержать несколько заданий, каждое из которых имеет максимальный балл.

from __future__ import annotations

from abc import abstractmethod


class Person:
	def __init__(self, person_id: int, name: str, email: str):
		self._person_id: int = person_id
		self._name: str = name
		self._email: str = email

	@staticmethod
	@abstractmethod
	def from_console() -> Person:
		raise NotImplementedError('нужно реализовать метод')

	def __str__(self) -> str:
		return f'{self._person_id}: {self._name} ({self._email})'


class Teacher(Person):
	def __init__(self, person_id: int, name: str, email: str, job_title: str):
		super().__init__(person_id, name, email)
		self._job_title: str = job_title

	@staticmethod
	def from_console() -> Teacher:
		person_id: int = int(input('Введите id: '))
		name: str = input('Введите name: ')
		email: str = input('Введите email: ')
		job_title: str = input('Введите должность: ')
		return Teacher(person_id, name, email, job_title)

	@staticmethod
	def send_notification():
		notify: str = input('Введите уведомление ,которое хотите направить студентам.')
		return notify

	@staticmethod
	def give_a_rating():
		rate: float = float(input('Введите оценку, которую хотите поставить за курс - '))
		return rate

	def __repr__(self):
		return f'Преподаватель  ({self._person_id}, {self._name}, {self._email}, {self._job_title})'


class Student(Person):
	def __init__(self, person_id: int, name: str, email: str, grade: float):
		super().__init__(person_id, name, email)
		self._grade: float = grade
		self._tasks_completed: list[Task] = []

	@staticmethod
	def from_console() -> Student:
		person_id: int = int(input('Введите id: '))
		name: str = input('Введите name: ')
		email: str = input('Введите email: ')
		grade: float = float(input('Введите grade: '))
		return Student(person_id, name, email, grade)

	def complete_task(self, task: Task, score: float) -> None:
		self._tasks_completed.append((task, score))
		print(f'Студент {self._name} выполнил задание {task._task_name} и получил {score} баллов.')

	def __repr__(self):
		return f'Студент({self._person_id}, {self._name}, {self._email}, {self._grade})'


class Course:
	def __init__(self, course_name: str, course_length: int):
		self.__course_name: str = course_name
		self.__course_length: int = course_length

	def __repr__(self):
		return f'Курс({self.__course_name}, {self.__course_length} - часов)'


class Task:
	def __init__(self, task_name: str, description: str):
		self._task_name: str = task_name
		self._description: str = description

	@property
	def task_name(self):
		return self._task_name

	def __repr__(self):
		return f'Задание - ({self.task_name}, {self._description})'


class University:
	def __init__(self):
		self.__teachers: list[Teacher] = []
		self.__courses: list[Course] = []
		self.__students: list[Student] = []
		self.__tasks: list = []

	def add_person(self, person: Person):
		if isinstance(person, Student):
			self.__students.append(person)
		elif isinstance(person, Teacher):
			self.__teachers.append(person)
		else:
			raise Exception('Можно добавить только студента или препода')

	def add_course(self, course: Course):
		self.__courses.append(course)

	def add_task(self, task: Task):
		self.__tasks.append(task)

	def __str__(self):
		return (f'Преподаватели - {self.__teachers}\n'
						f'Студенты - {self.__students}\n'
						f'Курсы - {self.__courses}\n'
						f'Задания - {self.__tasks}')

# Вроде бы так, что нужно было сделать по заданию - имеется, по идее можно углубиться
# и пойти дальше, выбирать какому студенту, за какой курс и задание ставить оценку и все
# это выводить, но по заданию вроде такого не было :)

u = University()
u.add_course(Course('Физика', 200))
u.add_course(Course('Изучение Python', 400))
u.add_task(Task('Законы Ньютона', 'Изучите все три и расскажите'))
u.add_task(Task('Чат бот ТГ', 'напишите чат бота за 200 дней'))
u.add_person(Student(1, 'Андрюха', 'andrey@mail.ru', 5))
u.add_person(Student(2,'Балбесина','balbes@mail.ru',1))
u.add_person(Teacher(2, 'Виктор Петрович', '2550033@mail.ru', 'Декан'))
print(u)
