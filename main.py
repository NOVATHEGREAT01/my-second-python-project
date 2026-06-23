from record.classes import student
from record.classes import EmptyError

def data():
    while True:
        try:
            student.name = str(input('Enter name: '))
            student.name = student.name.upper()

            if student.name == '':
                raise EmptyError
   
        except ValueError:
            print('name must be in alphabets')
            continue

        except EmptyError:
            print('enter a name')
            continue

        else:
            print(student)

        break


data()
            
