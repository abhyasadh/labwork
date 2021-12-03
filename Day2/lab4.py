a=int(input("Enter number of apples in the basket: "))
b=int(input("Enter number of students: "))
c=a//b
print("{} apples for single student".format(c))
d=a-(c*b)
print("{} apples remain in basket".format(d))