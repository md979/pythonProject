month = input("Enter a month: ")
day = int(input("Enter a day number: "))
year = int(input("Enter a year: "))

datetime_object = datetime.datetime.strptime(month, "%b") ## the %b is for short months names
month = datetime_object.month

print(datetime.date(year,month,day))