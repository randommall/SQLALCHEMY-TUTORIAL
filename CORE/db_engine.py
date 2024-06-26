from os import getenv
from dotenv import load_dotenv

from sqlalchemy import (create_engine, MetaData,
                        Table, Column, String,
                        Integer, ForeignKey,
                        select, insert)


load_dotenv()

DB_USER = getenv('DB_USER')
DB_PWD = getenv('DB_PWD')
DB_HOST = getenv('DB_HOST')
DB_NAME = getenv('DB_NAME')

con_string = f'mysql+mysqlconnector://{DB_USER}:{DB_PWD}@{DB_HOST}/{DB_NAME}'

mysql_engine = create_engine(con_string)

# POSTGRE_USER = getenv('POSTGRE_USER')
# POSTGRE_PWD = getenv('POSTGRE_PWD')
# POSTGRE_HOST = getenv('POSTGRE_HOST')
# POSTGRE_NAME = getenv('POSTGRE_NAME')
# # postgresql connection string
# postgre_conn_str = f'postgresql+psycopg2://{POSTGRE_USER}:{POSTGRE_PWD}@{POSTGRE_HOST}/{POSTGRE_NAME}'
# postgre_engine = create_engine(postgre_conn_str)

# sqlite_engine = create_engine('sqlite:///mydb.db')

metadata = MetaData()

users = Table('users', metadata,
              Column('id', Integer, primary_key=True, autoincrement=True),
              Column('name', String(60), nullable=False),
              Column('email', String(60), nullable=False),
              Column('age', Integer))

accounts = Table('accounts', metadata,
              Column('id', Integer, primary_key=True, autoincrement=True),
              Column('type', String(60), nullable=False, default='savings'),
              Column('user_id', Integer, ForeignKey('users.id', ondelete='CASCADE', name='fk_accounts_user_id'), nullable=False))

metadata.create_all(bind=mysql_engine)

# drop tables
# metadata.drop_all(bind=mysql_engine)

# create single table
# users.create(mysql_engine)

# drop single table
# users.drop(mysql_engine)

__all__ = ['mysql_engine', 'users', 'accounts', 'insert', 'select']
