# def adder(*num):
#     sum = 0
    
#     for n in num:
#         sum = sum + n

#     print("Sum:",sum)

# adder(3,5)
# adder(4,5,6,7)
# adder(1,2,3,5,6)
# def intro(**data):
#     print("\nData type of argument:",type(data))

#     for key, value in data.items():
#         print("{} is {}".format(key,value))

# intro(Firstname="Sita", Lastname="Sharma", Age=22, Phone=1234567890)
# intro(Firstname="John", Lastname="Wood", Email="johnwood@nomail.com", Country="Wakanda", Age=25, Phone=9876543210)



#Function ko kam ho yo timiley bujnu parcha bujeu k nai
#day 8 



# def pro1(num1,num2,num3):
#     print(num1*num2*num3)
# ans=pro1(10,2,3)
# print(f"Anwer yo ho kta:{ans}")

# def pro2(num1,num2,num3):
#     return(num1*num2*num3)
# ans=pro2(10,2,3)
# print(f"Anwer yo ho kta:{ans}")



#*args
# def example(*args,**kwargs):
#     print(args,kwargs)
# example(1,2,3,4,5,name="Nirlaz punit puspa raj kumar dev ",address="ruru-4,baletaksar,gulmi")

# def profile(name,contact,address):
#     print(f"{name}:{name}")
#     print(f"{name}:{address}")
#     print(f"{name}:{contact}")
# app={"name":"nirlaz","address":"baletaksar","contact":93393993}
# profile(**app)

#task 2
# def squarerootofsum(func,num1,num2):
#     return func(num1,num2)**0.5
# def add(num1,num2):
#     return num1+num2
# print(squarerootofsum(add,10,15))

# task 3 

# def outer_func():
#     def first_child():
#         print("i am first child")
#     def second_child():
#         print("i am second child")
#     first_child()
#     second_child()

# outer_func()

#task3


# a=int(input("Enter the inital value"))
# b=int(input("enter second number"))
# operator=input("Enter the operation you want to perform")

# def calculator(operator,a,b):
#     def add():
#         return a+b
#     def sub():
#         if a>b:
#             return a-b
#         else:
#             return b-a
#     def prod():
#         return a*b
#     if operator=="+":
#         return add
#     elif operator=="-":
#         return sub
#     elif operator=="*":
#         return prod
# c=calculator(operator,a,b)
# print(c())

#Q.no 1)