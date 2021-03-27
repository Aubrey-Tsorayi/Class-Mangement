# update3
import database

import graph

print("Class records 'alpha' ")
print()

while True:

    print("This are the current students and their student number/id.")
    database.current()
    print()

    print("Select an option")
    print(
        """
    add: Add student
    delete: Delete student
    marks: Add marks to a student
    students: Show student table
    search: Search for a student
    visual: visualizes a students marks using a graph
    graph: Graph
    quit: Quit
    """
    )

    choice = input(">> ")

    # choice 1 adding
    if choice.lower() == "add":

        counter = eval(input("Enter number of students to be entered: "))

        for i in range(counter):
            stud = eval(input("Enter Student Number: "))
            name = input("Enter student name: ")
            surname = input("Enter student surname: ")
            database.add(stud, name, surname)
            input("Enter to continue....")

    # choice 2 deleting
    elif choice.lower() == "delete":
        print("////////////////////////////////////////////////////////////////")
        print("    You about to delete a record be sure before proceeding       ")
        print("////////////////////////////////////////////////////////////////")
        stud = input("Enter Student Number: ")
        database.delete(stud)
        input("Enter to continue....")

    # choice 3 updating
    elif choice.lower() == "marks":
        print("/// Welcome to mark update///")
        print("///Choose an option///")
        print(
            """
		math: adding maths marks
		english: adding english marks
		gp: adding gp marks
		history: adding history marks
        all: adding all marks at once
		"""
        )

        mark = input(">> ")
        if mark == "math":
            database.math()
            input("Enter to continue....")

        elif mark == "english":
            database.english()
            input("Enter to continue....")

        elif mark == "gp":
            database.gp()
            input("Enter to continue....")

        elif mark == "history":
            database.history()
            input("Enter to continue....")

        elif mark == "all":
            database.update_all_marks()
            input("Enter to continue......")

        else:
            print("Invalid option, try again")

    # choice 4 data presentation
    elif choice.lower() == "students":
        database.table()
        input("Enter to continue....")

    # choice 5 searching
    elif choice.lower() == "search":
        stud = input("Enter Student number: ")
        database.search(stud)
        input("Enter to continue....")

    elif choice.lower() == "graph":
        graph.graph()
        input("Enter to continue....")

    elif choice.lower() == "visual":
        stud = eval(input("Enter student number: "))
        graph.student_average(stud)
        input("Enter to continue....")

    elif choice == "quit":
        print(
            """
        Are sure yo want to exit:
                No
                Yes
        """
        )
        op = input(">> ")

        if op.lower() == "no":
            continue
        elif op.lower() == "yes":
            print("###################")
            print("    THANK YOU      ")
            print("###################")
            break
        else:
            print("Invalid option.")
    else:
        print("Invalid option, try again")
