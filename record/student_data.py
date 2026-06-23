from record.student import student

def data():
    while True:
        try:
            student.name = str(input('Enter name: '))

            if student.name == '':
                raise ValueError
   
        except ValueError:
            continue

        else:
            print(student)
        break

student_data = data()
