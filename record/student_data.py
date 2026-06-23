from record.student import student

def data():
    while True:
        try:
            student.name = input('Enter name: ')
            student.name = student.name.upper()
            
            if student.name.strip() == '':
                raise ValueError

            if any(ch.isdigit() for ch in student.name):
                raise ValueError

        except ValueError:
            print('enter name')
            continue
        else:
            print(f'WELCOME {student.name}\n')
            break

    return student.name

student_data = data()
