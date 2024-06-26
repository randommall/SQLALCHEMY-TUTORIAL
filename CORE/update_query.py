from db_engine import *
from sqlalchemy import update

with mysql_engine.begin() as conn:
    users_result = conn.execute(users.select())
    acc_result = conn.execute(accounts.select())

print('\nUsers Before update: ')
for row in users_result:
    print(row)

print('\nAccounts Before update: ')
for row in acc_result:
    print(row)

acc_stmt = accounts.update().where(accounts.c.type == 'checkings').values(type='savings')

users_stmt = update(users).where(users.c.id == 1).values(name='Loki', email='Loki@email.com')

with mysql_engine.begin() as conn:
    conn.execute(acc_stmt)
    conn.execute(users_stmt)

    users_result = conn.execute(users.select())
    acc_result = conn.execute(accounts.select())

print('\nUsers After update: ')
for row in users_result:
    print(row)

print('\nAccounts Accounts update: ')
for row in acc_result:
    print(row)
