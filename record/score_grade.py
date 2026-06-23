from record.classes import student

def scoregrade():
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
                print(student.grade)

            elif student.score < 70 and student.score >= 60:
                student.grade = 'B'
                print(student.grade)

            elif student.score < 60 and student.score >= 50:
                student.grade = 'c'
                print(student.grade)

            elif student.score < 50 and student.score >= 40:
                student.grade = 'D'
                print(student.grade)

            elif student.score < 40 and student.score >= 30:
                student.grade = 'E'
                print(student.grade)

            elif student.score < 30:
                student.grade = 'F'
                print(student.grade)

        break

score_grade = scoregrade()


