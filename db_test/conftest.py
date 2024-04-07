import mysql.connector
import pytest
import os

from dotenv import load_dotenv


load_dotenv()

@pytest.fixture()
def db():
    connection = mysql.connector.connect(
      host=os.getenv('host'),
      port=os.getenv('port'),
      user=os.getenv('user'),
      password=os.getenv('password'),
      database=os.getenv('database')
    )
    cursor = connection.cursor()
    yield cursor
    connection.close()








