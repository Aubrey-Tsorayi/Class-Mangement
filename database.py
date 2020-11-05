import sqlite3


#uncomment the section below to create table and database
"""con = sqlite3.connect('students.db')
c = con.cursor()
c.execute('''CREATE TABLE students (
	StudID text,
	Name text,
	Surname text,
	Math real,
	English real,
	GP real,
	History real
)''')
print('Done!')
con.commit()
con.close()"""

#adding student
def add(stud,name,surname):
	con = sqlite3.connect('students.db')
	c = con.cursor()
	info = [(stud),(name),(surname)]
	c.execute("INSERT INTO students (StudID,Name,Surname) VALUES (?,?,?)",info)
	con.commit()
	con.close()

#deleting student
def delete(stud):
	con = sqlite3.connect('students.db')
	c = con.cursor()
	delete = 'DELETE FROM students WHERE StudID = ?'
	choice = input("Press Y to accept or N to cancel: ")
	if choice.upper() == 'Y' :
		c.execute(delete,(stud,))
		print("Student has been deleted")
		con.commit()
		con.close()
	elif choice.upper() == 'N' :
		print("Operation canceled")
		pass
	else:
		print("Option chosen is invaild, Please Try agian.")

#searching for a student
def search():
	stud = input("Enter Student number: ")
	con = sqlite3.connect('students.db')
	c = con.cursor()
	find ="SELECT * FROM students WHERE StudID = '{}'".format(stud)
	c.execute(find)
	print("STUDID","\tNAME","\tSNAME","\tMATHS","\tENGLI","\tGENP","\tHIST")
	print("-----------------------------------------------------------")
	print(c.fetchone())
	con.commit()
	con.close()

#updating maths mark
def math():
	con = sqlite3.connect('students.db')
	c = con.cursor()
	stud = input("Enter Student number: ")
	math = eval(input("Enter Math Percentage: "))
	if math>0 and math<100:
		c.execute("UPDATE students SET Math =?  WHERE StudID =?",(math,stud))
		print("Mark has been updated")
	else:
		print("Mark out range")
	con.commit()
	con.close()

#updating english mark
def english():
	con = sqlite3.connect('students.db')
	c = con.cursor()
	stud = input("Enter Student number: ")
	english = eval(input("Enter English Percentage: "))
	if english>0 and english<100:
		c.execute("UPDATE students SET English =?  WHERE StudID =?",(english,stud))
		print("Mark has been updated")
	else:
		print("Mark out range")
	con.commit()
	con.close()

#updating gp mark
def gp():
	con = sqlite3.connect('students.db')
	c = con.cursor()
	stud = input("Enter Student number: ")
	gp = eval(input("Enter G.P Percentage: "))
	if gp>0 and gp<100:
		c.execute("UPDATE students SET GP =?  WHERE StudID =?",(gp,stud))
		print("Mark has been updated")
	else:
		print("Mark out range")
	con.commit()
	con.close()

#updating history mark
def history():
	con = sqlite3.connect('students.db')
	c = con.cursor()
	stud = input("Enter Student number: ")
	history = eval(input("Enter History Percentage: "))
	if history>0 and history<100:
		c.execute("UPDATE students SET History =?  WHERE StudID =?",(history,stud))
		print("Mark has been updated")
	else:
		print("Mark out range")
	con.commit()
	con.close()

#Showing the whole class
def table():
	con = sqlite3.connect('students.db')
	c = con.cursor()
	c.execute("SELECT * FROM  students")
	results = c.fetchall()

	print("STUDID","\tNAME","\tSNAME","\tMATHS","\tENGLI","\tGENP","\tHIST")
	print("-----------------------------------------------------------")
	for results in results:
		print(results[0] , "\t" , results[1] , "\t" , results[2] , "\t" , results[3] , "\t" , results[4] , "\t" , results[5] , "\t" , results[6])

		
