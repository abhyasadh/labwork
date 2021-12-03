#time in digital clock
a=int(input("Enter number of minutes passed: "))
b=a//60
if a<60: 
    print("Time: {}".format(b))
else:
    c=a%60
    print("Time: {}".format(b),c)