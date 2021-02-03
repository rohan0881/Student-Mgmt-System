import os //to check the operating system compatibility 
import platform //check the platform we are working on

global studentList //decalre a function student List
studentList=["James","Harry","Michael","Richard"] //student List will be holding the list of all students from the college

def studentManagement(): //function for student Management
    print("Welcome To Jain College Management System:->") //Welcome to Trinity College Management System
    print("[Choice 1: Showing the list of student:]") //Choice 1-> Showing The List of Students
    print("[Choice 2: Add a new student:]") // Choice 2-> Add a new Student
    print("[Choice 3: Searching a student:]") //Choice 3-> Searching a Student
    print("[Choice 4: Deleting a student]") //Choice 4 -> Deleting a Student

        x=int(input("Enter a choice:")) //Take the input from the user
    except valueError: //Exception if it involves a value error
        exit("This is not a number") //print "This is not a number"
    else:
        print("") //if not then print blankabstract 
    if(x==1): //check if choice is 1
        print("Student List:->") //print the student list
    for students in studentList: //check for students in student list
        print("".format(students)) //print Students
    elif(x==2): //check if choice is
        student_new=input("Enter a new student") //Store the new student entries in student_new 
    if(student_new in studentList): //check if student_new exists in student List
        print("This student is already in the table".fomat(student_new)) //print The student already exits in our records
    else:
        studentList.append(student_new) //if not present in the list add it to the student List
        print("New student added successfully".format(student_new)) //print New Student Added successfully
    for students in studentList: //again check for students in student list
        print("".format(students)) //print 
    elif(x==3): //check if choice is 3
        studentsearching=input("Choose student name to search:->") //enter the name of the student you want to search and store it in student_searching
        try:
    if(studentsearching in studentList): //check if student searching in student List
        print("There is a record found for this student".format(studentsearching)) //print Record Found for this student!.
    else:
        print("There is no record found of this student:".format(studentsearching)) //Else print no record found for this student
    elif(x==4): //if choice is equal to 4
        studentdelete=input("Choose a student name to delete:->") //enter the student name you wish to delete
        if(studentdelete in studentList): //if student_delete in student List
            studentList.remove(studentdelete) //if he exists in the list, then delete him from the list
        for students in studentList: //check for students in student List
            print("".format(students)) //print 
        else:
            print("There is no record found for this student:".format(studentdelete)) //else print no record found for this student
    def continueAgain(): //function to continue the iterations again
        running_again=input("Do you want to continue the process yes/no") //check if the user wants to continue the iterations
        if(running_again.lower()=='yes'): //check if he enters 'yes'
            if(platform.system()=='windows'): //check if his platform is 'windows'
                print(os.system('cls')) //print os-system
            else:
                print(os.system(clear)) //else print clear
                studentManagement() //call the student Management System Function as a function call
                continueAgain() //continue again function call
        else:
                quit() //else Quit

continueAgain() //otherwise Lets Start Again!!.
