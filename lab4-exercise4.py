#!/usr/bin/env python3
import sqlite3
#connect to database file
dbconnect = sqlite3.connect("Test.db");
#If we want to access columns by name we need to set
#row_factory to sqlite3.Row class
dbconnect.row_factory = sqlite3.Row;
#now we create a cursor to work with db
cursor = dbconnect.cursor();
#execute insetr statement
cursor.execute('''insert into Test values (42, "hate")''');
dbconnect.commit();
#execute simple select statement
cursor.execute('SELECT * FROM Test');
#print data
for row in cursor:
    print(row['Number'],row['words'] );
#close the connection
cursor.execute('''CREATE TABLE Efour(sensorID INTEGER, type WORD,zone WORD) ''');
cursor.execute('''insert into Efour values (1,"door", "kitchen")''');
cursor.execute('''insert into Efour values (2,"temperature", "kitchen")''');
cursor.execute('''insert into Efour values (3,"door", "garage")''');
cursor.execute('''insert into Efour values (4,"motion", "garage")''');
cursor.execute('''insert into Efour values (5,"temperature", "garage")''');

cursor.execute('SELECT * FROM Efour');
#print data
for row in cursor:
    print(row['sensorID'],row['type'],row['zone'] );


dbconnect.close();