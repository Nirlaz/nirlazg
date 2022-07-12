
# Program to add two matrices using nested loop
 
# X = [[1,2,3],
#     [4 ,5,6],
#     [7 ,8,9]]
 
# Y = [[9,8,7],
#     [6,5,4],
#     [3,2,1]]
 
 
# result = [[0,0,0],
#         [0,0,0],
#         [0,0,0]]
 
# # iterate through rows
# for i in range(len(X)):  
# # iterate through columns
#     for j in range(len(X[0])):
#         result[i][j] = X[i][j] + Y[i][j]
 
# for r in result:
#     print(r)

#lambda function
#lambda p1,p2:p1+p2
# total =lambda a,b:a+b

# c=int(input("enter a and b"))
# d=int(input())
# print(total(c,d))

#map,filter
#map ma 2 ta kura passs garna milcha auta func  ra arko interable
# a=[1,2,3,4,5]
# def inc(n):
#     return n+1
# out=map(inc,a)
# print(list(out))
# print(list(map(lambda n:n+6,a)))

#task1
# name=["ram","shyam","sita","hari"]
# print(list(map(lambda s:s.title(),name)))
# print(list(map(str.title,name)))

# a=[1,2,3,4,5]
# print(list(filter(lambda n:n%2!=0,a)))

# email =[
#     "1@gmail.com",
#     "2@yahoo.com",
#     "3@gmail.com"
#     ]
# print(list(filter(lambda n:n.endswith("@gmail.com"),email)))

# a=[1,2,3,"python","apple",4,5,6]
# print(list(filter(lambda n:isinstance(n,int),a)))

