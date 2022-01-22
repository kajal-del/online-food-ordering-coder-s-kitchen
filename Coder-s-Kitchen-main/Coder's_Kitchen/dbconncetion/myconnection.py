import pymysql
conn=pymysql.connect(host="localhost", user="root", password="kajal@", db="coders_kitchen")
mycur=conn.cursor()