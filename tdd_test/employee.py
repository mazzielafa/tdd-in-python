# from sys import last_traceback


class Employee:

    def __init__(self, name, passw, email, username):
        self.name = name
        self.email = email
        self.username = username
        self.passw = passw

    def addEmployee(self):
        return f"Please create a {self.username} and {self.passw}"