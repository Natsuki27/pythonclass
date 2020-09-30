import os
import pickle


class Student:
    """This is a class definition of q student object"""

    def __init__(self, first_name="", last_name="", ID=0):
        """This is a class constructor the __init__ is short initialization.a
        This will create an instance of the class. type subjects: object"""
        self.__first_name = first
        # the double __ allows for the member to be private not accessible outside of the classes
        self.__last_name = last
        self.__ID = newId
        self.__subjects = {}

    def set_first_name(self, first_name: str):
        self.__first_name = first_name

    def set_last_name(self, last_name: str):
        pass

    def set_ID(self, ID: int):
        pass

    def set_subject(self, Subject: str):
        pass

    def get_first_name(self):
        return self.__last_name

    def get_last_name(self):
        return self.__last_name

    def get_ID(self):
        return self.__ID

    def get_subject(self):
        return self.__subject

    def add_grade(self, subject: str, grade: int):

        if subject in self.__subjects:
            self.__subjects[subject].append(grade)  # add grade to existing list
        else:
            self.__subjects[subject] = [grade]

    def __get_average_for_subject(self, subject: str):  # note methods can be private to :)
        """This prints the average for the subject requested"""
        result = 0.0

        if subject in self.__subjects and len(self.__subjects[subject]) > 0:
            result = sum(self.__subjects[subject]) / len(self.__subjects[subject])
        return result

    def print_letter_grade(self):
        """Prints all the letter grades for each subject"""
        for key in self.__subjects:
            grade = self.__get_average_for_subject(key)
            if grade >= 90:
                result = "A"
            elif grade >= 80:
                result = "B"
            elif grade >= 70:
                result = "C"
            elif grade >= 60:
                result = "D"
            else:
                result = "F"
            print("Subject: %s Grade: %s" % (key, result))

    def print_letter_grade(self):
        """Prints all the letter grades for each subject"""
        for key in self.__subjects:
            grade = self.__get_average_for_subject(key)
            if grade >= 90:
                result = "A"
            elif grade >= 80:
                result = "B"
            elif grade >= 70:
                result = "C"
            elif grade >= 60:
                result = "D"
            else:
                result = "F"
            print("Subject: %s Grade: %s" % (key, result))

    def print_student_info(self):
        """This method prints out the student information"""
        print("ID: %s" % self.__ID)
        print("Name: %s, %s" % (self.__last_name, self.__first_name))

    def __str__(self):
        """This method overrides the parents __str___ method for our custom addition"""
        # this is the method that is called with print command
        return "ID: %s Name: %s, %s" % (self.__ID, self.__last_name, self.__first_name)

    def __repr__(self):
        return self.__str__(self)


def load():
    master_list = {}
    if os.path.exists('master_list'):
        with open("master_list", "rb") as input_ID:
            master_list = pickle.load(input_ID)
    return master_list


def save():
    with open("master_list", "wb") as output:
        pickle.dump(student_list, output)


student_list = load()
running = True
while running:

    print("Enter a to add a student")
    print("Enter d to remove a student")
    print("Enter s to select a subject and add grade")
    print("Enter p to display the student list")
    print("Enter q to quit")
    option = input(">>>")

    if option == "a" or option == "d" or option == "s" or option == option == "p" or option == "q":

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
                    student_list[ID] = Student(first_name, last_name, ID)
                    print(last_name + " is added")
            else:
                print("Please use numbers for ID. Try again.")

        elif option == "d":
            answer = input("Enter the student's ID to remove>>>")
            if answer in student_list:
                del student_list[answer]
                print("Deleted")

            else:
                print(answer + " is an invalid ID. Please check.")

        elif option == "s":
            ID = input("please enter the student ID>>>")
            if ID.isnumeric():
                if ID in student_list:
                    print("Do you want to select a subject for " + student_list[ID].get_last_name() + "_?")
                    answer = input("enter y for yes. enter n for no >>>")

                    if answer == "y":
                        print("select subject from following options.")
                        print("e:English, m:Math")
                        subject = input(">>>")

                        if subject == "e":
                            score = input("enter grade for English>>>")

                            if score.isnumeric():
                                student_list[ID].add_grade("English", int(score))
                                student_list[ID].print_student_info()
                                student_list[ID].print_letter_grade()

                            else:
                                print("please enter correct grade. try again from menu")

                        elif subject == "m":
                            score = input("enter grade for Math>>>")
                            if score.isnumeric():
                                student_list[ID].add_grade("Math", int(score))
                                student_list[ID].print_student_info()
                                student_list[ID].print_letter_grade()

                            else:
                                print("please enter correct grade. try again from menu")

                        else:
                            print("please enter y or n. please try again from menu")

                    elif answer == "n":
                        print("back to menu")

                    else:
                        print("invalid select. enter y or n.")

                else:
                    print("please enter valid ID numbers. Try again.")

            else:
                print("please enter valid ID numbers. Try again.")

        elif option == "p":
            print("select a to display all students")
            print("select b to display individual student")
            option2 = input(">>>")
            if option2 == "a":
                for ID in student_list:
                    student_list[ID].print_student_info()

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
            save()
            running = False

    else:
        print("Please select a,d,p or q")
