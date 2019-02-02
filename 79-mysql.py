import pymysql
db = pymysql.connect(host="172.16.10.103",user="root",password="123456",port=3306)
cursor = db.cursor()
cursor.execute("select version()")
#print(cursor.execute("SELECT VERSION()"))
data = cursor.fetchone()
print("data_version:",data)
cursor.execute("create database spiders default character set utf8")
db.close()





