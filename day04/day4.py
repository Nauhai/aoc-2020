import functools
from abc import *


def str_to_field(field_input):
    name, value = field_input.split(':')
    return name, value

fields_validation = {
    'byr': lambda value: value.isdigit() and int(value) in range(1920, 2003),
    'iyr': lambda value: value.isdigit() and int(value) in range(2010, 2021),
    'eyr': lambda value: value.isdigit() and int(value) in range(2020, 2031),
    'hgt': lambda value: (value[-2:] == 'cm' and value[:-2].isdigit() and int(value[:-2]) in range(150, 194)) or (value[-2:] == 'in' and value[:-2].isdigit() and int(value[:-2]) in range(59, 77)),
    'hcl': lambda value: value[0] == '#' and all(char in '0123456789abcdef' for char in value[1:]),
    'ecl': lambda value: value in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth'],
    'pid': lambda value: value.isdigit() and len(value) == 9
}

def is_field_valid(name, value):
    return fields_validation[name](value)

class Passport(ABC):
    def __init__(self, passport_input):
        self.fields = {name: value for name, value in list(map(str_to_field, ' '.join(passport_input).split(' ')))}

    @abstractmethod
    def is_valid(self):
        pass

class Passport1(Passport):
    def is_valid(self):
        return all(field in self.fields.keys() for field in fields_validation.keys())

class Passport2(Passport):
    def is_valid(self):
        return all(field in self.fields.keys() for field in fields_validation.keys()) and all(name == 'cid' or is_field_valid(name, value) for name, value in self.fields.items())


def solve_problem(passports):
    return len(list(filter(lambda passport: passport.is_valid(), passports)))


if __name__ == '__main__':
    with open('input.txt') as file:
        passports = []
        passport = []
        for line in file.readlines():
            if line.strip() == '':
                passports.append(passport)
                passport = []
                continue
            passport.append(line.strip())
        passports.append(passport)

        print('Problem 1:', solve_problem(list(map(lambda passport: Passport1(passport), passports))))
        print('Problem 2:', solve_problem(list(map(lambda passport: Passport2(passport), passports))))
