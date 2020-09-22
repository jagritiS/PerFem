import mysql.connector

#mydb is the database connector
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="perfem"
)
email = ""
id = ""
print(mydb)
mycursor = mydb.cursor()

def setEmail(e):
    global email
    email = e
def setId(ids):
    global id
    id = ids
#check if the table exists and if not then create a table
def create_table(create_query):
    mycursor.execute("SHOW TABLES LIKE 'users'")
    result = mycursor.fetchone()
    if result:
        print("Table exists")
    else:
        mycursor.execute("CREATE TABLE users (id int primary key auto increment ,"
                         "f_name VARCHAR(25),l_name VARCHAR(25),email_id VARCHAR(25),"
                         "contact_no VARCHAR(25),dob date ,password VARCHAR(25))")

#insert data into the table
def insert_data(insert_query,val):
    #   sql = "INSERT INTO users (f_name, address) VALUES (%s, %s)"
    #  val = ("Jagriti", "Kathmandu")
    mycursor.execute(insert_query, val)
    mydb.commit()
    print(mycursor.rowcount, "record inserted.")
    if(mycursor.rowcount):
        flag = 1
    else:
        flag = 0
    return flag
def getUsers(read_query):
    print("the email from getuser")
    print(email)
    mycursor.execute(read_query)
    myresult = mycursor.fetchall()
    for x in myresult:
        return x[0]

#read data from the table
def read_data(read_query):
    mycursor.execute(read_query)
    myresult = mycursor.fetchall()
    for x in myresult:
        print(x)
    if (myresult):
        flag = 1
    else:
        flag = 0
    return flag

#delete data from the table
def delete_data(delete_query):
     sql = "DELETE FROM students WHERE address = 'lalitpur'"
     mycursor.execute(sql)
     mydb.commit()
     print(mycursor.rowcount, "record(s) deleted")

def update_data(update_query):
    sql = "UPDATE FROM students SET ID = 2 WHERE address = 'lalitpur'"
    mycursor.execute(sql)
    mydb.commit()
    print(mycursor.rowcount, "record(s) UPDATED")

def get_p_data(read_query):
    print("read period datas")
    print(id)
    print(email)
    print(read_query)
    mycursor.execute(read_query)
    myresult = mycursor.fetchall()
    for x in myresult:
        print(x)
        return x
