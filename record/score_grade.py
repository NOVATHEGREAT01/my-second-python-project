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

            for s in student.score:
                if s < 0 or s > 100:
                    raise ValueError

        except ValueError:
            print('enter valid data')
            continue
        else:
            average = sum(student.score) / len(student.score)
            if average >= 70 and average <= 100:
                student.grade = 'A'
            elif average >= 60:
                student.grade = 'B'
            elif average >= 50:
                student.grade = 'C'
            elif average >= 40:
                student.grade = 'D'
            elif average >= 30:
                student.grade = 'E'
            else:
                student.grade = 'F'
            break

    return student.grade

score_grade = scoregrade()
