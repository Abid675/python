#This program will find wheter the words are palindrom or not
from csv import list_dialects


exp=input("enter single word\n")
list_ = []
for i in exp:
    list_.append(i)
for j in range(len(exp)):
    con=False
    if list_[j] == list_[-j-1]:
        con = True
if con:
    print(f"The word {exp} is palindrome")
else:
    print(f"The word {exp} is not palindrome")


    


