
# protoperties ={
#     "data":{
#         "profile":[
#             {"name":"Ram",
#             "rank":1,
#             "contact":["09384"]
#             },
#             {
#                 "name":"site",
#                 "rank":2,
#                 "contact":["987654","988339"]

#             }
            
#         ]
#     },
#     "total_count":3,
# }
# profiles=protoperties.get("data").get("profile")
# print("xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx")
# for profile in profiles:
#     print(f"name:{profile.get('name')}")
#     print(f"rank:{profile.get('rank')}")
#     t=profile.get("contact")
#     i=1
#     for v in t:
#         print(f"contact{i}:{v}")
#         i=i+1
def profile(name,contact,address):
    print(f"Name:{name}")
    print(f"contact:{contact}")
    print(f"address:{address}")
profile("ram","03303","ktm")#positioanl argument
print("##################")
profile(name="ram",address="ktm",contact="03303")#keyword argument