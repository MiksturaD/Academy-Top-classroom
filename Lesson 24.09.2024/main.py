from people import Human
from Passport import Passport, ForeignPassport

a = Passport('Alex', 'Ivanov', '1980')
print(a)


b = ForeignPassport('Pavel', 'Durov', '1980', 'France')
print(b)