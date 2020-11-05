import database
import graph


print("////////////////////////")
print("    Class records       ")
print("////////////////////////")

while True:
	print("                                               ")
	print("/// Selcet an option ///")
	choice = eval(input("1. Add student\n2. Delete Student\n3. Add marks\n4. Show student table\n5. Search for a student\n6. Graph\n7. Quit\nOption: "))

	#choice 1 adding
	if choice == 1:
		
		counter = eval(input("Enter number of students to be entered: "))

		for i in range(counter):
			stud = input("Enter Student Number: ")
			name = input("Enter student name: ")
			surname = input("Enter student surname: ")
			database.add(stud,name,surname)
	#choice 2 deleting
	elif choice == 2:
		print("////////////////////////////////////////////////////////////////")
		print("    You about to delte a record be sure before proceeding       ")
		print("////////////////////////////////////////////////////////////////")
		stud = input("Enter Student Number: ")
		database.delete(stud)
	#choice 3 updating
	elif choice == 3:
		print("/// Welcome to mark update///")
		print("///Choose an option///")
		mark = eval(input("1. Math\n2. English\n3. GP\n4. History\nOption : "))

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
	elif choice == 4:
		database.table()

	#choce 5 searching
	elif choice == 5:
		database.search()

	elif choice == 6:
		graph.graph()

	elif choice == 7:
		print("///////////////////////////")
		print("         Thank You         ")
		print("///////////////////////////")
		break		