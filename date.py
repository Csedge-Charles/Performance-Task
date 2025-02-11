months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']

month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

def year(year):
    leap = int(year / 4)
    return (year - leap) * 365 + leap * 366


def month(month, year): #calculate number of days before month starts
    key = 12
    for i in range(len(months)):
        if months[i] == month:
            key = i
    total = 0
    for i in range(key):
        total += month_days[i]
    if key >= 2 and year % 4 and year >= 2024 == 0:
        total += 1
    if key <= 1 and year % 4 and year <= 2024 == 0:
        total -= 1
    return total



def between(year_1, year_2): #Jan 1 of year 1 to Jan 1 year_2
    return year(year_1 - 1) - year(year_2 - 1)


def day(mon, day, year):
    total = 0
    day_list = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    if year < 2024:
        total = -1 * month(mon, year) + between(2024, year) - (day - 1)
        return day_list[-(total % 7)]

    else:
        total = month(mon, year) + between(year, 2024) + day - 1
        return day_list[total % 7]
