class Courses():
    def __init__(self,courses,name,score):
        self.courses = courses
        self.name = name
        self.score = score

    def __str__(self):
        return f'Hello {self.name}'
    
def data():
    while True:
        try:
            course.name = str(input('name: '))
            if course.name == '':
                d
            course.score = int(input('score: '))
            if course.score == '':
                d

        except ValueError:
            print('Invalid datatype \n name = "STRING" and score = "INTEGER"')

        else:
            print(course.name)
            print(course.score)
        break
        



course = Courses(['MTH','PHY','CHM','STA','COS'],name = '',score = '')


d = data()



