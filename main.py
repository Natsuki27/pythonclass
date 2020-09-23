import pickle
pickle.dump("Homework_2", "wb")
f = open("Homework_2")
student_list = {}
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
                if ID in f.student_list:
                    val = f.student_list[ID]
                    print(ID + " is used for")
                    print(val)
                    print("Please select different ID. Try again.")
                    f.close()

                else:
                    f.wight[ID] = last_name + "," + first_name
                    print(last_name + " is added")
                    f.close()

            else:
                print("Please use numbers for ID. Try again.")

        elif option == "d":
            answer = input("Enter the student's ID to remove>>>")
            if answer in f:
                del [answer]
                f.close()

                print("Deleted")

            else:
                print(answer + " is an invalid ID. Please check.")

        elif option == "p":
            print("select a to display all students")
            print("select b to display individual student")
            option2 = input(">>>")
            if option2 == "a":
                print(f.student_list)
                f.close()

            elif option2 == "b":
                ID: str = input("Please input the student's ID>>>")
                if ID.isnumeric():
                    val = f.student_list[ID]
                    print(val)
                    f.close()

                else:
                    print("Please input correct ID#. Try again.")

            else:
                print("Invalid option. Please try again.")

        elif option == "q":
            running = False

    else:
        print("Please select a,d,p or q")
