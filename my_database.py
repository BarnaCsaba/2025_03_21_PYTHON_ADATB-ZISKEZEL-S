import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password=""
)
#általunk létrehozott adatbázis
mycursor = mydb.cursor()
DATABASE = "mydatabase"

#táblázat létrehozása
mycursor.execute(f"CREATE DATABASE IF NOT EXISTS {DATABASE}")

#adatbázisok mutatása
mycursor.execute("SHOW DATABASES")


for x in mycursor:
  print(x)

#adatbázis használata
mycursor.execute(f"USE {DATABASE}")

#táblázat létrehozása
mycursor.execute("CREATE TABLE IF NOT EXISTS customers (name VARCHAR(255), address VARCHAR(255))")

#adatok beszúrása (INSERT)

sql = "INSERT INTO customers (name, address) VALUES (%s, %s)"
val = [
  ('Peter', 'Lowstreet 4'),
  ('Amy', 'Apple st 652'),
  ('Hannah', 'Mountain 21'),
  ('Michael', 'Valley 345'),
  ('Sandy', 'Ocean blvd 2'),
  ('Betty', 'Green Grass 1'),
  ('Richard', 'Sky st 331'),
  ('Susan', 'One way 98'),
  ('Vicky', 'Yellow Garden 2'),
  ('Ben', 'Park Lane 38'),
  ('William', 'Central st 954'),
  ('Chuck', 'Main Road 989'),
  ('Viola', 'Sideway 1633')
]

mycursor.executemany(sql, val)

mydb.commit()

print(mycursor.rowcount, "was inserted.")

#select

mycursor.execute("SELECT * FROM customers")

myresult = mycursor.fetchone()

print(myresult)

#where

sql = "SELECT * FROM customers WHERE address = %s"
adr = ("Yellow Garden 2", )


myresult = mycursor.fetchall()

for x in myresult:
  print(x)