#Написать функцию is_year_leap, принимающую 1 аргумент — год, и возвращающую True, если год високосный, и False иначе.
def year(y):
    return y % 4 == 0 and y % 100 == 0  or y % 400 == 0
print(year(int(input())))