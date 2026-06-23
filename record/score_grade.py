from record.student_class import student

def score_grade():
    while True:
        try:
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

            elif student.score < 40 and student.score >= 30:
                student.grade = 'E'
                print(f'{student.name} your grade is {student.grade}')

            elif student.score < 30:
                student.grade = 'F'
                print(f'{student.name} your grade is {student.grade}')

        break