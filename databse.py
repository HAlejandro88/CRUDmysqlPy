import mysql.connector

config = {
    'user': 'root',
    'password': 'Venus#88',
    'host': 'localhost',
    'database': 'acme'
}

db = mysql.connector.connect(**config)
cursor = db.cursor()