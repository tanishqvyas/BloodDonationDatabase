import MySQLdb


# Connecting to database
db = MySQLdb.connect(host="localhost",  		# your host 
                     user="user",       		# username
                     passwd="PASSWORD",     	# password
                     db="dbms_project")   	# name of the database


# Check if the connection to Database was successsful or not
if(db):
	print("Databse Connected Successfully\n")
else:
	print("Failure in Connecting....\n")


# Create a Cursor object to execute queries.
cur = db.cursor()

# List of queries to populate the Database
query_list = [
	

	# Populate the Site Table
	"INSERT INTO Site VALUES(1, 'Madam Malkins Lounge', '125, Diagon Alley')",
	"INSERT INTO Site VALUES(2, 'The Ollivanders', '123 Diagon Alley')",
	"INSERT INTO Site VALUES(3, 'Leaky Cauldron', '121 Filtchland Street, London')",
	"INSERT INTO Site VALUES(4, 'Azkaban', 'Forbidden Islands')",
	"INSERT INTO Site VALUES(5, 'GramSchmidtt Memorial Hall', '12th Main SQR, Orlands')",
	"INSERT INTO Site VALUES(6, 'Madam Pomfreys Health Care Centre', 'Ward 13, Hogwarts')",


	# Populate the Organization Table
	"INSERT INTO Organization VALUES(1, 'Hufflepuff', 'Basement, next to Kitchens, Hogwarts','8898976535')",
	"INSERT INTO Organization VALUES(2, 'Slytherin', 'Dungeons, Hogwarts','8836492649')",
	"INSERT INTO Organization VALUES(3, 'Gryffindor', 'Gryffindor Tower, through Fat Ladys Portrait, Hogwarts', '88267193729')",
	"INSERT INTO Organization VALUES(4, 'Ravenclaw', 'WestSide, top of Spiral Staircase, Hogwarts', '8826492649')",
	"INSERT INTO Organization VALUES(5, 'Thunderbird', 'Illvermony', '8826592649')",


	# Populate the Donor Table
	"INSERT INTO Donor VALUES(1,1, 'Clint Barton', 'B+', 45, 'Male', 'hawkeye@gmail.com',0)",
	"INSERT INTO Donor VALUES(2,2, 'Billy', 'A+', 21, 'Feale', 'ahawkeye@gmail.com',1)",
	"INSERT INTO Donor VALUES(3,3, 'Willy Smith', 'B-', 33, 'Female', 'bhawkeye@gmail.com',2)",
	"INSERT INTO Donor VALUES(4,4, 'Baron Jones', 'B-', 43, 'Feale', 'chawkeye@gmail.com',0)",
	"INSERT INTO Donor VALUES(5,5, 'Connar John', 'B-', 44, 'Male', 'dhawkeye@gmail.com',0)",
	"INSERT INTO Donor VALUES(6,1, 'Dolph Ziggler', 'B+', 43, 'Male', 'ehawkeye@gmail.com',0)",
	"INSERT INTO Donor VALUES(7,2, 'Mariana Finn', 'B+', 41, 'Male', 'fhawkeye@gmail.com',0)",
	"INSERT INTO Donor VALUES(8,3, 'Clint', 'B+', 23, 'Male', 'ghawkeye@gmail.com',0)",
	"INSERT INTO Donor VALUES(9,4, 'Clint Barton', 'A+', 42, 'Male', 'hgawkeye@gmail.com',0)",
	"INSERT INTO Donor VALUES(10,5, 'Clint Barton', 'AB+', 25, 'Female', 'ghkjiawkeye@gmail.com',0)",
	"INSERT INTO Donor VALUES(11,1, 'Priyal Jain', 'AB+', 25, 'Female', 'hggawkeye@gmail.com',0)",
	"INSERT INTO Donor VALUES(12,2, 'Tomar Rajesh', 'AB+', 35, 'Male', 'hawkegsye@gmail.com',0)",
	"INSERT INTO Donor VALUES(13,3, 'Taimur', 'AB-', 65, 'Male', 'hawkeyee@gmail.com',0)",
	"INSERT INTO Donor VALUES(14,4, 'Gangadhar Rao', 'B+', 85, 'Male', 'hawkeyse@gmail.com',0)",
	"INSERT INTO Donor VALUES(15,5, 'Akash Kumar', 'B+', 95, 'Male', 'hawkeyte@gmail.com',0)",
	"INSERT INTO Donor VALUES(16,1, 'Cortis Reed', 'B+', 25, 'Female', 'hawkfdeye@gmail.com',0)",
	"INSERT INTO Donor VALUES(17,2, 'Ryan Reynolds', 'B+', 35, 'Male', 'hoipawkeyse@gmail.com',0)",
	"INSERT INTO Donor VALUES(18,3, 'Donal Trump', 'B+', 23, 'Male', 'hawkeydfe@gmail.com',0)",
	"INSERT INTO Donor VALUES(19,4, 'Kim Jong Un', 'A+', 23, 'Female', 'hawkeye1@gmail.com',0)",
	"INSERT INTO Donor VALUES(20,5, 'Sheera Finn', 'B+', 22, 'Male', 'hawkeyooe@gmail.com',0)",
	"INSERT INTO Donor VALUES(21,1, 'Leyman Short', 'B+', 22, 'Female', 'hawkeyyie@gmail.com',0)",
	"INSERT INTO Donor VALUES(22,2, 'Daniel Rad', 'B+', 22, 'Male', 'hawkedfye@gmail.com',0)",
	"INSERT INTO Donor VALUES(23,3, 'Clint Barton', 'B+', 24, 'Male', 'hawkeyesda@gmail.com',0)",
	"INSERT INTO Donor VALUES(24,4, 'Sean', 'B+', 25, 'Male', 'hawkeyerqe@gmail.com',0)",
	"INSERT INTO Donor VALUES(25,5, 'Clint Barton', 'B+', 34, 'Female', 'hawkeyafee@gmail.com',0)",
	"INSERT INTO Donor VALUES(26,1, 'Clint Barton', 'B+', 34, 'Female', 'hawkeyadawe@gmail.com',0)",
	"INSERT INTO Donor VALUES(27,2, 'Sean', 'O+', 33, 'Male', 'hawkeywe@gmail.com',0)",
	"INSERT INTO Donor VALUES(28,3, 'Clint Barton', 'O+', 32, 'Male', 'hawkeyewaa@gmail.com',0)",
	"INSERT INTO Donor VALUES(29,4, 'Bunny Bugs', 'B+', 32, 'Female', 'hawkeyeawd@gmail.com',0)",
	"INSERT INTO Donor VALUES(30,5, 'Rachel Ryna', 'B+', 33, 'Male', 'hawkeyeerw@gmail.com',0)",
	"INSERT INTO Donor VALUES(31,1, 'Rachel Ryna', 'B+', 34, 'Male', 'hawkeyewrwr@gmail.com',0)",
	"INSERT INTO Donor VALUES(32,2, 'Tom Thompson', 'B+', 35, 'Female', 'hawkeyqqee@gmail.com',0)",
	"INSERT INTO Donor VALUES(33,3, 'Timmy Indie', 'O+', 36, 'Female', 'hawkeyeqqrv@gmail.com',0)",
	"INSERT INTO Donor VALUES(34,4, 'Elliath Finn', 'B+', 37, 'Male', 'hawkeyshbde@gmail.com',0)",
	"INSERT INTO Donor VALUES(35,3, 'Gronads Tram', 'B+', 38, 'Male', 'hawkeywdce@gmail.com',0)",
	"INSERT INTO Donor VALUES(36,3, 'Cloaith Teast', 'B+', 39, 'Male', 'hawkeygape@gmail.com',1)",
	"INSERT INTO Donor VALUES(37,5, 'Amber Swift', 'B+', 40, 'Male', 'hawkeyepp@gmail.com',0)",
	"INSERT INTO Donor VALUES(38,1, 'Alexa Bliss', 'O-', 33, 'Male', 'hawkeyecc@gmail.com',1)",
	"INSERT INTO Donor VALUES(39,1, 'Sharon Carter', 'O-', 44, 'Male', 'hawkeyeqwa@gmail.com',0)",
	"INSERT INTO Donor VALUES(40,1, 'Sharon Carter', 'B+', 41, 'Male', 'habbwskesye@gmail.com',0)",
	"INSERT INTO Donor VALUES(41,2, 'Niyama Bliss', 'B+', 29, 'Male', 'hawekwfweeye@gmail.com',0)",
	"INSERT INTO Donor VALUES(42,3, 'Kori Blaze', 'O-', 30, 'Female', 'hawkervalye@gmail.com',0)",
	"INSERT INTO Donor VALUES(43,2, 'Ash Ketchum', 'B+', 50, 'Female', 'hawkeydfee@gmail.com',1)",
	"INSERT INTO Donor VALUES(44,1, 'Rial Minrow', 'B+', 27, 'Female', 'hawkewfeye@gmail.com',0)",
	"INSERT INTO Donor VALUES(45,5, 'David Brown', 'B+', 27, 'Male', 'hawkewefeeeye@gmail.com',0)",
	"INSERT INTO Donor VALUES(46,5, 'Filton Geen', 'B+', 38, 'Male', 'hawkeacbdwye@gmail.com',0)",
	"INSERT INTO Donor VALUES(47,4, 'Cassey Cassandra', 'O-', 31, 'Male', 'hawkewfpalye@gmail.com',1)",
	"INSERT INTO Donor VALUES(48,4, 'Colan Sean', 'B+', 56, 'Male', 'hawkeyllalae@gmail.com',1)",
	"INSERT INTO Donor VALUES(49,4, 'Thor Steve', 'B+', 69, 'Male', 'hawkellalaye@gmail.com',0)",
	"INSERT INTO Donor VALUES(50,4, 'Colan Steve', 'B+', 25, 'Male', 'hawkeyalaoape@gmail.com',0)",

	# Populate the Hospital Table
	"INSERT INTO Hospital VALUES(1, 'City Hospital','123 Main Square', '8872528252')",
	"INSERT INTO Hospital VALUES(2, 'Boneselvania Hospital','124 Main Square', '8872028252')",
	"INSERT INTO Hospital VALUES(3, 'Musclevania Hospital','125 Main Square', '8872518252')",
	"INSERT INTO Hospital VALUES(4, 'Ligamentarium Hospital','23 Main Square', '8872428252')",
	"INSERT INTO Hospital VALUES(5, 'Pomfrey Hospital','121 Main Square', '8872528259')",

	# Populate the Volunteer Table
	"INSERT INTO Volunteer VALUES(1, 1, 'Harry Potter')",
	"INSERT INTO Volunteer VALUES(2, 1, 'Hermione Granger')",
	"INSERT INTO Volunteer VALUES(3, 1, 'Ronald Weasley')",
	"INSERT INTO Volunteer VALUES(4, 1, 'Neville Longbottom')",
	"INSERT INTO Volunteer VALUES(1, 2, 'Draco Malfoy')",
	"INSERT INTO Volunteer VALUES(2, 2, 'Ginny Weasley')",
	"INSERT INTO Volunteer VALUES(3, 2, 'Percy Weasley')",
	"INSERT INTO Volunteer VALUES(4, 2, 'Cho Chang')",
	"INSERT INTO Volunteer VALUES(1, 3, 'Chirayu Gupta')",
	"INSERT INTO Volunteer VALUES(2, 3, 'Karen Smith')",
	"INSERT INTO Volunteer VALUES(3, 3, 'Bernard Kimberley')",
	"INSERT INTO Volunteer VALUES(4, 3, 'Parvati Patil')",
	"INSERT INTO Volunteer VALUES(5, 3, 'Dean Thomas')",
	"INSERT INTO Volunteer VALUES(1, 4, 'Seamus Finnigan')",
	"INSERT INTO Volunteer VALUES(2, 4, 'Cedric Doggory')",
	"INSERT INTO Volunteer VALUES(3, 4, 'Tom Riddle')",
	"INSERT INTO Volunteer VALUES(4, 4, 'Barty Crouch')",
	"INSERT INTO Volunteer VALUES(5, 4, 'Harold Dunsley')",
	"INSERT INTO Volunteer VALUES(1, 5, 'Remus Lupin')",
	"INSERT INTO Volunteer VALUES(9, 5, 'Albus Wulfric Percival Brian Dumbledore')",
	"INSERT INTO Volunteer VALUES(2, 5, 'Helena Carter')",
	"INSERT INTO Volunteer VALUES(3, 5, 'Severus Snape')",
	"INSERT INTO Volunteer VALUES(4, 5, 'Kirley Shackley')",
	"INSERT INTO Volunteer VALUES(5, 5, 'Riana Simpson')",
	"INSERT INTO Volunteer VALUES(5, 1, 'Gary Oldman')",
	"INSERT INTO Volunteer VALUES(6, 1, 'Regulus Black')",
	"INSERT INTO Volunteer VALUES(7, 1, 'Jane Granger')",
	"INSERT INTO Volunteer VALUES(9, 2, 'Rosemary Filtch')",
	"INSERT INTO Volunteer VALUES(6, 3, 'Dudley Dursley')",
	"INSERT INTO Volunteer VALUES(5, 2, 'Cornilius Fudge')",
	"INSERT INTO Volunteer VALUES(6, 4, 'Viktor Krum')",
	"INSERT INTO Volunteer VALUES(8, 1, 'Charlie Weasley')",
	"INSERT INTO Volunteer VALUES(6, 5, 'Lizabeth Carter')",
	"INSERT INTO Volunteer VALUES(7, 5, 'Steve Rogers')",
	"INSERT INTO Volunteer VALUES(8, 5, 'Anthony Stark')",
	"INSERT INTO Volunteer VALUES(9, 1, 'Bruce Banner')",
	"INSERT INTO Volunteer VALUES(10, 1, 'Fill Colson')",
	"INSERT INTO Volunteer VALUES(11, 1, 'Maria DB')",
	"INSERT INTO Volunteer VALUES(6, 2, 'Kiara Johanson')",

	# Populate the Donation Table
	"INSERT INTO Donation VALUES(1,1,1,1,'2019-08-01')"
	

	]


# start from the first query
query_index = 0

while(query_index < len(query_list)):

	# Fetch the query from the list of queries
	query = query_list[query_index]

	# Increment the query Index
	query_index += 1

	# Check for any kind of SQL Error
	try:
		# Execute the SQL query
		cur.execute(query)
		print("Query :",query_index," Executed Successfully")

	except Exception as e:
		print()
		print("----------ERROR INFORMATION FOR QUERY : ",query_index ,"------------------------------------->")
		print(e)
		print("For The Query : ")
		print(query)
		print("-------------------------------------------------------------------------------->")


# Close the cursor
cur.close()

# Commiting the changes
db.commit()