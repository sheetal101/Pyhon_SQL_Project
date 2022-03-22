#_______________________Restaurant Management Database Project___________________________________#

import mysql.connector

mydb=mysql.connector.connect(host='localhost', user='root', password='Situ321@#', database="RESTAURANT_SQL_PROJECT")
myacces=mydb.cursor()

# myacces.execute("CREATE DATABASE RESTAURANT_SQL_PROJECT")

# myacces.execute("CREATE TABLE CUSTOMER_TABLE (firstname varchar (30) not null, lastname varchar (30) not null, in_time varchar (30) not null, contact varchar (30) not null, total_amount int not null);")
# sql="INSERT INTO CUSTOMER_TABLE (firstname, lastname, in_time, contact, total_amount) VALUES(%s,%s,%s,%s,%s)"

# val=[("Preeti","Rawat","10:20 AM", 9934000034, 22000),
#     ("Sapna", "negi", "04:00 AM", 4490120923, 30000),
#     ("Ashna","Gusian" ,"11:00 AM", 4423003323, 2900),
#     ("Sheetal","Devrani" ,"04:00 AM", 9012120221, 1500),
#     ("Vijay","Ganesh", "10:20 AM", 9721021222, 400), 
#     ("Rahul","Sharma" ,"04:00 AM", 7017142322, 500),
#     ("Akshit","Dwivedi", "11:00 AM", 9200112113, 2500), 
#     ("Sahil","Roy", "04:00 AM", 8092301200, 1500),
#     ("max","oppenhiemer", "10:20 AM", 8092003031, 1500),
#     ("sushree","Rana", "04:00 AM", 8022459000,2500),
#     ("prerna","Rai", "11:00 AM", 8092301122, 500),
#     ("Lewis","max", "04:00 AM", 4023453422, 2500),
#     ("Sahil","Sharma", "10:20 AM", 8234130221, 500),
#     ("alan","walker", "11:00 AM", 8092330112, 5500),
#     ("Ram","Krishna", "04:00 AM", 1013498722, 2000),
#     ("Anjani","Prajapat", "10:20 AM", 802130770, 5200),
#     ("Himani","Palariya", "04:00 AM", 8992309144, 2000),
#     ("Shlini","singh", "04:00 AM", 7088501422, 1000),
#     ("Krishna","Ram", "11:00 AM", 9718231212, 1300),
#     ("Shyam","Sharma", "04:00 AM", 8045231223, 1200),
#     ("Owne","Walker", "11:00 AM", 4001233434, 1000),
#     ("Rohit","Devrani", "04:00 AM", 9078563422, 2500),
#     ("Mohit","Sharma", "11:00 AM", 9045441200, 1500),
#     ("Susheel","Verma", "05:00 AM", 7907899599, 1500),
#     ("Rahul","Negi", "08:00 AM", 9045342388, 1500)]

# myacces.executemany(sql,val)
# mydb.commit()

#                                HOW TO DELETE A TABLE
# myacces.execute("drop table CUSTOMER_TABLE")


#_________________________________________UPDATE TABLE_________________________________________________

# UPDATE EXISTING RECORDS IN A TABLE BY USING UPDATE STATEMENT 


# updt_rec = "UPDATE SALARY_TABLE SET bonus = 5000 WHERE bonus = 3000"
# myacces.execute(updt_rec)
# mydb.commit()



#                SELECT ALL THE DATA FROM "CUSTOMER_TABLE" AND DISPLAY THE RESULT :
#                    HERE I'm USING THE fetchall() METHOD, WHICH FETHCES ALL ROWS.

# myacces.execute("SELECT * FROM CUSTOMER_TABLE")
# myresult = myacces.fetchall()
# for i in myresult:
#   print(i)


#                   SELECTING SOME OR ANY ONE COLUMN FROM CUSTOMER_TABLE 
#               myacces.execute("SELECT firstname, lastname FROM CUSTOMER_TABLE")

# myresult = myacces.fetchall()
# for i in myresult:
#   print(i)

#_______________ DELETE ANY EMPLOYEE'S RECORD FROM TABLE BY USING "DELETE FROM" _________________

# select_to_del = "DELETE FROM CUSTOMER_TABLE WHERE name = 'sahil' and name = Rahul'"
# myacces.execute(select_to_del)
# mydb.commit()

#_________________________________________CREATING TABLE 2__________________________________________

# myacces.execute("CREATE TABLE CUSTOMER_ORDERS (Customer_name varchar (30) not null,Order_name varchar (30) not null, Qty int not null, total_amount int not null);")
# sql="INSERT INTO CUSTOMER_ORDERS (Customer_name, Order_name, Qty, total_amount) VALUES(%s,%s,%s,%s)"


# val=[("Preeti","Burger",4, 22000),
#     ("Sapna","Burger",3, 30000),
#     ("Ashna","Burger",5, 29000),
#     ("Sheetal","Noodles",2, 1500),
#     ("Vijay","Noodles",3, 400), 
#     ("Rahul", "Noodles",1, 500),
#     ("Akshit", "Noodles",2, 2500), 
#     ("Sahil","Noodles",4, 1500),
#     ("max", "Noodles",5, 1500),
#     ("sushree","Pasta",7, 2500),
#     ("prerna", "Waffles",8, 500),
#     ("Lewis","Pizza",2, 2500),
#     ("Sahil","Pizza",2, 500),
#     ("alan","Pizza",2, 5500),
#     ("Ram","Pizza",2, 2000),
#     ("Anjani","Pizza",4, 5200),
#     ("Himani", "Noodles",2, 2000),
#     ("Shlini","Burger",2, 1000),
#     ("Krishna","Burger",2,1300),
#     ("Shyam","Burger",2, 1200),
#     ("Owne","Pizza",2, 1000),
#     ("Rohit","Pizza",2, 2500),
#     ("Mohit","Pizza",2, 1500),
#     ]
# myacces.executemany(sql,val)
# mydb.commit()

#_____________________________________CALCULATE MINIMUM AMOUNT_________________________________________

# myacces.execute("SELECT MIN(total_amount) AS minimum FROM CUSTOMER_ORDERS")
# result = myacces.fetchall()
# for i in result:
    # HERE i(var) WILL BE THE MINIMUM AMOUNT FROM ALL RECORDS
    # print(i)

#_____________________________________CALCULATE MAXIMUM AMOUNT_________________________________________

# myacces.execute("SELECT MAX(total_amount) AS minimum FROM CUSTOMER_ORDERS")
# result = myacces.fetchall()
# for i in result:
    # HERE i(var) WILL BE THE MINIMUM AMOUNT FROM ALL RECORDS
    # print(i)

#______________________________________AVERAGE OF total_amount PAID BY CUSTOMER______________________

# result="SELECT AVG(total_amount) AS average from CUSTOMER_ORDERS;"
# myacces.execute(result)
# rows = myacces.fetchall()
# for i in rows:
#     print("Average marks is :" + str(i[0]))


# ____________________________________GIVING LIMIT TO TABLE DATA____________________________________#

# myacces.execute("SELECT * FROM CUSTOMER_ORDERS LIMIT 8")

# IT WILL FETCH FIRST 5 RECORDS FROM CUSTOMER_ORDERS

# myresult = myacces.fetchall()
# for rec in myresult:
#   print(rec)


#_________________________________________LEFT JOIN___________________________________________________

# The LEFT JOIN keyword returns all records from the left table (table1), and the matching records (if any) from the right table (table2).

# myacces.execute("SELECT * FROM CUSTOMER_TABLE LEFT JOIN CUSTOMER_ORDERS ON CUSTOMER_TABLE.firstname =CUSTOMER_ORDERS.Customer_name")
# myresult = myacces.fetchall()
# for x in myresult:
#   print(x)