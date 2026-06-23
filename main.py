class Student():
    def __init__(self,courses,name,score,grade):
        self.students = courses
        self.name = name
        self.score = score
        self.grade = grade

    def __str__(self):
        return f'Hello {self.name}'
    
student = Student(['MTH','PHY','CHM','STA','COS'],name = '',score = '',grade = '')
    
def data():
    while True:
        try:
            student.name = str(input('name: '))
            if student.name == '':
                continue
            
            student.score = int(input('score: '))
            if student.score == '':
                continue

        except ValueError:
            print('enter valid data')
            continue

        else:
            if student.score >= 70:
                student.grade = 'A'
                print(f'{student.name} your grade is {student.grade}')

            elif student.score < 70 and student.score >= 60:
                student.grade = 'B'
                print(f'{student.name} your grade is {student.grade}')

            elif student.score < 60 and student.score >= 50:
                student.grade = 'c'
                print(f'{student.name} your grade is {student.grade}')

            elif student.score < 50 and student.score >= 40:
                student.grade = 'D'
                print(f'{student.name} your grade is {student.grade}')

            elif student.score < 40:
                student.grade = 'F'
                print(f'{student.name} your grade is {student.grade}')

        break

data()



