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


class Course:
	def __init__(self, course_name: str, course_length: int):
		self.__course_name: str = course_name
		self.__course_length: int = course_length

class Task:
	def __init__(self, task_name: str, description: str):
		self._task_name: str = task_name
		self._description: str = description

	@property
	def task_name(self):
		return self._task_name


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



u = University()

u.add_person(
	Student(1, 'Андрюха', 'andrey@mail.ru', 5)
)
u.add_person(
	Teacher(2, 'Виктор Петрович', '2550033@mail.ru', 'Декан')
)
print(Student)
