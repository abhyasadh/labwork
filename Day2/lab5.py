a=int(input("Enter number of students in first class: "))
b=int(input("Enter number of students in second class: "))
c=int(input("Enter number of students in third class: "))
if a%2==0:
    d=a/2
else:
    d=(a+1)/2
if b%2==0:
    e=b/2
else:
    e=(b+1)/2
if c%2==0:
    f=c/2
else:
    f=(c+1)/2
g=d+e+f
print("Number of bench in first class: {}".format(int(d)))
print("Number of bench in second class: {}".format(int(e)))
print("Number of bench in third class: {}".format(int(f)))
print("Total no. of bench needed: {}".format(int(g)))