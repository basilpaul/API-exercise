#!/usr/bin/env python3.6

from flask import Flask, jsonify, request
from flaskext.mysql import MySQL
import sys
import warnings
import mysql.connector
import csv
import os

#Ignore warnings
if not sys.warnoptions:
    warnings.simplefilter("ignore")

#SQL Queries
create_database_query = """CREATE DATABASE IF NOT EXISTS titanic"""
use_database_query = """USE titanic"""
create_table_query = """CREATE TABLE IF NOT EXISTS `passengers`
    						(Survived INT(1), 
    						Pclass INT(10),
						    Name VARCHAR(255),
						    Sex VARCHAR(255),
						    Age INT(3),
						    Siblings INT(10),
						    Parents INT(10),
						    Fare FLOAT(20))"""
sql_insert_query = ("INSERT INTO passengers "
               "(Survived, Pclass, Name, Sex, Age, Siblings, Parents, Fare) "
               "VALUES (%s, %s, %s, %s, %s, %s, %s, %s)")

#Connect to mysql
mydb = mysql.connector.connect(
	host=os.getenv('MYSQL_HOST'),
	user=os.getenv('MYSQL_USER'),
	password=os.getenv('MYSQL_ROOT_PASSWORD'),
	port=3306
	)

cur = mydb.cursor()

#Create database and table if it does not exist
dbresult = cur.execute(create_database_query)
#Use database
useresult = cur.execute(use_database_query)
#Create table if it does not exist
tableresult = cur.execute(create_table_query)

#Insert into table
print("Insert in progress:")

#Load CSV
with open('titanic.csv', 'r') as csvfile:
	csv_data=csv.reader(csvfile)
	#Skip the first line
	next(csv_data)
	for item in csv_data:
		try:
			result = cur.execute(sql_insert_query, item)
		except:
			sys.exit(2)

print("Insert: Success")
#Commit and close db
mydb.commit()
cur.close()
mydb.close()
