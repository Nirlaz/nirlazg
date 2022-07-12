#Noun --> object
#adjective -> attributes,property
#verb(action)-> behaviour,methode

class book: #attribute(property)and behaviour  
    #initialiser funtion
    def __init__(self,page,read):
        self.page=page
        self.read=read

    
c = book("attribute","method")
print(c.page)
# c.color="black"
print(c.read)
    