import time


# def null_decorator(func):
# 	print('aaaa')
# 	return func
#
#
# @null_decorator
# def foo():
# 	print('Hello')
#
#
# foo()

# a = null_decorator(foo)
# print(a)
# a()


def uppercase(func):
	def wrapper():
		result = func()
		result = result.upper()
		return result
	return wrapper


def time_worker(func):
	def wrapper(*args, **kwargs):
		start = time.time()
		result = func(*args, **kwargs)
		end = time.time() - start
		print(f'Функция {func.__name__} выполнялась {end} с.')
		return result
	return wrapper


@time_worker
def calc(n, start=0):
	s = start
	for i in range(n):
		s += i
	return s


calc(1000000, start=100000)


def repeat(amount):
	def decorator(func):
		def wrapper(*args, **kwargs):
			for i in range(0, amount):
				a = func(*args, **kwargs)
				print(a)

		return wrapper
	return decorator


@repeat(2)
def say_hi(name):
	return f'Hello, my name is {name}'


say_hi('DENIS')