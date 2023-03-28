def check_type(*types):
    def decorator(func):
        def wrapper(*args):
            for args, arg_type in zip(args[1:], types):
                if not isinstance(args, arg_type):
                    raise TypeError(f'Expected type {arg_type}. Got {type(args)} instead')
                return func(*args)
            return wrapper
        return decorator


class Date:

    def __init__(self, year, month, day):
        self.__year = year
        self.__month = month
        self.__day = day

    @property
    def year(self) -> int:
        return self.__year

    @property
    def month(self) -> int:
        return self.__month

    @property
    def day(self) -> int:
        return self.__day

    @year.setter
    @check_type(int)
    def year(self, year: int):
        self.__year = year

    @month.setter
    @check_type(int)
    def month(self, month: int):
        if 0 < month <= 12:
            self.__month = month
        else:
            raise ValueError('месяц от 1 до 12')

    @day.setter
    @check_type(int)
    def day(self, day: int):
        days = self.days_in_month()
        if 0 < day <= days:
            self.__day = day
        else:
            raise ValueError('ошибка')

    def is_leap_year(self, year=None):
        year = year if year else self.__year
        if year % 400 == 0:
            return True
        elif year % 100 == 0:
            return False
        elif year % 4 == 0:
            return True
        else:
            return False

    def days_in_month(self, month=None, year=None):
        month = month if month else self.__month
        if month in [1, 3, 5, 7, 8, 10, 12]:
            return 31
        elif month in [4, 6, 9, 11]:
            return 30
        elif month == 2 and self.is_leap_year(year):
            return 29
        else:
            return 28

    def next_day(self):
        if self.__day < self.days_in_month():
            self.__day += 1
        elif self.__month < 12:
            self.__month += 1
            self.__day = 1
        else:
            self.__year += 1
            self.__month = 1
            self.__day = 1

    def set_date(self, string):
        from re import fullmatch, split
        correct_date = fullmatch(r'\d\d\w\d\d\w\d{4}', string)
        if correct_date:
            day, month, year = split(r'\w', correct_date.group())
            self.month = int(month)
            self.day = int(day)
            self.year = int(year)
        else:
            raise ValueError('Ошибка')


a = Date(2012, 12, 5)
print(a)

print(str(a))