from record.student import student

def data():
    while True:
        name = input('Enter name: ').strip()

        if name == '':
            print('enter name')
            continue

        if any(ch.isdigit() for ch in name):
            print('enter name: name must not contain numbers')
            continue

        student.name = name.upper()
        print(f'WELCOME {student.name}\n')
        break

student_data = data()
