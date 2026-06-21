class Courses():
    def __init__(self,courses,name,score):
        self.courses = courses
        self.name = name
        self.score = score

    def data(self):
        self.name = input('name: ')
        self.score = int(input('score: '))

        print(f'{self.name} {self.score}')

course = Courses(['MTH','PHY','CHM','STA','COS'],name = '',score = '')

course.data()



