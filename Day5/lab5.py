#reverse word
#string slicing
a=input("Enter a word: ")
print(a[::-1])
#loop
j=len(a)-1
while j>=0:
    print(a[j],end="")
    j=j-1