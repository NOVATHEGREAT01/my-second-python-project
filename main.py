class Courses():
    def __init__(self,courses,name,score,grade):
        self.courses = courses
        self.name = name
        self.score = score
        self.grade = grade

    def __str__(self):
        return f'Hello {self.name}'
    
def data():
    while True:
        try:
            course.name = str(input('name: '))
            if course.name == '':
                data()
            
            course.score = int(input('score: '))
            if course.score == '':
                data()

        except ValueError:
            data()

        else:
            if course.score >= 70:
                course.grade = 'A'
                print(f'{course.name} your grade is {course.grade}')

            elif course.score < 70 and course.score >= 60:
                course.grade = 'B'
                print(f'{course.name} your grade is {course.grade}')

            elif course.score < 60 and course.score >= 50:
                course.grade = 'c'
                print(f'{course.name} your grade is {course.grade}')

            elif course.score < 50 and course.score >= 40:
                course.grade = 'D'
                print(f'{course.name} your grade is {course.grade}')

            elif course.score < 40:
                course.grade = 'F'
                print(f'{course.name} your grade is {course.grade}')

        break

course = Courses(['MTH','PHY','CHM','STA','COS'],name = '',score = '',grade = '')

data()



