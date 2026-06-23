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

            # validate each score is in 0-100
            for s in student.score:
                if s < 0 or s > 100:
                    raise ValueError

        except ValueError:
            print('enter valid data')
            continue
        else:
            # compute grade from average (single grade value)
            avg = sum(student.score) / len(student.score)
            if avg >= 70 and avg <= 100:
                student.grade = 'A'
            elif avg >= 60:
                student.grade = 'B'
            elif avg >= 50:
                student.grade = 'C'
            elif avg >= 40:
                student.grade = 'D'
            elif avg >= 30:
                student.grade = 'E'
            else:
                student.grade = 'F'
            break

    return student.grade

score_grade = scoregrade()
