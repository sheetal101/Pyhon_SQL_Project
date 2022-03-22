#                                     PROJECT 1
#                          Payroll Management System WITH SQL(PYTHON)                       #

import mysql.connector
# Python needs a MySQL driver to access the MySQL database.
# creating a connection to the database
mydb=mysql.connector.connect(host='localhost', user='root', password='Situ321@#', database="PYTHON_SQL_PROJECT")

myacces=mydb.cursor()
# myacces.execute("CREATE DATABASE PYTHON_SQL_PROJECT")


#_____________________________________CREATING TABLE 1______________________________________________

# myacces.execute("CREATE TABLE EMP_TABLE (Emp_ID int, firstname varchar (30) not null, lastname varchar (30) not null, address varchar (30) not null, contact int not null);")
# sql="INSERT INTO EMP_TABLE (Emp_ID, firstname, lastname, address, contact) VALUES(%s,%s,%s,%s,%s)"

# val=[(105, "Preeti","Rawat","Paris", 99340000),
#     (106, "Sapna", "negi", "London", 44901209),
#     (107, "Ashna","Gusian" ,"Eidenburg", 44230033),
#     (108, "Sheetal","Devrani" ,"Delhi", 90121201),
#     (109, "Vijay","Ganesh", "Dehradun", 97210212), 
#     (110, "Rahul","Sharma" ,"Kolkatta", 70171423),
#     (111, "Akshit","Dwivedi", "Jaipur", 92001123), 
#     (112, "Sahil","Roy", "sidney", 80923012),
#     (113, "max","oppenhiemer", "sidney", 80923031),
#     (114, "sushree","Rana", "Jaspur", 80224590),
#     (115, "prerna","Rai", "sikkim", 80923011),
#     (116, "Lewis","max", "scotland", 40234534),
#     (117, "Sahil","Sharma", "Udaipur", 82341301),
#     (118, "alan","walker", "pars", 80923301),
#     (119, "Ram","Krishna", "Mathura", 10134987),
#     (220, "Anjani","Prajapat", "Kanpur", 8021300),
#     (223, "Himani","Palariya", "Nainital", 89923091),
#     (221, "Shlini","singh", "delhi", 70885014),
#     (233, "Krishna","Ram", "Kotdwara", 97182312),
#     (345, "Shyam","Sharma", "Rishikesh", 80452312),
#     (231, "Owne","Walker", "London", 40012334),
#     (200, "Rohit","Devrani", "Laddakh", 90785634),
#     (210, "Mohit","Sharma", "Dehradun", 90454412),
#     (290, "Susheel","Verma", "Kanpur", 79078995),
#     (230, "Rahul","Negi", "Jaipur", 90453423),
#     ]

# myacces.executemany(sql, val)
# mydb.commit()

# SELECT ALL THE DATA FROM "EMP_TABLE" AND DISPLAY THE RESULT :
# HERE I'm USING THE fetchall() METHOD, WHICH FETHCES ALL ROWS.

# myacces.execute("SELECT * FROM EMP_TABLE")
# myresult = myacces.fetchall()
# for i in myresult:
#   print(i)

# SELECTING SOME OR ANY ONE COLUMN FROM TABLE 
# myacces.execute("SELECT firstname, lastname FROM EMP_TABLE")
# myresult = myacces.fetchall()
# for i in myresult:
#   print(i)

# HOW TO FILTER WITH A "WHERE" STATEMENT: 

# selected_data = "SELECT * FROM EMP_TABLE WHERE address='Dehradun'"
# myacces.execute(selected_data)

# myresult = myacces.fetchall()
# for i in myresult:
#   print(i)

# DELETE ANY EMPLOYEE'S RECORD FROM TABLE BY USING "DELETE FROM" 
# select_to_del = "DELETE FROM EMP_TABLE WHERE address = 'delhi' and address='sidney'"
# myacces.execute(select_to_del)
# mydb.commit()


# mydb.commit() is required to make the changes

#____________________________________CREATING TABLE 2_____________________________________________#
# I'm creting Another table "SALARY TABLE"

# myacces.execute("CREATE TABLE SALARY_TABLE (Emp_ID int, name varchar (30) not null, salary int not null, bonus int not null, department varchar (30) not null, dept_no int not null, Hire_date varchar(30));")
# sql="INSERT INTO SALARY_TABLE (Emp_ID, name, salary, bonus, department, dept_no, Hire_date ) VALUES(%s,%s,%s,%s,%s,%s,%s)"
# val=[(105, "Preeti",10000,1000, "clerk", 10, "02-Jan-2021"),
#     (106, "Sapna", 25000, 2000, "Manager", 20, "02-Jan-2021"),
#     (107, "Ashna",30000 ,3000,"Devops", 10, "02-Jan-2021" ),
#     (108, "Sheetal",23400 ,1000, "Analyst", 30, "02-Jan-2021"),
#     (109, "Vijay",120000, 3000, "clerk", 10, "17-Jan-2022"), 
#     (110, "Rahul",50000 ,1000, "Devops", 30, "17-Jan-2022"),
#     (111, "Akshit",350000, 3000, "Analyst", 30, "17-Jan-2022"), 
#     (112, "Sahil",10000, 3000, "clerk", 10, "17-Jan-2022"),
#     (113, "max",200000, 3000, "Analyst", 10, "15-Sep-2020"),
#     (114, "sushree",100000, 3000, "clerk", 20, "17-Jan-2022"),
#     (115, "prerna",50000, 2000, "Devops", 10, "02-Jan-2021"),
#     (116, "Lewis",25000, 1000, "Analyst", 30, "15-Sep-2020"),
#     (117, "Sahil",120000, 4000,"Manager", 10, "17-Jan-2022"),
#     (118, "alan",25000, 1000,"Devops", 30, "17-Jan-2022"),
#     (119, "Ram",50000, 2000, "Manager", 30, "17-Jan-2022"),
#     (220, "Anjani",120000, 3000, "Analyst", 20, "15-Sep-2020"),
#     (223, "Himani",120000, 3500, "Manager", 20, "02-Jan-2021"),
#     (221, "Shlini",120000, 4000, "Devops", 30, "02-Jan-2021"),
#     (233, "Krishna",50000, 2000, "Analyst", 30, "02-Jan-2021"),
#     (345, "Shyam",120000, 5000, "Devops", 30, "02-Jan-2021"),
#     (231, "Owne",50000, 2000, "clerk", 30, "17-Jan-2022"),
#     (200, "Rohit",25000, 2000, "clerk", 20, "15-Sep-2020"),
#     (210, "Mohit",120000, 3000, "Devops", 20, "17-Jan-2022"),
#     (290, "Susheel",25000, 1000,"Manager", 20, "15-Sep-2020"),
#     (230, "Rahul",120000, 3000, "clerk", 20, "17-Jan-2022")
#     ]
# myacces.executemany(sql, val)
# mydb.commit()

# DELETE IF THE TABLE EXIST
# sql = "DROP TABLE IF EXISTS SALARY_TABLE"
# myacces.execute(sql)

#_________________________________________UPDATE TABLE_________________________________________________

# UPDATE EXISTING RECORDS IN A TABLE BY USING UPDATE STATEMENT 
# HERE I'm SETTING/UPDATING BONUS 5000 IN PLACE OF 3000

# updt_rec = "UPDATE SALARY_TABLE SET bonus = 5000 WHERE bonus = 3000"
# myacces.execute(updt_rec)
# mydb.commit()

# ____________________________________GIVING LIMIT TO TABLE DATA____________________________________#

# myacces.execute("SELECT * FROM SALARY_TABLE LIMIT 5")

# IT WILL FETCH FIRST 5 RECORDS FROM SALARY_TABLE

# myresult = myacces.fetchall()
# for rec in myresult:
#   print(rec)


