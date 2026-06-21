class Courses():
    def __init__(self,courses,name,score):
        self.courses = courses
        self.name = name
        self.score = score

def data():
    try:
        course.name = str(input('name: '))
        course.score = int(input('score: '))

    except ValueError:
        print('Invalid datatype \n name = "STRING" and score = "INTEGER"')

    else:
        print(course.name)
        print(course.score)


course = Courses(['MTH','PHY','CHM','STA','COS'],name = '',score = '')

    

data()



