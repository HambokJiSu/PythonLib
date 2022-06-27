import datetime
day1 = datetime.date(2019, 12, 14)
print("day1:", day1)
datetime.date(2019, 12, 14)
day2 = datetime.date(2021, 6, 5)
print("day2:", day2)

diff = day2 - day1
print("diff:", diff)

print("day3")
day3 = datetime.datetime(2020, 12, 14, 14, 10, 50)
print(day3.hour)
print(day3.minute)
print(day3.second)

#	combine() 함수로 datetime.date 객체와 datetime.time 객체를 합쳐 일시 데이터를 만들 수도 있다.
print("dt")
day = datetime.date(2020, 12, 14)
time = datetime.time(10, 14, 50)
dt = datetime.datetime.combine(day, time)
print(dt)

#	오늘 기준 100일 이후 날짜 구하기
dt2 = datetime.date.today()
diff_days = datetime.timedelta(days=100)

print("plus 100Days:",dt2 + diff_days)