
for i in range (5,55,5):
   print(i)   
   

i = 1
while i<=10:
    print(i)
    i=i+2


for i in range(6):
    for j in range(i):
        print("*",end="")
    print()    

i=1
while i<=5:
    j=1
    while j<=i:
        print(i,end="")
        j=j+1
    i=i+1
    print()    