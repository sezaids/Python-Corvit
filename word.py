# 01 - display the result to output
# print("hello world")
# print(34)
# print(True)
# print(type("hello world 56"))

# 02 - legal name of variables

# name = "Khurram"
# firstName = "ali" # camel case;
# FirstName = "aslam" # pascal case;
# first_name = "ali" # snake case;
# name1st = "alia" # number case; case sensitive;


# 03 - type of variables;

# print(type(23))
# print(type(True))
# print(type("34"))

# 04 data types in python

# a = "string"
# b = True
# c = 34
# d = 34.5
# e = 1j
# f = ["aslam","amna","mehmona"] 
# g = ("hello","world","!")
# h = {"name":"umar","age":23}
# i = b"hello world"
# j = {"hi","many","fight"}

# 05 math operation

# a = 4
# b = 2
# sum =  a + b 
# print(sum , type(sum))
# print(a ** b)

# 06 input type 

# a = input("Enter you name : ")
# print(a,type(a))

# 07 if conditions 

# num = 101
# if (num >= 45 and num <= 50 ) :
#     print("you are passed")
# elif (num >= 90 and num > 101) :
#     print("you are passed Grad A")
# else :
#     print("you are not passsed")

# num = 20
# num2 = 60
# if num == 20:

#     if num2 == 40:
#         print("you got both right")
#     elif num2 == 60:
#         print("hurrey you got it")
#     else :
#         print("you have wrong")
# else:
#    print( "you got both wrong")

# marks = 90
# if marks > 80:
#     print("passed")
# elif marks > 85:
#     print("passed Grade a")

# 08 typ casting

# num = "45"
# num = int(num)
# print(type(num))

# num2 = 45
# num2 = str(num2)
# print(type(num2))

# num3 = "43.0"
# num3 = float(num3)
# print(type(num3))

# val = input("Enter your age in number : ")
# val1 = int(val)
# print(type(val1) , type(val))


# 01 Assignment solution

# edu = int(input("Enter you education : "))
# age = int(input("Enter you age : "))
# height = float(input("Enter you height : "))

# if( edu >= 12 and (age <= 32 and age >= 18)):
#     print("Passed")
# elif( (age <= 32 and age >= 18) and height >= 5.6 ) :
#     print("Passed")
# elif(  height >= 5.6 and edu >= 12 ) :
#     print("Passed")
# else:
#     print("Failed")

# 09  multiline string

# b = """hello world how are
#  you;"""
# print(b)

# c = """hello world"""
# print(type(c), len(c))

# 10 concatenation 

# a = "hello"
# b = "World"
# print(a + " " + b)

# a = 42
# b = 43
# c = "hello world!"
# print( str(a) + b + " " + c)


# 11  format in string and integers / float
# marks = 45
# total = " your total marks is 100 and you got {}"
# obt = total.format(marks)
# print(obt)

# age = 24
# total = 100
# obt = 90
# res = " your age is {0} and your total marks {2} and obtain marks {1}"
# tot = res.format(age,obt,total)
# print(tot)


# 12 string slicing

# a = "hello world!"
# print(a[-3:-1])
# print(a[0:])
# print(a[:5])

# 13  split in string

# a = "hello AI class"
# b = a.split(" ")
# print(a, b)

# 14  uppar case lower case in string

# st = "Hello World!"
# up = st.upper()
# lo = st.lower()
# print(up, lo) 
# print( st.upper(), st.lower())
# st = "hello world"
# print(st.capitalize(),st.title())

# a = "hello"
# b = "world"
# print( a.capitalize() + " " + b.capitalize())

# 02 assignment solution 

# a = "jaranwala faisalabad lahore"
# print( a[0:1].upper() + a[1:9] , a[10:11].upper() + a[11:20] , a[21:22].upper() + a[22:]   )


# 15 replace methods 
# a = "hello"
# b = a.replace("h","H")
# print(b)

# 03 assignment home 

# st = "Jaranwala Faisalabad Lahore Karachi Multan" # don't use the slice method and replace first letters in small;


# 15 lists  

 # ls = list(("Lahore","Faisalabad","Jaranwala")) # constructor method

# ls= []
# ls = [ "Lahore","Faisalabad","Jaranwala"]
# print(type(ls), ls)
# print(type(ls), ls)

# ls = ["Lahore","Faisalabad","Jaranwala"]

# print(ls[2:])

# ls[1] = "Multan"
# ls[0:1] = [ "Karachi"]
# ls[2:] = ["Multan"]
# ls[1:2] = ["Peshawar"]
# ls[0:] = ["Lahore","Faislabad","Jaranwala","Peshawar"]
# print(ls)

# ls = ["Lahore","Faisalabad","Jaranwala"]
# ls.append("Peshawar")
# ls.insert(2,"Peshawar")
# ls.pop(0)
# ls.remove("Faisalabad")
# del ls

# ls.clear()
# print(ls)

# 16 for loops 

# ls = ["apple","banana","mango", "orange"]

# print(ls)
# for item in ls:
#     print(item)

# Assignments class 19/ 03/ 2025:______________________

# ls = ["lahore","faisalabad","jaranwala"]
# lp=[]
# for x in ls:
#     p = x[0:1].upper() + x[1:-1].lower() + x[-1:].upper()
#     lp.append(p)
#     print(p)
# print(lp)

# ls = [ "lahore","Faisalabad","jaranwala"]
# lp = []
# for x in ls:
#     lp.insert(0,x)
# print(lp)

# print(lp)
# print(lp)
# print(lp)

# 17 for loop while loop
# ls = ["Karachi", "Jaranwala", "Faisalabad"]
# for x in range(len(ls)):
#     print(ls[x])

# print("While loop started ")
# i = 0
# while i<len(ls):
#     print(ls[i])
#     i = i + 1

# 18 range
# for x in range(0,21,2):
#     print(x)

# 19 list comprensions
# ls = [x for x in range(2,10,2)]
# print(ls)

# ls = ["kaRAChi", "jarAnwaLa", "faiSAlabad","kiVi","test"]
# ls2 = [x for x in ls if ("a" or "v") in x] #first x is expression and second x is item
# # for x in ls:
# #     if "K" in x:
# #         ls2.append(x)
# print(19)
# print(ls2)

# ls2 = [x[0].upper()+x[1:-1].lower()+x[-1:].upper() for x in ls]
# print(ls2)


# 20 tuples
# tup = ("hello","world")
# print(type(tup)) #it is unchangeable - Ordered
# print(tup)

# tp = tuple(("hello",))
# ls = list((tp))
# ls.append("world")
# print(type(ls))
# tp = tuple((ls))
# print(type(tp))
# Primitive data type -> Pass by Value
# Non Primitive data type -> Pass by Reference

# tp1 = ("Tuple 1 ",)
# tp2 = ("Tuple 2 ",)
# tp3 = tp1 + tp2

# print(tp3)

# tup = ("Semester","Annual","Master","M phil","Bachelor")
# (tup1,tup2,tup3,*tup4) = tup # Unpacked || Destructrize
# print(type(tup1))
# print(tup1)
# print(type(tup2))
# print(tup2)
# print(type(tup3))
# print(tup3)
# print(type(tup4))
# print(tup4)


# 21 sets

# set = {"Hello", "World"}
# set1 = set(("Hello","World","!",bool("True")))
# set2 = set((True,False,1,0))
# set1.add("Python")
# set1.update(set2)
# set2.pop()
# set2.remove(0)
# set2.discard(0)
# set2.clear()
# del set2
# print(set2)
# dict = {"Hello": "World"}

# st1 = {"hello","world","!"}
# st2 = {"menu","food","hello"}
# st4 = {"program", "world"}

# st3 = st1.union(st2)
# st3 = st1 | st2

# st3 = st1.intersection(st2)
# st3 = st1 & st2

# # st3 = st1.difference(st2,st4)
# st3 = st1 - st2
# print(st3)


# dic = {"name" : "amna"}
# dic = set({"name" , "amna"})
# dic = dict({"name" : "amna"})
# dic = list(["name" , "amna"])
# dic = dict({"name" : "amna" , "age" : 20 , "color" : "white" , "alpha" : "1.09"})

# print(type(dic),dic, len(dic))
# print(dic.get("name"))
# print(dic["name"]) #Read

# dic["name"] = "bushra" #Update
# print(dic["name"]) #Read

# dic["color"] = "fade"
# dic.update({"color" : "white" , "alpha" : "1.09"})
# dic.popitem()
# dic.pop("alpha")
# print(dic.keys())
# print(dic.values())
# print(dic.items())

# del dic["name"]
# dic.clear()
# del dic #Error
# print(dic)

# 23 pass by reference and pass by value
# usually single data type is premitive and multiple data type is non-premitive
# a=10
# b=a
# a=20
# print(a,b)
# dic1 = {"name":"amna","age":20}
# dic2 = dic1
# dic1["name"] = "adil"
# print(dic1,dic2)


# 24 Copy dictionary ---
# dic1 = {"name":"amna","age":20}
# dic1["name"] = "zaid"
# dic2 = dic1.copy()
# dic2["name"] = "adil"
# dic2 = dict(dic1)
# dic1["name"] = "adil"
# print(dic1,dic2)


# 25 - Functions
# def s():
#     print("Hello world")
# s()

# def func(name , age):
#     print("Hello world! " + name , str(age))
# func("Akash" , 25)

# def func(name , age):
#     print("Hello world! " + name , str(age))
# func("Akash" , 25)

# def func(name, age):
#     print("Hello world! " + name , str(age))
# func("a",22)

# def func(name, *age):
#     print(name , str(age[0]))
# func("alina","25",30)

# def fun(**krgs):
#     print(krgs["name"] + str(krgs["age"]))
# fun(name = "akash", age = 34)

# def fun():
#     pass
# fun()

# 26 exception handling
# x = 23
# y = 24
# z = 25
# try:
#     print(x,a)
#     try:
#         print(x,y,z,a)
#     except:
#         print("inner error")

# except:
#     print("outer Error")
# finally:
#     print("this is always executed")


# 27 Anonymous function
# x = lambda a,b,c: (a/b)*c # Already return method
# print(x(5,2,2))

# ls1 = ["Faisalabad","jaranwala"]
# ls2 = ["Lahore1"]
# ls1.extend(ls2)
# print(ls1, type(ls1))

# tup1 = ("faisalabad","Jaranwala","Lahore")
# tup2 = (1,2,3,4,5,6,7)
# tup3 = tup2 + tup1
# print(tup3)

# st = {"hello","world","!"}
# st = set((False,True,"hello","world","!",0,1,"yes","no"))
# st2 = set(("philospher","hell menu"))

# st.add("philospher")
# st.update(st2)


# Functions ---------------------------------------------------------------:
# def sum():
#     print(type(str(42)), type(42))
# sum()

# def sum(a,b,c):
#     print(a+b-c)
# sum(10,20,10)

# def sum(a,b):
#     print("hello world {} : {}".format(a,b))
# sum(10,20)

# def sum(a,b):
#     print(f"hello world {a} : {b}")
# sum(10,20)

# def sum(a,*b,c):
#     print(f"hello world {a} : {b[0]} : {b[1]} : {b}")
# sum(10,20,30,40)

# def sum(a,**b):
    

# class Employee:
#     def setEmp(this,name,age):
#         this.name = name
#         this.age = age
#     def getEmp(q):
#         print(f"{q.name} : {q.age}")

# ab = Employee()
# cd = Employee()
# ab.setEmp("ab",23)
# ab.getEmp()  
# cd.setEmp("cd",4)
# cd.getEmp()

# class Employee:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#     def getEmp(self):
#         print(f"{self.name} : {self.age}")
# ab = Employee("Aslam",23)
# ab.getEmp()


# class Parent():
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
        
#     def name_age (self):
#         print(f"Name is : {self.name} , Age is : {self.age}")
# class Child(Parent):
#     def __init__(self,name, age, education):
#         self.education = education
#         super().__init__(name, age)
#     def edu(self):
#         print(f"Education is : {self.education}")
# ab = Child("Anam", 23,"SE")
# ab.name_age()
# ab.edu()


# class Parent():
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
        
#     def info (self,birthday):
#         print(f"Name is : {self.name} , Age is : {self.age}, Birthday is : {self.birthday}")
# class Child(Parent):
#     def __init__(self,name, age, education):
#         self.education = education
#         super().__init__(name, age)
#     def edu(self):
#         print(f"Education is : {self.education}")
# ab = Child("Anam", 23,"SE")
# ab.info("23-03-2000")
# ab.edu()


# class Parent():
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
        
#     def info(self, birthday):
#         # self.birthday = birthday  # Assign birthday to an instance attribute
#         print(f"Name is : {self.name} , Age is : {self.age}, Birthday is : {birthday}")

# class Child(Parent):
#     def __init__(self, name, age, education):
#         self.education = education
#         super().__init__(name, age)

#     def edu(self):
#         print(f"Education is : {self.education}")

# ab = Child("Anam", 23, "SE")
# ab.info("23-03-2000")  # This now works correctly
# ab.edu()