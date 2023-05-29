import datetime
#
# # mytime = datetime.time()
# #
# # print(mytime.minute)
# # print(mytime)
#
# today = datetime.date.today()
#
# print(today)
# today.year

date1 = datetime.date(2020,5,25)
date2 = datetime.date(2021,5,25)
final_date = date2 - date1

print(type(final_date))
datetime.timedelta
print(final_date.days)

# como lidar com datas em python