from datetime import datetime, timedelta
from dateutil import rrule

date_strs = ['07-06-2022', '03-24-2022', '12-05-2021', '06-25-2021','01-25-2021']
dates = [datetime.strptime(d, "%m-%d-%Y") for d in date_strs]

# check consecutive date
# date_ints = set([d.toordinal() for d in dates])

# print(date_ints)

# if len(date_ints) == 1:
#     print('unique')
# elif max(date_ints) - min(date_ints) == len(date_ints) - 1:
#     print('consecutive')
# else:
#     print('not consecutive')

# check consecutive month


#ds = [] 
#for dt in rrule.rrule(rrule.MONTHLY, dtstart=dates[0], until=dates[len(dates)-1]):
#    ds.append(dt)


# for index, d in enumerate(dates[:-1]):
#     dt = rrule.rrule(rrule.MONTHLY, dtstart=d, until=dates[index+1])
#     print(dt)

ds = []
start_year = dates[0].year 
print(start_year)

for index, d in enumerate(dates[:-1]):
    num_months = abs((dates[index+1].year - d.year) * 12 + (dates[index+1].month - d.month))
    ds.append(num_months)
    if num_months > 5: break    

print(len(ds))
# 11-06-2010 = 2021
# 2-06-2011 = 2013