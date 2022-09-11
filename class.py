class student:
    def __init__(self, name, age):

        self.name = name
        self.age = age

for i in range (1,3):
    name = input("Enter your name")
    age = input("enter your age")
    firstStudent = student(name, age)
    print (f"My name is {firstStudent.name} and my age is {firstStudent.age}" )
    with open (str(i)+".txt","w") as f:
        f.write(f"My name is {firstStudent.name} and my age is {firstStudent.age}")
        
