from sqlalchemy import MetaData, create_engine
from os import getenv
from dotenv import load_dotenv
from sqlalchemy import (create_engine, MetaData, select)

load_dotenv()

DB_USER = getenv('DB_USER')
DB_PWD = getenv('DB_PWD')
DB_HOST = getenv('DB_HOST')
DB_NAME = getenv('DB_NAME')

conn_string = f'mysql+mysqlconnector://{DB_USER}:{DB_PWD}@{DB_HOST}/{DB_NAME}'

mysql_engine = create_engine(conn_string)

reflect_metadata = MetaData()

# reflect_metadata.reflect(bind=mysql_engine, only=['users', 'accounts'], views=True)
reflect_metadata.reflect(bind=mysql_engine)

tables = reflect_metadata.tables

users = tables['users']

accounts = tables['accounts']

addresses = tables['addresses']

for column in users.columns:
    print(f"Column Name: {column.name}")
    print(f"Data Type: {column.type}")
    print(f"Nullable: {column.nullable}")
    print("-" * 50)

users_pk = users.primary_key

stmt1 = users.select().where(users.c.age > 30)

stmt2 = select(users, accounts).where(users.c.id == accounts.c.user_id)

with mysql_engine.connect() as conn:
    result1 = conn.execute(stmt1)
    result2 = conn.execute(stmt2)
for row in result1:
    print(row)
for row in result2:
    print(row)
print("-" * 50)

with mysql_engine.begin() as conn:
    for table in reversed(reflect_metadata.sorted_tables):
        conn.execute(table.delete().where(table.c.id == 4))


with mysql_engine.connect() as conn:
    result1 = conn.execute(stmt1)
    result2 = conn.execute(stmt2)
for row in result1:
    print(row)
for row in result2:
    print(row)
print("-" * 50)
