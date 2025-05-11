import mysql.connector as ms;

con = ms.connect(
    host="localhost",
    user="root",
    database="library",  # name your database here
    passwd="Rithan@123"  # enter your mysql passwd here
)


if con.is_connected():
    print("database connected")
else:
    print("connection unsuccessful")
