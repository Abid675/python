
string_ = input("\nEnter the statement\n")
chr_ = dict()

for i in sorted(string_.lower()): 
    if i not in chr_:
        chr_[i] = 1
    else:
        chr_[i] += 1
for key, value in chr_.items():
    print(f"The character {key} is repeated {value} times")





        