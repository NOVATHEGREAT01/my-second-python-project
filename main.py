from record.student import student
from record.student_data import student_data
from record.score_grade import score_grade

def student_record():
    print(student_data)
    print(score_grade)
    print(f'{student.name} your result are as followed\n')
    print(f'{student.courses[0]} = {student.score[0]}({student.grade})')
    print(f'{student.courses[1]} = {student.score[1]}({student.grade})')
    print(f'{student.courses[2]} = {student.score[2]}({student.grade})')
    print(f'{student.courses[3]} = {student.score[3]}({student.grade})')
    print(f'{student.courses[4]} = {student.score[4]}({student.grade})\n')
    print(f'Your average is {sum(student.score)/len(student.score)}')

student_record()