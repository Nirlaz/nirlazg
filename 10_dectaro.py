# def div(a,b):
#     print(a/b)

# def smart_div(func):
#     def inner(a,b):
#         if a<b:
#             a,b=b,a
#         return func(a,b)

#     return inner
# div1 = smart_div(div)
# div1(2,4)

# def decorate_function(func):
#     def wrapper():
#         print("Hello student!")
#         func()
#         print("khatam tata bye bye")
#     return wrapper
# @decorate_function
# def welcome():
#     print("welcome studentes!")
# welcome()


# def nirlaz():
#     print("I am Nirlaz")

# def gyawali(func):
#     def inner():
#         print("I am from gulmi")
#         func()
#         print("i study in himalayan college of engineering")
#     return inner
# a=gyawali(nirlaz)
# a()

# def smart_divsion(func):
#     def inner(a,b):
#         if b==0:
#             return "chal bhosdeka b ma zero rakhxas"
#         else:
#             print("la mam fuley b ko value zero haney nas ramro gars")
#             return func(a,b)
#     return inner
# @smart_divsion
# def divison(a,b):
#     return a/b
# print(divison(10,2))
# print(divison(10,0))


heros=['spiderman','thor','hulk','ironman','captain america']
print(len(heros))\
# heros.insert(6,"black panter")
heros.insert(6,"black panter")
print(heros)
heros.remove("black panter")
print(heros)
heros.insert(4,"black panter")
print(heros)
heros[1:3]=["doctor strange"]
print(heros)
heros.sort()
print(heros)

