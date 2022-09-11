vowels  = ["a","e","i","o","u"]
consonants = []
list_of_vowels = []
exp = input("Enter Any statment")
for i in exp:
    if i in vowels and i not in list_of_vowels:
        list_of_vowels.append(i)
    else:
        if i not in consonants and i !=" ":
            consonants.append(i)
print (f"The list of vowels in this statment are:{list_of_vowels}")
print (f"The list of consonants in this statment are:{consonants}")

