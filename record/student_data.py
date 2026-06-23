from record.student import student

def data():
    while True:
        try:
            student.name = str(input('Enter name: '))
            student.name = student.name.upper()

            if student.name == '':
                raise ValueError
   
        except ValueError:
            print('enter name')
            continue

        else:
            print(f'WELCOME {student.name}\n')
        break

student_data = data()
