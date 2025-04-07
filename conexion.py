import psycopg2
import os


def connect():

    return psycopg2.connect(

        host = os.getenv("DB_HOST"),

        user = os.getenv("DB_USER"),

        password = os.getenv("DB_PASSWORD"),

        database = os.getenv("DB_DATABASE")
        
)