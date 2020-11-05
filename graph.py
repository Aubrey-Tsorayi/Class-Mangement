import sqlite3
import matplotlib.pyplot as plt 

#calculating average of subjects
def graph():
	con = sqlite3.connect('students.db')
	c = con.cursor()
	result = "SELECT avg(Math), avg(English), avg(GP), avg(History) FROM students"
	c.execute(result)
	results = c.fetchone()

	activities = ['Math', 'English', 'GP', 'History']

	colors = ['r', 'y', 'g', 'b'] 

	# plotting the pie chart 
	plt.pie(results, labels = activities, colors=colors,  
        	startangle=90, shadow = True, explode = (0, 0, 0.1, 0), 
        	radius = 1.2, autopct = '%1.1f%%') 

	plt.title("Subject Averages")
  
	# plotting legend 
	plt.legend() 
  
	# showing the plot 
	plt.show()
