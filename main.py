import os
import pickle
import re


def load():
    master_list = {}
    if os.path.exists('master_list.txt'):
        with open("master_list.txt", "rb") as input_ID:
            pickle.load(input_ID)
    return master_list


def save():
    with open("master_list.txt", "wb") as output:
        pickle.dump(student_list, output)


student_list = load()
running = True
while running:

    print("Enter a to add a student")
    print("Enter d to remove a student")
    print("Enter p to display the student list")
    print("Enter q to quit")
    option = input(">>>")

    if option == "a" or option == "d" or option == "p" or option == "q":

        if option == "a":
            last_name = input("Enter the student's last name>>>")
            first_name = input("Enter the student's first name>>>")
            ID = input("Enter the student ID#>>>")

            if ID.isnumeric():
                if ID in student_list:
                    val = [ID]
                    print(ID + " is used for")
                    print(val)
                    print('Please select different ID. Try again.')

                else:
                    student_list[ID] = last_name + "," + first_name
                    save()
                    print(last_name + " is added")

            else:
                print("Please use numbers for ID. Try again.")

        elif option == "d":
            answer = input("Enter the student's ID to remove>>>")
            if answer in student_list:
                del [answer]
                save()
                print("Deleted")

            else:
                print(answer + " is an invalid ID. Please check.")

        elif option == "p":
            print("select a to display all students")
            print("select b to display individual student")
            option2 = input(">>>")
            if option2 == "a":
                print(student_list)

            elif option2 == "b":
                ID: str = input("Please input the student's ID>>>")
                if ID.isnumeric():
                    val = student_list[ID]
                    print(val)

                else:
                    print("Please input correct ID#. Try again.")

            else:
                print("Invalid option. Please try again.")

        elif option == "q":
            running = False

    else:
        print("Please select a,d,p or q")
