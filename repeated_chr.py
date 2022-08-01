from ast import IsNot, NotIn


string_ = input("\nEnter the statement\n")
chr = []
for i in sorted(string_.lower()): 
    if i not in chr:
        count_ = string_.count(i)
        chr.append(i)
        if i != " ":
            print(f"\nThe letter {i} is repeated {count_} times")



     


        


