
students = ['Steven Frederick', 'Sophia Petrillo',
            'Rose Nylund', 'Blanche Devereaux']
hometown = ['Farmington Hills', 'Sicily', 'Miami', 'Atlanta']
fav_food = ['Pizza', 'Pasta', 'Cookies', 'Cupcakes']

def name_search(name):
    if name in students:
        print(f'{name} is Student {students.index(name) + 1}. Their hometown is {hometown[students.index(name)]}\n'
            f'and their favorite food is {fav_food[students.index(name)]}.')
    else:
        print("That is not a current student, please try again.")



switch = True
while switch == True:
    student_list = input("Would you like to see a list of all students? (y/n) ").lower()
    if student_list == 'y':
        for student in students:
            print(student)
    else:
        pass
    name_select = input('Would you like to search by name? (y/n) ').lower()
    while name_select == 'y':
        name = input("What is the student's full name? ").title()
        name_search(name)
        cont = input('Would you like to learn about another student? \n').lower()
        if cont == 'n':
            break
    else:

        student_select = int(input("Which student would you like to know more about? Enter a number 1-4:\n"))
        if student_select in range(len(students)+1):
            print(f"Student {student_select} is {students[student_select-1]}. What would you like to know?")
            while student_select != 0:
                category = input("Enter 'hometown' or 'favorite food'\n").lower()
                if category == 'hometown':
                    print(f"{students[student_select-1]} is from {hometown[student_select-1]}")
                    break

                elif category == 'favorite food' or category == 'food':
                    print(f"{students[student_select-1]}'s favorite food is {fav_food[student_select-1]}")
                    break
                else:
                    print("That category does not exist. Please try again.")
                    continue
            another = input("Would you like to learn about another student? (y/n) ").lower()
            if another == 'n':
                print('Thank you! <END PROGRAM>')
                break
        else:
            print("number out of range")
            break
