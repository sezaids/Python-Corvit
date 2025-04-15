# print("hello")
# print("hello" ,end="333")
# print("Zaid", 2 ,5, sep="-")
# d = None
# print(type(d))
# a = 4
# b = 2
# print(a+b) #Addition
# print(a-b) #Subtraction
# print(a*b) #Multiplication
# print(a**b) #Exponentiation
# print(a/b) #Division
# print(a//b) #Floor Division
# print(a%b) #Remainder
# print(a&b) #Bitwise AND
# print(a|b) #Bitwise OR
# print(a^b) #Bitwise XOR
# print(a<<b) #Bitwise left shift
# print(a>>b) #Bitwise right shift
# print(a==b) #Equal to
# print(a!=b) #Not equal to
# print(a>b) #Greater than
# print(a<b) #Less than

# Day 7&8 > Create Basic Calculator
# a = 7
# b = 3
# print(f"Sum of {a} and {b} is : {a + b}")
# print(f"Subtraction of {a} and {b} is : {a - b}")
# print(f"Multiplication of {a} and {b} is : {a * b}")
# print(f"Division of {a} and {b} is : {a / b}")

# # Day 9 > Conversion
# a = "5"
# b = "7"
# print(int(a) + int(b)) # Explicit Type Conversion > Conversion by programmer
# a = 6
# b = 5.7
# print(a + b) # Implicit Type Conversion > Conversion by Python (automatically)

# # Day 10 > Input Function
# a = input()
# print(a, type(a)) # Input function always returns string

# Day 11 > Strings
# name = "Zaid"
# print(name[0])
# print(name[1])
# print(name[2])
# print(name[3])

# for multiline_string we use triple quotes
# paragraph = """lorem ipsum dolor sit amet, consectetur adipiscing elit.
# Praesent commodo cursus magna, vel scelerisque nisl consectetur et.
# Donec id elit non mi porta gravida at eget metus.
# Nullam quis risus eget urna mollis ornare vel eu leo."""

# for X in paragraph:
#     print(X)

# a = "!@@@@!!Zaid@@@@@@@@@@@"
# print(a.strip("!"))
# print(a.rstrip("!"))
# print(a.lstrip("!"))
# print(len(name))
# print(name.center(7), len(name.center(10)))
# print(a.count("@"))
# print(a.startswith("!@@@"))
# print(a.endswith("@@@"))
# print(a.endswith("id", 4, 11)) #checking 4 to 10 index to find id at last

# greet = "Hello World, This is python programming class toDAy is my second day."
# greet = "Hello World"
# print(greet.find("ish")) # tells index of first occurrence in the string and return "-1" if not found
# print(greet.index("ish")) # tells index of first occurrence in the string and return "error" if not found
# print(greet.isalnum()) # if string is made of a-z, A-Z, 0-9 > Return "true", else "false" 
# print(greet.isalpha()) # if string is made of a-z, A-Z > Return "true", else "false"
# print(greet.islower()) # check all char in string is in lower case
# print(greet.isupper()) # check all char in string is in upper case
# print(greet.swapcase()) # convert lowercase to uppercase and vice versa
# print(greet.isprintable()) # if we use "\n" in string it returns false because it is not return printable.
# print(greet.isspace()) # if a string is made of only spaces (using spacebar or tab) it returns true, else false
# print(greet.istitle()) # Rerurn true if first letter on each word is capital, else return false
# print(greet.title()) # Convert first letter of each word in capital

# import time
# timestamp = time.strftime('%H:%M:%S')
# print(timestamp)
# timestamp = int(time.strftime('%H'))
# # print(timestamp)
# # timestamp = time.strftime('%M')
# # print(timestamp)
# # timestamp = time.strftime('%S')
# # print(timestamp)

# if (timestamp >= 6 and timestamp < 12):
#     print("Good Morning")
# elif(timestamp >= 12 and timestamp < 18):
#     print("Good Afternoon")
# elif(timestamp >= 18 and timestamp < 21):
#     print("Good Evening")
# else:
#     print("Good Night")


#Match case

# dayNum = int(input("Enter day number : "))
# match dayNum:
#     case 1:
#         print("Today is monday")
#     case 2:
#         print("Today is tuesday")
#     case 3:
#         print("Today is wednesday")
#     case 4:
#         print("Today is Thrusday")
#     case 5:
#         print("today is friday")
#     case 6:
#         print("today is saturday")
#     case 7:
#         print("today is sunday")
#     case _ if (dayNum < 1):
#         print("Invalid and small number")
#     case _ if (dayNum > 7):
#         print("invalid and large number")

# names = ["Usama", "Talha", "Zaid", "Asma", "Hafsa"]
# for name in names:
#     print("\n")
#     for i in name:
#         print(i)
#     print(name)

# for num in range(3,11,3):
#     print(num)

# i = int(input("Enter any numberr : "))
# while(i % 2 == 0):
#     print(i)
#     i = int(input("Enter any numberr : "))
# else:
#     print(i)
#     print("Sorry! You entered odd number")

# while True:
#   number = int(input("Enter a positive number: "))
#   print(number)
#   if not number > 0:
#     break

# for i in range (1, 11):
    # # if(i % 2 == 0):
    # #     continue
    # if (i >= 7):
    #     break
    # print("7 X",i,"=",7*i)

# def name(fname="zaid", mname="usama", lname="talha"):
    # print(fname , mname , lname)
# name(lname="usama")

# marks = [74,73,52,"Zaid",7,8,9,1,2,3,4,5] # List > changeable, can be different data types,
# print(marks[3])
# if 52 in marks:
#     print("Yes")
# else:
#     print("No")
# if "ai" in "Zaid":
#     print("yes")
# else:
#     print("no")
# print(marks[1::3])

# lst = [i*i for i in range(5)]
# print(lst)

# ls = [1,2,3,4,5,6,7,8,9]
# ms = [11,12,13,14,15]
# ns = ls + ms #Concatenation 2 list = using "extend()" method
# ls.append(13) # add number at last
# ls.sort()
# ls.sort(reverse=True)
# print(ls.index(1)) # find where first occurr of number in list
# print(ls.count(9)) # count how many time number available
# ms = ls.copy()
# ms[0] = 0
# ls.extend(ms) # add every elements of ms[] in the ls[]
# print(ls)
# print(ns)
# print(ms)

# tup = (1,2,34,57,89,463)
# print(tup[0])
# print(tup[1])
# print(tup[2])
# print(tup[5])
# if 89 in tup:
#     print("89 is present in list")
# tup1 = tup[1:5:2]
# print(tup1)

# tup1 = ("A","B","C","D","E","F","...")
# tup2 = ("T","U","V","W","X","Y","Z")
# lis1 = list(tup1)
# lis1.append("Q")
# tup3 = tuple(lis1)
# alphabet = tup1 + tup2
# print(alphabet)
# print(tup3)
# tup = (1,2,1,3,3,3,1,2,6,5)
# print(tup.count(6))
# print(tup.index(1,3,9)) # Here index of 1 is find in between 3 to 9
# price = 23.5678436
# name = "zaid"
# print(f"Price is {price:.2f}")
# print(f"My name is {{name}}") # if we want to add curly braces in output

# ls = [0,1]
# def fibonacci(n):
#     if (n == 0) or (n==1):
#         return n
#     fnm1 = fibonacci(n-1)
    
#     fnm2 = fibonacci(n-2)
#     ls.append(fnm1)
#     fn = fnm1 + fnm2
#     return fn

# print(fibonacci(0))
# print(fibonacci(1))
# print(fibonacci(2))
# print(fibonacci(3))
# print(fibonacci(4))
# print(fibonacci(5))
# print(fibonacci(6))
# print(fibonacci(7))

# set1 = set() # If you want to create empty set then we will create by using "set()". we can't use "{}" bcz it represent 'dict' not 'set'

# s1 = {1,2,3,4}
# s2 = {3,4,5,6}
# print(s1.union(s2)) # Union of S1 and s2
# print(s1.intersection(s2)) # Intersection of s1 and s2
# s1.update(s2) # it adds the values s2 in s1 and it will update "s1"
# s1.intersection_update(s2) # it is intersection of s2 and s1 and update it in "s1"
# print(s1.symmetric_difference(s2)) # symmetric means (s1 U s2)-(s1 n s2) => {1,2,3,4,5,6}-{3,4} => {1,2,5,6}
# s1.symmetric_difference_update(s2) # symmetric means (s1 U s2)-(s1 n s2) => {1,2,3,4,5,6}-{3,4} => {1,2,5,6} and update in "s1"
# print(s1.difference(s2)) # s1 - s2
# s1.difference_update(s2) # s1 - s2
# print(s1.isdisjoint(s2)) # if in both set not any common value then it will return 'True'
# print(s1.issuperset(s2)) # if all value of s2 in s1 then s1 is 'superset' of s2
# print(s1.issubset(s2)) # if all value of s2 in s1 then s1 is 'superset' of s2
# s1.add(7) # if you want to add one element in the list
# s1.update({8,9,10}) # if you want to add more than one elements
# s1.remove(1) # remove method raise error if element will not present in the list
# s1.discard(1) # discard method does not raise error if element will not present in the list
# s1.pop()
# del s1
# s1.clear()
# print(s1, type(s1))

# dict = {
#     29481: "Zaid", 135: "Ali",
#     29472: "Subhan",
#     29456: "Saim"
# }

# 2 method but same work \/ and difference is written in from of function
# print(dict[29481]) # it will throw error if key will not exist
# print(dict.get(29481)) # it will "not" throw error if key will not exist and then it will return 'None'

# print(dict.keys()) # gives keys of every element
# print(dict.values()) # gives values of every element
# print(dict.items()) # gives key-values pairs
# for key in dict.keys():
#     print(dict[key]) # finding a value by keys() using loop

# for key,value in dict.items():
#     print(f"[{key} : {value}]") # finding a key-value by items() using loop

# emp1 = {111:90, 112:85, 113:99, 114:66}
# emp2 = {121:56, 122:75, 123:47, 124:97}
# emp1.update(emp2) # Update the emp1 by adding emp2's key-value pairs
# emp1.clear() # clear the 'dict'
# emp1.pop(113) # Remove the key-value pair as input key of element
# emp1.popitem() # Remove the last key-value pair
# del emp1 # delete full 'dict'
# del emp1[111] # Remove the key-value pair as input key of element
# print(emp1)

# for i in range(6):
#     print(i)
#     if i == 4:
#         break
# else:
#     print("i not found")

# a = int(input("Enter number : "))
# print(f"Table of {a}\n")

# try:
#     for i in range(1,11):
#         print(f"{a} X {i} = {a*i}")
# except Exception as e:
#     print(e)

# try:
#     num = int(input("Enter an integer: "))
#     a = [6, 3]
#     print(a[num])
# except ValueError:
#     print("Number entered is not integer.")
# except IndexError:
#     print("Index Error.")
# finally: # 'finally' always executed.
#     print("I will always executed.")

# def func():
#     try:
#         li = [2,4,6,8,10]
#         num = int(input("Enter index number : "))
#         print(li[num])
#         return 1
#     except:
#         print("Error occurred.")
#         return 0
    
#     finally: # 'finally' will also run although 'try' and 'except' 'return'
#         print("I will always executed.")
# x = func()
# print(x)