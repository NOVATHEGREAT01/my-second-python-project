from record.student import student

def scoregrade():
    while True:
        try:
            print('Enter the scores respectively\n')
            student.score[0] = int(input('MTH score: '))
            student.score[1] = int(input('PHY score: '))
            student.score[2] = int(input('STA score: '))
            student.score[3] = int(input('COS score: '))
            student.score[4] = int(input('GST score: '))
            if student.score == '':
                raise ValueError

        except ValueError:
            print('enter valid data')
            continue

        else:
            if student.score[0 or 1 or 2 or 3 or 4] >= 70 and student.score[0 or 1 or 2 or 3 or 4] <= 100:
                student.grade = 'A'

            elif student.score[0 or 1 or 2 or 3 or 4] < 70 and student.score[0 or 1 or 2 or 3 or 4] >= 60:
                student.grade = 'B'

            elif student.score[0 or 1 or 2 or 3 or 4] < 60 and student.score[0 or 1 or 2 or 3 or 4] >= 50:
                student.grade = 'c'

            elif student.score[0 or 1 or 2 or 3 or 4] < 50 and student.score[0 or 1 or 2 or 3 or 4] >= 40:
                student.grade = 'D'

            elif student.score[0 or 1 or 2 or 3 or 4] < 40 and student.score[0 or 1 or 2 or 3 or 4] >= 30:
                student.grade = 'E'

            elif student.score[0 or 1 or 2 or 3 or 4] < 30 :
                student.grade = 'F'

            break

score_grade = scoregrade()


