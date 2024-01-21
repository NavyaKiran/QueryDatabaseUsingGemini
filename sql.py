#creating the database to use with the app 

import sqlite3

## Connect to sqlite

connection = sqlite3.connect("student.db")

## Create a cursor to insert record, create table or retrieve records 

cursor = connection.cursor() 

## create the table 

table_info = """
create table STUDENT(Name varchar(25), Class varchar(25), 
Section varchar(25), Marks int);

"""
cursor.execute(table_info)

## insert records into the table 

cursor.execute ('''Insert into STUDENT values('A', 'BDA', 'ADS', 90)''')
cursor.execute ('''Insert into STUDENT values('B', 'BA', 'ADS', 95)''')
cursor.execute ('''Insert into STUDENT values('C', 'AML', 'ADS', 90)''')
cursor.execute ('''Insert into STUDENT values('D', 'BA', 'CS', 98)''')
cursor.execute ('''Insert into STUDENT values('E', 'BDA', 'CS', 90)''')


## Display all the records 
print("The inserted records are ")

data = cursor.execute('''Select * from STUDENT''')
for row in data: 
    print(row)

## Close the connection 
    
connection.commit() 
connection.close