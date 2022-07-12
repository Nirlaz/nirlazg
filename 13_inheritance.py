
class user:
    def __init__(self,_id,username,pwd):
        self._id = _id
        self.username = username
        self.password = pwd
    def login(self,uname,pwd):
        if self.username == uname and self.password == pwd:
            return "logged in successfully."
        return "unauthorised user"

class teacher(user):
    def __init__(self,_id,username,pwd,designation):
        super().__init__(_id,username,pwd) #yasley chai class username call garcha
        self.designation = designation

class student(user):
    def __init__(self,_id,username,pwd,faculty):
        super().__init__(_id,username,pwd)
        self.faculty = faculty

t = teacher(1,"teacher","teacher","professor")
s = student(2,"student","student","bct2076")
uname = input("Enter your username")
pwd = input("Enter your passwored")
#  print(t.login(uname,pwd))
print(s.login(uname,pwd))

        