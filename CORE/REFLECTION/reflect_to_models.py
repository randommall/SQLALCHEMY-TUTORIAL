from os import getenv
from dotenv import load_dotenv
from sqlalchemy.orm import DeclarativeBase, sessionmaker
from sqlalchemy import MetaData, create_engine
from sqlalchemy.ext.automap import automap_base
from sqlalchemy import (create_engine, MetaData)
from contextlib import contextmanager

load_dotenv()


DB_USER = getenv('DB_USER')
DB_PWD = getenv('DB_PWD')
DB_HOST = getenv('DB_HOST')
DB_NAME = getenv('DB_NAME')

conn_string = f'mysql+mysqlconnector://{DB_USER}:{DB_PWD}@{DB_HOST}/{DB_NAME}'

mysql_engine = create_engine(conn_string)

Session = sessionmaker(bind=mysql_engine, autoflush=False, expire_on_commit=False)

reflect_metadata = MetaData()

reflect_metadata.reflect(bind=mysql_engine)

class Base(DeclarativeBase):
    metadata = reflect_metadata

Base = automap_base(Base)
Base.prepare()

User = Base.classes.users
Account = Base.classes.accounts
Address = Base.classes.addresses

@contextmanager
def session_gen():
    try:
        session = Session()
        yield session
    except Exception as exc:
        print(f'An error occured: {exc}')
    finally:
        session.close()

with session_gen() as session:
    new_user = User(name="John Doe", email="john.doe@example.com", age=30)
    session.add(new_user)
    session.commit()

with session_gen() as session:
    users = session.query(User).all()

for user in users:
    print(user.id, user.name, user.email, user.age)
