import random
A = random.sample(range(0,100),20)
B = random.sample(range(0,100),20)
cmn=[]

for i in A:  
    if i in cmn:
        continue 
    for j in B:
        if i == j:
            cmn.append(i)
            break
print(f"\nThe list of common numbers are:\t{cmn}")






