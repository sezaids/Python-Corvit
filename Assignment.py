# 01 Assignment - W1-D3

# age = input("Please Enter your Age : ")
# height = input("Please Enter your Height in Feet : ")
# education = input("Please Enter your Highest education : ")

# age = int(age)
# height = float(height)
# education = int(education)

# if(height >= 5.6):
#     if(education >= 12):
#         print("Congratulation! You passed the eligiblity criteria")
#     elif(age >= 18 and age <=32):
#         print("Congratulation! You passed the eligiblity criteria")
#     else:
#         print("Sorry! You are not eligiblity")
# elif (age >= 18 and age <=32) and (education >= 12):
#     print("Congratulation! You passed the eligiblity criteria")
# else:
#     print("Sorry! You are not eligiblity")


# 02 Assignment - W1-D3 

# obtained_marks = int(input("Enter your obtained marks: "))
# total_marks = int(input("Enter your Total marks: "))
# percentage = float((obtained_marks/total_marks)*100)
# print(percentage)


# # 03 Assignment - W1-D3 - Homework

# bonus_amount = float(input("Please enter your 6 month's bonus : "))
# bonus_percentage = float(input("Please enter your bonus' percentage : "))

# half_year_salary = (bonus_amount / (bonus_percentage/100))
# monthly_salary = half_year_salary/6
# print(" ")
# print("Your monthly Salary: " ,monthly_salary)
# print("Your half year's Salary: " ,half_year_salary)


# # 03 Assignment - W1-D3 - Homework
# bonus_amount = float(input("Please enter your bonus : "))
# bonus_percentage = (float(input("Please enter your bonus' percentage : ")))/100
# monthly_salary = (bonus_amount / (bonus_percentage))
# print(" ")
# print("Your monthly Salary: " , monthly_salary)


# # 04 Assignment - W1-D3
# city = "jaranwala faisalabd lahore "
# print(city[0].replace("j","J")+city[1:9],city[10].replace("f","F")+city[11:19],city[20].replace("l","L")+city[21:])
# # print(city.replace(("j","f","l")("J","F","L")))


# # # 05 Assignment - W1-D4
# # Replace first letter in small using only replace() do not use slice method
# original_string = "Jaranwala Faisalabad Lahore Karachi Multan"
# new_string = original_string.replace("J","j").replace("F","f").replace("L","l").replace("K","k").replace("M","m")
# print(new_string)


# ls =["lahore" , "faisalabad" , "jaranwala" , "Karachi" , "Gojra"]
# ls[0:1] = ["Lahore"]
# ls[1:2] = ["Faisalabad"]
# ls[2:] = ["Jaranwala"]

# newls = ls[0][0].upper()+ls[0][1
# print(type(ls), ls)

# for city in ls:
#     n = len(city) - 1
#     print(city[0].upper() + city[1:n] + city[n].upper())

# lp = []
# for x in ls :
    # p = x[0:1].lower() + x[1:2].upper() + x[2:-2].lower() + x[-2:-1].upper() + x[-1:].lower()
#     lp.append(p)
# print(lp)

# ls =["Lahore" , "Faisalabad" , "Jaranwala" , "Karachi" , "Gojra"]

# lp = []
# for city in ls :
#     lp.insert(0,city)
# print(lp)

# Assignment 19-03-25 (H-W)
# 10 cities 
# first reverse
# first and last letter should be large
# at middle should be small letters

# cities = ["larkana","khanewal","FaisaLABAD","KARAchi","lahore","peshawar","Multan","sargodha","quetta","GoJra"]
# new_cities = []
# for city in cities:
#     city = city[:1].upper()+city[1:-1].lower()+city[-1:].upper()
#     new_cities.insert(0,city)
# print(new_cities)

# Assignment
# for x in range(1,11):
#     print("2 X " + str(x) + " = " + str(2*x))

# ls = []
# ls.append((input("Please Enter: ")))
# ls.append((input("Please Enter: ")))
# print(ls)

# factorial_num = int(input("Please enter factorial num: "))
# factorial = 1

# i = 0
# count = 0
# for x in range(0,101):
#     while i < len(x):
#         count = count + 1
#         print(x[i])
#         i = i+1
# print("3 repeatation in range: " + str(count))

# print even in ls - written test - 24-03-25
# ls = [1,2,3,4,5,6,7,8,9,10]
# for num in ls:
#     if num % 2 == 0:
#         print(num)

# ls1 = ["Faisalabad", "jaranwala","lahore"]
# # print first letter capital , middle small, last capital - written test - 24-03-25
# lp = []
# for city in ls1:
#     city1 = city[0].upper()+city[1:-1].lower()+city[-1:].upper()
#     lp.append(city1)
# print(lp)

# Convert first letter of each word in capital letter in Tuple and also return Tuple
# append_city = []
# tuple_city = ("faisalabad", "laHore", "gojra")
# list_city = list((tuple_city))
# for city in list_city:
#     single_city = city[0].upper() + city[1:-1].lower()+city[-1:].upper()
#     append_city.append(single_city)
# tuple_city = tuple((append_city))
# print(tuple_city, type(tuple_city))

# tup1 = ("Faisalabad", "Jaranwala", "Lahore")
# tup2 = (1,2,3,4,5,6)
# list_tup1 = list((tup1))
# list_tup2 = list((tup2))
# list_tup3 = list_tup2 + list_tup1
# print(list_tup3[6:9] + list_tup3[0:6])

# list_tup3.pop(0)
# list_tup3.insert(0,list_tup1)
# print(list_tup3[0:])

# st1 = "item1"
# st2 = "item2"
# st3 = "item3"
# st4 = "item4"
# st = {st1,st2}
# # st2 = {"item1","item2","item3","item4"}
# (st1,st2) = st
# st.clear()
# st.update((st3,st4))
# print(type(st))
# st = list((st))
# print(type(st))
# st = tuple((st))
# print(type(st))

# ls = ["apple", "pineapple","mange","orange","banana"]
# tup = ("grapes", "pineapple","kiwi","cherry","banana")
# st1 = set((ls))
# set2 = set((tup))
# set1 = st1 | set2
# dif = set1 - set2
# uni = set1.union(set2)
# intsec = set1.intersection(set2)
# print(dif)
# print(uni)
# print(intsec)

# tup = (0,1,2,3,4,5,6,7,8,9)
# (t0,t1,t2,t3,t4,t5,t6,t7,*t8) = tup
# t8.append("eleven")
# t8.append("twelve")
# print(t8)
# st = list((t8))
# print(type(st), st)

# set 1 + set 2 + set 3 + set 4 -> join using union -> list -> tuple
st1 = {"orange","mango","pineapple","apple","kiwi"}
st2 = {"SF90 Stradale", "roma","296","Daytona SP3"}
st3 = {"Microsoft","Google","Apple","IBM","Dell"}
st4 = {"mango","apple","roma","Google","IBM"}

set_of_union = st1.union(st2,st3,st4)
set_to_list = list(set_of_union)
list_to_tuple = tuple(set_to_list)
print(set_of_union)
print(type(set_of_union))
print(type(set_to_list))
print(type(list_to_tuple))