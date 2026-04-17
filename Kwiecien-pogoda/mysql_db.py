import mysql.connector
from config import Config

def create_connection():
    try:
        connection = mysql.connector.connect(
            host=Config.db_host,
            user=Config.db_user,
            password=Config.db_password,
            port=Config.db_port
        )
        return connection
    except Exception as e:
        print(e)


def create_db_and_table():
    try:
        conn = create_connection()
        cursor = conn.cursor()
        cursor.execute(f"CREATE DATABASE IF NOT EXISTS {Config.db_name}")
        cursor.execute(f"USE {Config.db_name}")

        create_table_query = """ 
            CREATE TABLE IF NOT EXISTS weather_data (
                id INT AUTO_INCREMENT NOT NULL PRIMARY KEY,
                temp FLOAT,
                feels_like FLOAT,
                name VARCHAR(255) NOT NULL,
                timestamp DATETIME NOT NULL,
                humidity INT,
                pressure INT,
                description VARCHAR(255),
                wind_speed FLOAT
            )
        """
        cursor.execute(create_table_query)
        print("Tabela i baza zostały utworzone bądź istnieją")
        cursor.close()

    except Exception as e:
        print(e,"ww")


create_db_and_table()