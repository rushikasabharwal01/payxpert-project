import mysql.connector
from mysql.connector import Error


def create_connection():
    connection = mysql.connector.connect(
        host="localhost",
        user="root",
        password="root",
        port='3306',
        database="payxpert"
    )
    return connection