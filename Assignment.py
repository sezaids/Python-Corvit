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
# st1 = {"orange","mango","pineapple","apple","kiwi"}
# st2 = {"SF90 Stradale", "roma","296","Daytona SP3"}
# st3 = {"Microsoft","Google","Apple","IBM","Dell"}
# st4 = {"mango","apple","roma","Google","IBM"}

# set_of_union = st1.union(st2,st3,st4)
# set_to_list = list(set_of_union)
# list_to_tuple = tuple(set_to_list)
# print(set_of_union)
# print(type(set_of_union))
# print(type(set_to_list))
# print(type(list_to_tuple))


# Dict = {"country": 'Pakistan', "province": "Punjab", "ID": {'name': "Zaid Sohail", 'gender': "Male", "address": "Lahore"}}
# # print("Original Dict : ", Dict)
# print("Original Dict : ", Dict["ID"])
# Dict["ID"]["religion"] = "Islam"
# Dict["ID"]["address"] = "Gojra"
# print("After Updatation : ",Dict["ID"])
# del Dict["ID"]["gender"]
# print("After Delete : " ,Dict["ID"])

# d = {
#     "a": {"b": {"c" : 0}},
#     "b": {"c" : 1},
#     "c": 2
#     }
# print(d)

# def func_city(ls):
#     input_city = input("Please enter city name: ")
#     for city in ls:
#         if(input_city == city):
#             print("City is cleaned")
#             break
#     else:
#         print("City is not cleaned")

# ls = ["faisalabad","gojra","lahore","karachi","multan"]
# func_city(ls)


# def fun(c):
#     alp = False
#     ls = ["faisalabad","gojra","lahore","karachi","multan"]
#     for city in ls:
#         if(city == c):
#             alp = True
#     if(alp):
#         print("City is cleaned")
#     else:
#         print("City is not cleaned")
# c = input("Please enter city name: ")
# fun(c)


# def func(num):
#     flag = False
#     # if num in range (50 ,501):
#     #     flag = True
#     if num >= 50 and num <= 500:
#         flag = True
#     if(flag):
#         print(num ,"Flag is True")
#     else:
#         print(num ,"Flag is False")
# c = 50+70-203*2/5
# func(c)

# Written test > 09-04-25 > Q#2
# lp = ("A distinct section of a piece of writing, usually dealing with a single theme and indicated by a new line, indentation, or numbering.")
# sep = lp.split(" ")
# in_list = list(sep)
# in_tuple = tuple(sep)

# print(type(lp))
# print(type(in_list))
# print(type(in_tuple))

# a = [1,2,3]
# print(a[2:1])

# lp = ("hello man")
# print(type(lp))

# # Assignment > 10-04-25 > Sum using Class
# class Sum:
#     def setter(this, a, b):
#         this.a = a
#         this.b = b
#     def getter(this):
#         print(f"Sum is {this.a + this.b}")

# sum = Sum()
# sum.setter(15,20)
# sum.getter()

# class Info:
#     def __init__(this,name,age):
#         this.name = name
#         this.age = age
#     def getter(this):
#         print(f"Name is : {this.name} , Age is : {this.age}")
# info1 = Info("Aslam",20)
# info2 = Info("Akram",22)
# info3 = Info("Alia",21)
# info4 = Info("Atika",24)
# info5 = Info("Aleem",26)
# info1.getter()
# info2.getter()
# info3.getter()
# info4.getter()
# info5.getter()

# class sum:
#     def __init__(this, *num):
#         this.num = num
#     def getSum(this):
#         print(f"{this.num[0]} + {this.num[1]} : {this.num[0] + this.num[1]}")
# sumNum = sum(10,155)
# sumNum.getSum()

# name age marks > **kwargs

# class Student:
#     def __init__(self, **std):
#         self.std = std
#     def getStd(self):
#         print(f"Name is : {self.std['name']} , Age is : {self.std['age']} , Marks is : {self.std['marks']}")

# std1 = Student(name = "Ali", age = 20, marks = 85)
# std1.getStd()

# class Student:
#     def __init__(self, **stdDetail):
#         self.stdDetail = stdDetail;
#     def stdPrint(self):
#         print(f"Name : {self.stdDetail['name']} --- Age : {self.stdDetail['age']} --- CGPA : {self.stdDetail['cgpa']} --- ID : {self.stdDetail['id']}")

# std1 = Student(name = "Zaid", age = 22, cgpa = 3.88, id = 240410277)
# std2 = Student(name = "Subhan", age = 21, cgpa = 3.90, id = 240512285)
# print("\n")
# std1.stdPrint()
# std2.stdPrint()
# print("\n")

class Animal:
    def __init__(self, multicellular, mobile, consumes_organics):
        self.multicellular = multicellular
        self.mobile = mobile
        self.consumes_organics = consumes_organics
    def prntanimal(multicellular, mobile, consumes_organics):
        print(f"multicellular : {multicellular} , mobile : {mobile} , consumes_organics : {consumes_organics}")

class Fish(Animal):
    def __init__(self, Cold_blooded, aquatic, gills):
        self.Cold_blooded = Cold_blooded
        self.aquatic = aquatic
        self.gills = gills
    def prntfish(self):
        print(f"Cold_blooded : {self.Cold_blooded} , aquatic : {self.aquatic} , gills : {self.gills}")

class Tuna(Fish):
    def __init__(self, fast_swimmer, saltwater, schooling):
        self.saltwater = saltwater
        self.fast_swimmer = fast_swimmer
        self.schooling = schooling
    def prnttuna(self):
        print(f"fast_swimmer : {self.fast_swimmer} , saltwater : {self.saltwater}, schooling = {self.schooling}")

class Shark(Fish):
    def __init__(self, cartilaginous, sharp_teeth, keen_smell):
        self.cartilaginous = cartilaginous
        self.sharp_teeth = sharp_teeth
        self.keen_smell = keen_smell
    def prntshark(self):
        print(f"cartilaginous : {self.cartilaginous} , sharp_teeth : {self.sharp_teeth}, keen_smell : {self.keen_smell}")

class Bird(Animal):
    def __init__(self, warm_blooded, feathers, lay_eggs):
         self.warm_blooded = warm_blooded
         self.feathers = feathers
         self.lay_eggs = lay_eggs
    def prntbird(self):
        print(f"warm_blooded : {self.warm_blooded} , feathers : {self.feathers} , lay_eggs : {self.lay_eggs}")

class Peacook(Bird):
    def __init__(self, Colorful_tail, ground_bird, omnivore):
        self.Colorful_tail = Colorful_tail
        self.ground_bird = ground_bird
        self.omnivore = omnivore
    def prntpeacook(self):
        print(f"Colorful_tail : {self.Colorful_tail} , ground_bird : {self.ground_bird} , omnivore : {self.omnivore}")

class Mammal(Animal):
    def __init__(self, Warm_blooded, hair, nurse_young, multicellular, mobile, consumes_organics):
        self.warm_blooded = Warm_blooded
        self.hair = hair
        self.nurse_young = nurse_young
        super().__init__(multicellular, mobile, consumes_organics)
    def prntmammal(self):
        print(f"warm_blooded : {self.warm_blooded} , hair : {self.hair} , nurse_young : {self.nurse_young}")

class Cat(Mammal):
    def __init__(self, Agile, claws, independent):
        self.Agile = Agile
        self.claws = claws
        self.independent = independent
    def prntcat(self):
        print(f"Agile : {self.Agile} , claws : {self.claws} , independent : {self.independent}")

class Dog(Mammal):
    def __init__(self, social, intelligent, wolf_ancestor):
        self.social = social
        self.intelligent = intelligent
        self.wolf_ancestor = wolf_ancestor
    def prntdog(self):
        print(f"social : {self.social} , intelligent : {self.intelligent} , wolf_ancestor : {self.wolf_ancestor}")

class Human(Mammal):
    def __init__(self, advanced_brain, language, tools, social, intelligent, wolf_ancestor):
        self.advanced_brain = advanced_brain
        self.language = language
        self.tools = tools
        super().__init__(social, intelligent, wolf_ancestor)
    def prnthuman(self):
        print(f"advanced_brain : {self.advanced_brain} , language : {self.language} , tools : {self.tools}")

hum = Animal()
hum.prntanimal()