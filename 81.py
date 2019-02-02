import pymysql
id = "10001"
user = "bob"
age = 20
db = pymysql.connect(host="172.16.10.103",user="root",password="123456",port=3306,db="spiders")
cursor = db.cursor()
sql = "inset into studens(id,name,age) values(%s,%s,%s)"
try:
    cursor.execute(sql,(id,user,age))
    db.commit()
except:
    db.rollback()
db.close()