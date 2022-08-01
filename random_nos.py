import random

New_array = [];
nos_40 = []
count_40 = 0
for i in range(100):
    nos = random.randint(10,90)
    New_array.append(nos)
print(New_array)
max_no = max(New_array)
min_no = min(New_array)
sum_no = sum(New_array)
avg_nos = (sum_no/len(New_array))
for no in New_array:
    if no > 40:
       continue 
    count_40 = count_40 + 1
    nos_40.append(no)
print(f"The maximum number is = {max_no}")
print(f"The minimum number is = {min_no}")
print(f"The sum of numbers is = {sum_no}")
print(f"The average of numbers is = {avg_nos}")
print(f"The count of numbers which are greater than 40 = {count_40}")
print(f"The sum of numbers which are greater than 40 = {sum(nos_40)}")











