import calendar

print('Добро пожаловать в супер календарь \n')

year = int(input('Пожалуйста введите гол: '))
month = int(input('Введите номер любого месяца: '))

print(calendar.month(year, month))

print('Всего хорошего!')