class Student():
    def __init__(self,corecourses,name,score,grade):
        self.students = corecourses
        self.name = name
        self.score = score
        self.grade = grade

    def __str__(self):
        return f'Hello {self.name}'
    
student = Student(['MTH','PHY','CHM','STA','COS'],name = '',score = '',grade = '')

class EmptyError(Exception):
    pass