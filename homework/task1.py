
class Date:
    def __init__(self, date):
        self.date = date

    @classmethod
    def get_date(cls, date) -> str:  # дд-мм-гггг
        day = int(date[:2])
        month = int(date[3:5])
        year = int(date[6:])
        return day, month, year

    @staticmethod
    def cross_check(date):
        day, month, year = Date.get_date(date)
        return (day, month, year)  if (year <= 2020 and month <= 12 and day <= 31) else print('ошибка ввода')


print(Date.get_date('07-11-1994'))
print(Date.cross_check('07-11-1994'))
