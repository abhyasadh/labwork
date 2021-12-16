a=['abc','xyz','aba','1221','abba']
y=0
for x in a:
    if len(x)>2:
        if x[0]==x[len(x)-1]:
            y=y+1
print(y)