#1 break and continue
# for i in range(1,10):
#  n=int(input("Enter num:"))
#  if n==9:
#    continue
#  print(n)
# else:
#     print("tata bye bye")

# print(sum(list(range(1,10,2))))
# username="r@gmail.com"
# password="123@abcd"
# new=[]
# n=input("Enter the password")
# for i in range(0,len(password)):
#     if password[i]==n[i]:
# print("login successful")
#     else:
#         continue
#1 Task to take check usename and password
# username="r@gmail.com"
# password="123@abcd"
# uname=input("Enter your name")
# pode=input("enter your password")
# while uname != username or pode  != password:
#     uname=input("Enter your name")
#     pode=input("enter your password")
# else:
#     print("logged in")

# from re import A


# a=[]
# b=tuple()



a=[('1','2','3'),('5','6','7'),('8','9','0')]
b=a.pop(0)
print(b)
c=a.pop(1)
print(c)
d=a.pop(-1)
print(d)
e=b[0]+b[1]+b[2]
f=c[0]+c[1]+c[2]
g=d[0]+d[1]+d[2]
print(e)
print(f)
print(g)

h=sum(e,f)
i=sum(h,g)
print(i)