class Student():
    def __init__(self,courses,name,score,grade):
        self.courses = courses
        self.name = name
        self.score = score
        self.grade = grade

    def __str__(self):
        return f'WELCOME {self.name}'
    
student = Student(courses = ['MTH','PHY','STA','COS','GST'],name = '',score = [0,0,0,0,0],grade = '')