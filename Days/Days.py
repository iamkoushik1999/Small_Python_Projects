import itertools


from itertools import count

days = ['Mon Day', 'Tues Day', 'Wednes Day', 'Thurs Day', 'Fri Day', 'Satur Day', 'Sun Day']
for i, j in zip(count(), days):
    if i == 0:
        print('WorkingDays:')
    if i == 5:
        print("\nHoliDays:")
    if i == 5 and i == 6:
        print(j)
    else:
        print(j)