from os import getenv
from dotenv import load_dotenv
from sqlalchemy import (create_engine, MetaData, Table)

load_dotenv()

DB_USER = getenv('DB_USER')
DB_PWD = getenv('DB_PWD')
DB_HOST = getenv('DB_HOST')
DB_NAME = getenv('DB_NAME')

conn_string = f'mysql+mysqlconnector://{DB_USER}:{DB_PWD}@{DB_HOST}/{DB_NAME}'

mysql_engine = create_engine(conn_string)

reflect_metadata = MetaData()

employees = Table('employees', reflect_metadata, autoload_with=mysql_engine)

columns = [c for c in employees.columns]

# print('columns: ', columns)
print('-' * 50)

# print('\nconstraints: ', employees.constraints)

stmt = employees.select()

conn = mysql_engine.connect()

result = conn.execute(stmt)

print(list(result))
