no = int(input("Enter number to form diamond(2-10)"))
count = no*2
iter=0
for j in range(no):
    if j==0:
        for k in range(count):
            print(" ",end='')
        print (no-j)
    else:
        for q in range(count):
            print(" ",end='')
        print (no-j,end='')
        for p in range(iter):
            print(" ",end='')
        print (no-j,iter)
    count -= 2
    iter = ((2*no)-count)*2-1

for j in range(no,-1,-1):
    if j==0:
        for k in range(count):
            print(" ",end='')
        print (no)
    elif j==no:
        pass

    else:
        for q in range(count):
            print(" ",end='')
        print (no-j,end='')
        for p in range(iter):
            print(' ',end='')
        print (no-j)
    count += 2
    iter = ((2*no)-count)*2-1  

