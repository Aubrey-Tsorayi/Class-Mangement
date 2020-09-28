import database

print("////////////////////////")
print("    Class records       ")
print("////////////////////////")

while True:
	print("                                               ")
	print("/// Selcet an option ///")
	choice = eval(input("1. Add student 2. Delete Student 3. Add marks 4. Show student table 5. Quit  :"))

	#choice 1
	if choice == 1:

		counter = eval(input("Enter number of students to be entered: "))

		for i in range(counter):
			stud = input("Enter Student Number: ")
			name = input("Enter student name: ")
			surname = input("Enter student surname: ")
			database.add(stud,name,surname)

	elif choice == 2:
		print("////////////////////////////////////////////////////////////////")
		print("    You about to delte a record be sure before proceeding       ")
		print("////////////////////////////////////////////////////////////////")
		stud = input("Enter Student Number: ")
		database.delete(stud)

	elif choice == 3:
		print("/// Welcome to mark update///")
		stud = input("Enter Student Number: ")
		print("///Choose an option///")
		mark = eval(input("1. Math 2. English 3. GP 4. History 5. All : "))

		if mark == 1:
			math = input("Enter Math Percentage: ")
			if math > 0 and math < 100:
				database.math(math,stud)
		elif mark == 2:
			english = input("Enter English Percentage: ")

		elif mark == 3:
			gp = input("Enter General Paper Percentage: ")

		elif mark == 4:
			history = input("Enter History Percentage: ")

		elif mark == 5:
			math = input("Enter Math Percentage: ")
			english = input("Enter English Percentage: ")
			gp = input("Enter General Paper Percentage: ")
			history = input("Enter History Percentage: ")
			database.all(stud,math,english,gp,history)
		else:
			print("Invalid option, try again")

		
print("Test Complete")
		