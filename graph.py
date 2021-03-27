import sqlite3
import matplotlib.pyplot as plt


# calculating average of subjects
def graph():
    con = sqlite3.connect("students.db")
    c = con.cursor()
    result = "SELECT avg(Math), avg(English), avg(GP), avg(History) FROM students"
    c.execute(result)
    results = c.fetchone()

    activities = ["Math", "English", "GP", "History"]

    colors = ["r", "y", "g", "b"]

    # plotting the pie chart
    plt.pie(
        results,
        labels=activities,
        colors=colors,
        startangle=90,
        shadow=True,
        explode=(0, 0, 0.1, 0),
        radius=1,
        autopct="%1.1f%%",
    )

    plt.title("Subject Averages")

    # plotting legend
    plt.legend()

    # showing the plot
    plt.show()


def student_average(stud):
    con = sqlite3.connect("students.db")
    c = con.cursor()
    find = "SELECT Name, Surname FROM students WHERE StudID = '{}'".format(stud)
    c.execute(find)
    student_name = c.fetchone()
    result = "SELECT Math, English, GP, History FROM students WHERE StudID = '{}'".format(stud)
    c.execute(result)
    results = c.fetchone()

    data = ["Math", "English", "GP", "History"]

    colours = ["r", "g", "y", "b"]

    left = [1, 2, 3, 4]

    plt.bar(left,
            results,
            tick_label=data,
            width=0.8,
            color=colours)

    plt.xlabel('Subjects')

    plt.ylabel('Percentage/%')

    plt.title("Subject percentages for: " + str(student_name[0]) + " " + str(student_name[1]))

    plt.show()
