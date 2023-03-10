# Student Database

students = ['Steven Frederick', 'Sophia Petrillo',
            'Rose Nylund', 'Blanche Devereaux']
hometown = ['Farmington Hills', 'Sicily', 'Miami', 'Atlanta']
fav_food = ['Pizza', 'Pasta', 'Cookies', 'Cupcakes']

#fuctions are below.

def student_search(advance):
    if advance == 'y':
        student_select = input('Thank you. Which student would you like to learn more about?'
                               ' Enter a number 1-4:\n')

        # make function
        student_select = int(student_select)
        if 1 <= student_select <= len(students):
            if student_select == 1:
                print(f'Student {student_select} is {students[student_select - 1]}. What would you like to'
                      f' know?')
                stu_info = True
                while stu_info == True:
                    info_input = input("Enter 'hometown' or 'favorite food'\n")
                    info_input = info_input.lower()
                    if (info_input == 'hometown'):
                        print(f'{students[student_select - 1]} is from {hometown[student_select - 1]}')
                        cont = input('Would you like to learn about another student? (y/n) ')
                        cont = cont.lower()
                        if cont == 'n':
                            print('Thank you')
                            stu_info = False
                            return stu_info
                            # return switch?? for function
                        else:
                            stu_info = False
                            return stu_info
                    elif (
                            info_input == 'favorite food' or info_input == 'food'):  # can take value of favorite food or food, both start with f
                        print(f"{students[student_select - 1]}'s favorite food is {fav_food[student_select - 1]}")
                        cont = input('Would you like to learn about another student? (y/n) ')
                        cont = cont.lower()
                        if cont == 'n':
                            print('Thank you!')
                            stu_info = False
                            # return switch?? for function
                            return stu_info
                        else:
                            stu_info = False
                            return stu_info

                    else:
                        print('Please check your spelling or enter the categories given.')
            elif student_select == 2:
                print(f'Student {student_select} is {students[student_select - 1]}. What would you like to'
                      f' know?')
                stu_info = True
                while stu_info == True:
                    info_input = input("Enter 'hometown' or 'favorite food'\n")
                    info_input = info_input.lower()
                    if (info_input == 'hometown'):
                        print(f'{students[student_select - 1]} is from {hometown[student_select - 1]}')
                        cont = input('Would you like to learn about another student? (y/n) ')
                        cont = cont.lower()
                        if cont == 'n':
                            print('Thank you')
                            stu_info = False
                            # return switch?? for function
                            return stu_info
                        else:
                            stu_info = False
                            return stu_info
                    elif (
                            info_input == 'favorite food' or info_input == 'food'):  # can take value of favorite food or food, both start with f
                        print(f"{students[student_select - 1]}'s favorite food is {fav_food[student_select - 1]}")
                        cont = input('Would you like to learn about another student? (y/n) ')
                        cont = cont.lower()
                        if cont == 'n':
                            print('Thank you!')
                            stu_info = False
                            # return switch?? for function
                            return stu_info
                        else:
                            stu_info = False
                            return stu_info
                    else:
                        print('Please check your spelling or enter the categories given.')
            elif student_select == 3:
                print(f'Student {student_select} is {students[student_select - 1]}. What would you like to'
                      f' know?')
                stu_info = True
                while stu_info == True:
                    info_input = input("Enter 'hometown' or 'favorite food'\n")
                    info_input = info_input.lower()
                    if (info_input == 'hometown'):
                        print(f'{students[student_select - 1]} is from {hometown[student_select - 1]}')
                        cont = input('Would you like to learn about another student? (y/n) ')
                        cont = cont.lower()
                        if cont == 'n':
                            print('Thank you')
                            stu_info = False
                            # return switch?? for function
                            return stu_info
                        else:
                            stu_info = False
                            return stu_info
                    elif (
                            info_input == 'favorite food' or info_input == 'food'):  # can take value of favorite food or food, both start with f
                        print(f"{students[student_select - 1]}'s favorite food is {fav_food[student_select - 1]}")
                        cont = input('Would you like to learn about another student? (y/n) ')
                        cont = cont.lower()
                        if cont == 'n':
                            print('Thank you!')
                            stu_info = False
                            # return switch?? for function
                            return stu_info
                        else:
                            stu_info = False
                            return stu_info
                    else:
                        print('Please check your spelling or enter the categories given.')
            else:
                print(f'Student {student_select} is {students[student_select - 1]}. What would you like to'
                      f' know?')
                stu_info = True
                while stu_info == True:
                    info_input = input("Enter 'hometown' or 'favorite food'\n")
                    info_input = info_input.lower()
                    if (info_input == 'hometown'):
                        print(f'{students[student_select - 1]} is from {hometown[student_select - 1]}')
                        cont = input('Would you like to learn about another student? (y/n) ')
                        cont = cont.lower()
                        if cont == 'n':
                            print('Thank you')
                            stu_info = False
                            # return switch?? for function
                            return stu_info
                        else:
                            stu_info = False
                            return stu_info
                    elif (
                            info_input == 'favorite food' or info_input == 'food'):  # can take value of favorite food or food, both start with f
                        print(f"{students[student_select - 1]}'s favorite food is {fav_food[student_select - 1]}")
                        cont = input('Would you like to learn about another student? (y/n) ')
                        cont = cont.lower()
                        if cont == 'n':
                            print('Thank you!')
                            stu_info = False
                            # return switch?? for function
                            return stu_info
                        else:
                            stu_info = False
                            return stu_info
                    else:
                        print('Please check your spelling or enter the categories given.')

        else:
            print('Sorry. That number is out of range, please try again.')
    else:
        print(advance)
        off = True
        return off

def stu_name_search(name_search):
    if name_search == 'Steven Frederick' or name_search == 'Steven' or name_search == 'Frederick':
        print(f'Student 1 is {students[0]}. What would you like to'
              f' know?')
        stu_info = True
        while stu_info == True:
            info_input = input("Enter 'hometown' or 'favorite food'\n")
            info_input = info_input.lower()
            if (info_input == 'hometown'):
                print(f'{students[0]} is from {hometown[0]}')
                cont = input('Would you like to learn about another student? (y/n) ')
                cont = cont.lower()
                if cont == 'n':
                    print('Thank you')
                    stu_info = False
                    return stu_info
                    # return switch?? for function
                else:
                    stu_info = False
                    return stu_info
            elif (
                    info_input == 'favorite food' or info_input == 'food'):  # can take value of favorite food or food, both start with f
                print(f"{students[0]}'s favorite food is {fav_food[0]}")
                cont = input('Would you like to learn about another student? (y/n) ')
                cont = cont.lower()
                if cont == 'n':
                    print('Thank you!')
                    stu_info = False
                    # return switch?? for function
                    return stu_info
                else:
                    stu_info = False
                    return stu_info

            else:
                print('Please check your spelling or enter the categories given.')
    elif name_search == 'Sophia Petrillo' or name_search == 'Sally' or name_search == 'Petrillo':
        print(f'Student 2 is {students[1]}. What would you like to'
              f' know?')
        stu_info = True
        while stu_info == True:
            info_input = input("Enter 'hometown' or 'favorite food'\n")
            info_input = info_input.lower()
            if (info_input == 'hometown'):
                print(f'{students[1]} is from {hometown[1]}')
                cont = input('Would you like to learn about another student? (y/n) ')
                cont = cont.lower()
                if cont == 'n':
                    print('Thank you')
                    stu_info = False
                    # return switch?? for function
                    return stu_info
                else:
                    stu_info = False
                    return stu_info
            elif (
                    info_input == 'favorite food' or info_input == 'food'):  # can take value of favorite food or food, both start with f
                print(f"{students[1]}'s favorite food is {fav_food[1]}")
                cont = input('Would you like to learn about another student? (y/n) ')
                cont = cont.lower()
                if cont == 'n':
                    print('Thank you!')
                    stu_info = False
                    # return switch?? for function
                    return stu_info
                else:
                    stu_info = False
                    return stu_info
            else:
                print('Please check your spelling or enter the categories given.')
    elif name_search == 'Rose Nylund' or name_search == 'Rose' or name_search == 'Nylund':
        print(f'Student 3 is {students[2]}. What would you like to'
              f' know?')
        stu_info = True
        while stu_info == True:
            info_input = input("Enter 'hometown' or 'favorite food'\n")
            info_input = info_input.lower()
            if (info_input == 'hometown'):
                print(f'{students[2]} is from {hometown[2]}')
                cont = input('Would you like to learn about another student? (y/n) ')
                cont = cont.lower()
                if cont == 'n':
                    print('Thank you')
                    stu_info = False
                    # return switch?? for function
                    return stu_info
                else:
                    stu_info = False
                    return stu_info
            elif (
                    info_input == 'favorite food' or info_input == 'food'):  # can take value of favorite food or food, both start with f
                print(f"{students[2]}'s favorite food is {fav_food[2]}")
                cont = input('Would you like to learn about another student? (y/n) ')
                cont = cont.lower()
                if cont == 'n':
                    print('Thank you!')
                    stu_info = False
                    # return switch?? for function
                    return stu_info
                else:
                    stu_info = False
                    return stu_info
            else:
                print('Please check your spelling or enter the categories given.')
    elif name_search == 'Blanche Devereaux' or name_search == 'Blanche' or name_search == 'Devereaux':
        print(f'Student 4 is {students[3]}. What would you like to'
              f' know?')
        stu_info = True
        while stu_info == True:
            info_input = input("Enter 'hometown' or 'favorite food'\n")
            info_input = info_input.lower()
            if (info_input == 'hometown'):
                print(f'{students[3]} is from {hometown[3]}')
                cont = input('Would you like to learn about another student? (y/n) ')
                cont = cont.lower()
                if cont == 'n':
                    print('Thank you')
                    stu_info = False
                    # return switch?? for function
                    return stu_info
                else:
                    stu_info = False
                    return stu_info
            elif (
                    info_input == 'favorite food' or info_input == 'food'):  # can take value of favorite food or food, both start with f
                print(f"{students[3]}'s favorite food is {fav_food[3]}")
                cont = input('Would you like to learn about another student? (y/n) ')
                cont = cont.lower()
                if cont == 'n':
                    print('Thank you!')
                    stu_info = False
                    # return switch?? for function
                    return stu_info
                else:
                    stu_info = False
                    return stu_info
            else:
                print('Please check your spelling or enter the categories given.')
    else:
        print('Sorry. That number is out of range, please try again.')


print('Welcome!')
off = False
while off != True:
    studentlist_input = input("Would you like to see a list of the entire "
                              "class? (y/n) ")
    studentlist_input = studentlist_input.lower()
    if (studentlist_input == 'y'):
        for s in students:
            print(f'Student Number {students.index(s)+1}: ', s)
            pass
    else:
        advance = input('Would you like to continue? (y/n) ')
        advance.lower()
        if advance == 'y':
            name_search = input("Would you like to search by name? (y/n) ")
            name_search.lower()
            if name_search == 'y':
                stu_name = input("Enter student name: ")
                stu_name_search(stu_name)
            else:
                student_search(advance)
        else:
            print('Thank you. <END PROGRAM>')
            off = True
            break
