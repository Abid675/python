
A = int(input("enter number\n"))
for i in range(A,0,-1):
    print("\n")
    for j in range(i):
        print(i-j,'\t', end='')
        if i-j == 1:
            print(f"\n")


        
