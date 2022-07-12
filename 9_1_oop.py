"""
    1.class and objects
    2.Inhertance
    3.polymorephism
    -method overrideing
    4.Abstraction
"""
class Enticer:#attribute(property)and behaviour  
    #initialiser funtion
    def __init__(self,model,color):
        self.model=model
        self.color=color

    
c = Enticer("lu 2 pa","Red")
print(c.color)
# c.color="black"
print(c.model)
    
