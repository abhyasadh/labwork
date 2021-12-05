#time in day, hour and minute
a=int(input("Enter time in seconds: "))
day=a//86400
hour=a//3600
minute=a//60
print("Time: {} days".format(day))
print("{} hour".format(hour))
print ("{} minute".format(minute))