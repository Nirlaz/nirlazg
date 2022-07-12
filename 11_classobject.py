class page:
    def __init__(self,page_number,content):
        self.page_number = page_number
        self.content= content
    def read(self):
        print(f"reading{self.content} or page number {self.page_number}")
    @staticmethod
    def print_to_printer(content):
        print(f"printing....")
        print(content)
    def __repr__(self):
        return self.content
    
p=page(1,"This is new paragraph.")
p.read()
page.print_to_printer("This is sentence")


class book:
    def __init__(self,title,pages):
        self.title = title
        self.pages = pages
    def number_of_pages(self):
        return len(self.pages)
    def add_pae(self,page):
        self.pages.append(page)
    def __str__(self):
        return self.title
    def __repr__(self):
        return self.title
    def get_content(self,page_number):
        for i in self.pages:
            if i.page_number==page_number:
                return i.content
        return "page not faound"    

pages=[]
for i in range (1,6):
    p = page(i,f"This is paragraph{i}.")
    pages.append(p)
b = book("maths",pages)
# print(f"number of pages:{b.number_of_pages()}")
p= page(6,"this is new page")
b.add_pae(p)
# print(b)
# print(b.pages)
# print(p)
# print(b.get_content(10))

print(b.__dict__)

try:
    n1=int(input("Enter number:"))
    n2=int(input("Enter number:"))

except valueerror:
        print("cannot conver into interger")
except nameerror:
        print("variable not defined")
else:
    print(n1+n2)
