import sqlite3


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

#adding student info
def add(stud,name,surname):
	con = sqlite3.connect('students.db')
	c = con.cursor()
	info = [(stud),(name),(surname)]
	c.execute("INSERT INTO students (StudID,Name,Surname) VALUES (?,?,?)",info)
	con.commit()
	con.close()

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

def search():
	stud = input("Enter Student number: ")
	con = sqlite3.connect('students.db')
	c = con.cursor()
	find ="SELECT * FROM students WHERE StudID = '{}'".format(stud)
	c.execute(find)
	print(c.fetchone())
	con.commit()
	con.close()


def all(math,english,gp,history):
	con = sqlite3.connect('students.db')
	c = con.cursor()
	marks = [(math),(english),(gp),(history)]
	c.execute("INSERT INTO students (Math,English,GP,History) VALUES (?,?,?,?)",marks)
	con.commit()
	con.close()



def math(stud,math):
	con = sqlite3.connect('students.db')
	c = con.cursor()
	studid = 'SELECT StudID FROM students WHERE StudID = ?'
	result = c.execute(delete,(studid,))
	maths = math
	c.execute("INSERT INTO students (Math) WHERE StudID = ? VALUES (?)",maths)
	con.commit()
	con.close()


