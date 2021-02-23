#update2
import database

import graph

print("Class records")

while True:
    print("Select an option")
	print("""
    add: Add student
    delete: Delete student
    marks: Add marks to a student
    students: Show student table
    search: Search for a student
    graph: Graph
    quit: Quit
    """)

	choice = input(">> ")

	#choice 1 adding
	if choice.lower() == "add":
		
		counter = eval(input("Enter number of students to be entered: "))

		for i in range(counter):
			stud = input("Enter Student Number: ")
			name = input("Enter student name: ")
			surname = input("Enter student surname: ")
			database.add(stud,name,surname)
	#choice 2 deleting
	elif choice.lower() == "delete":
		print("////////////////////////////////////////////////////////////////")
		print("    You about to delte a record be sure before proceeding       ")
		print("////////////////////////////////////////////////////////////////")
		stud = input("Enter Student Number: ")
		database.delete(stud)
	#choice 3 updating
	elif choice.lower() == "marks":
		print("/// Welcome to mark update///")
		print("///Choose an option///")
		option = print("""
		math: adding maths marks
		english: adding english marks
		gp: adding gp marks
		history: adding history marks
		""")

		mark = input(">>: ")
		if mark == 1:
			database.math()

		elif mark == 2:
			database.english()

		elif mark == 3:
			database.gp()

		elif mark == 4:
			database.history()
		else:
			print("Invalid option, try again")

	#choice 4 data presentation
	elif choice,lower() == "students":
		database.table()

	#choce 5 searching
	elif choice.lower() == "search":
		database.search()

	elif choice.lower() == "graph":
		graph.graph()

	elif choice == "quit":
		print("THANK YOU")
		break	
	else:
		print("Invalid option, try again")	