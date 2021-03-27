import sqlite3

# uncomment the section below to create table and database
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


# adding student
def add(stud, name, surname):
    con = sqlite3.connect("students.db")
    c = con.cursor()
    info = [stud, name, surname]
    try:  # to check if student ID already taken
        c.execute("INSERT INTO students (StudID,Name,Surname) VALUES (?,?,?)", info)
        print("Student: " + name + " " + surname + " has been created with Student ID: " + str(stud))
        con.commit()
        con.close()
    except sqlite3.IntegrityError:
        print("Student ID already used")


# deleting student
def delete(stud):
    con = sqlite3.connect("students.db")
    c = con.cursor()
    find = "SELECT Name, Surname FROM students WHERE StudID = '{}'".format(stud)
    c.execute(find)
    print(str(c.fetchone()) + " will be deleted")
    remove = "DELETE FROM students WHERE StudID = ?"
    choice = input("Press Yes to accept or No to cancel: ")
    if choice.upper() == "YES":
        c.execute(remove, (stud,))
        print("Student has been deleted")
        con.commit()
        con.close()
    elif choice.upper() == "NO":
        print("Operation canceled")
        pass
    else:
        print("Option chosen is invalid, Please Try again.")


# searching for a student
def search(stud):
    con = sqlite3.connect("students.db")
    c = con.cursor()
    find = "SELECT * FROM students WHERE StudID = '{}'".format(stud)
    c.execute(find)
    print("STUDID", "\tNAME", "\tSNAME", "\tMATHS", "\tENGLI", "\tGENP", "\tHIST")
    print("-----------------------------------------------------------")
    print(c.fetchone())
    con.commit()
    con.close()


# updating maths mark
def math():
    con = sqlite3.connect("students.db")
    c = con.cursor()
    stud = input("Enter Student number: ")
    maths = eval(input("Enter Math Percentage: "))
    if 0 <= maths <= 100:
        c.execute("UPDATE students SET Math =?  WHERE StudID =?", (math, stud))
        print("Mark has been updated")
    else:
        print("Mark out range")
    con.commit()
    con.close()


# updating english mark
def english():
    con = sqlite3.connect("students.db")
    c = con.cursor()
    stud = input("Enter Student number: ")
    englishs = eval(input("Enter English Percentage: "))
    if 0 <= englishs <= 100:
        c.execute("UPDATE students SET English =?  WHERE StudID =?", (english, stud))
        print("Mark has been updated")
    else:
        print("Mark out range")
    con.commit()
    con.close()


# updating gp mark
def gp():
    con = sqlite3.connect("students.db")
    c = con.cursor()
    stud = input("Enter Student number: ")
    gps = eval(input("Enter G.P Percentage: "))
    if 0 <= gps <= 100:
        c.execute("UPDATE students SET GP =?  WHERE StudID =?", (gp, stud))
        print("Mark has been updated")
    else:
        print("Mark out range")
    con.commit()
    con.close()


# updating history mark
def history():
    con = sqlite3.connect("students.db")
    c = con.cursor()
    stud = input("Enter Student number: ")
    historys = eval(input("Enter History Percentage: "))
    if 0 <= historys <= 100:
        c.execute("UPDATE students SET History =?  WHERE StudID =?", (history, stud))
        print("Mark has been updated")
    else:
        print("Mark out range")
    con.commit()
    con.close()


def update_all_marks():
    con = sqlite3.connect('students.db')
    c = con.cursor()
    stud = eval(input("Enter Student Number: "))
    maths = eval(input("Enter Math Percentage: "))
    englishs = eval(input("Enter English Percentage: "))
    gps = eval(input("Enter GP Percentage: "))
    historys = eval(input("Enter History Percentage: "))

    if 0 <= historys & maths & gps & englishs <= 100:
        c.execute("UPDATE students SET Math = ?, English = ?, GP = ?, History = ? WHERE StudID = ?",
                  (math, english, gp, history, stud))
        print("Marks have been updated")
    else:
        print("Please make sure all marks are in range.")
    con.commit()
    con.close()


# Showing the whole class
def table():
    print(
        """
        Select sort option:

        id: sort by student id
        sur: sort by surname
        per: sort by percentage
        """
    )
    option = input(">> ")

    if option == "id":

        con = sqlite3.connect("students.db")
        c = con.cursor()
        c.execute("SELECT * FROM  students ORDER BY StudID ASC")
        results = c.fetchall()

        print("ID", "\tNAME", "\tSNAME", "\tMATHS", "\tENGLI", "\tGENP", "\tHIST")
        print("-----------------------------------------------------------")
        for results in results:
            print(
                results[0],
                "\t",
                results[1],
                "\t",
                results[2],
                "\t",
                results[3],
                "\t",
                results[4],
                "\t",
                results[5],
                "\t",
                results[6],
            )

    elif option == "sur":
        con = sqlite3.connect("students.db")
        c = con.cursor()
        c.execute("SELECT * FROM  students ORDER BY Surname ASC")
        results = c.fetchall()

        print("STUDID", "\tNAME", "\tSNAME", "\tMATHS", "\tENGLI", "\tGENP", "\tHIST")
        print("-----------------------------------------------------------")
        for results in results:
            print(
                results[0],
                "\t",
                results[1],
                "\t",
                results[2],
                "\t",
                results[3],
                "\t",
                results[4],
                "\t",
                results[5],
                "\t",
                results[6],
            )

    elif option == "per":
        print("""
            Math: use math percentage
            English: use english percentage
            GP: use gp percentage
            History: use history percentage
        """)

        sub = input(">> ")

        per = eval(input("Enter lower bound percentage: "))

        con = sqlite3.connect("students.db")
        c = con.cursor()
        find = "SELECT * FROM students WHERE {} >= '{}'".format(sub, per)
        c.execute(find)
        results = c.fetchall()

        print("STUDID", "\tNAME", "\tSNAME", "\tMATHS", "\tENGLI", "\tGENP", "\tHIST")
        print("-----------------------------------------------------------")
        for results in results:
            print(
                results[0],
                "\t",
                results[1],
                "\t",
                results[2],
                "\t",
                results[3],
                "\t",
                results[4],
                "\t",
                results[5],
                "\t",
                results[6],
            )


# shows current students and student IDs
def current():
    con = sqlite3.connect('students.db')
    c = con.cursor()
    c.execute("SELECT StudID, Name, Surname FROM  students ORDER BY StudID ASC")
    results = c.fetchall()
    print("STUDID", "\tNAME", "\tSNAME")
    print("---------------------")
    for results in results:
        print(
            results[0],
            "\t",
            results[1],
            "\t",
            results[2],
        )
