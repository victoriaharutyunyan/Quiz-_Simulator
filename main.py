import Instructor
import student

def main1():
    print("Welcome to Quiz Simulator App")

    while True:
        user_type = input("Are you an instructor or a student?")
        if (user_type.lower() == "instructor"):
            Instructor.main()
            break
        elif (user_type.lower() == "student"):
              student.main()
              break
        else:
            print("Wrong input,please try again"),
    print ("Thanks for using the app")
main1()
