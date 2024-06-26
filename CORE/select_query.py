from db_engine import *
from sqlalchemy import and_, or_

users_stmt = users.select()

acc_stmt = select(accounts)

with mysql_engine.connect() as conn:
    result = conn.execute(users_stmt)
    result2 = conn.execute(acc_stmt)

print('\nall users in the database: ')
for row in result:
    print(row)

print('\nall accounts in the database: ')
for row in result2:
    print(row)

users_stmt2  = users.select().where(users.c.age > 20)

acc_stmt2 = accounts.select().where(accounts.c.type == 'savings')

users_stmt3 = users.select().where(and_(users.c.id == 1, users.c.name == 'Johnson'))

users_stmt4 = users.select().where((users.c.id == 1) & (users.c.name == 'Johnson'))

users_stmt5 = users.select().where(or_(users.c.id == 1, users.c.id == 2))

users_stmt6 = users.select().where((users.c.id == 1) | (users.c.id == 2))

users_stmt7 = users.select().where(and_(users.c.age > 20, or_(users.c.id > 1, users.c.email.like('%email.com'))))

users_stmt8 = users.select().where((users.c.age > 20) & ((users.c.id > 1) | (users.c.email.like('%email.com'))))

with mysql_engine.connect() as conn:
    filtered_users = conn.execute(users_stmt2)

    savings_accounts = conn.execute(acc_stmt2)

    user_Johnson = conn.execute(users_stmt3)

    user_Johnson2 = conn.execute(users_stmt4)

    users_or = conn.execute(users_stmt5)

    users_or2 = conn.execute(users_stmt6)

    complex_select = conn.execute(users_stmt7)

    complex_select2 = conn.execute(users_stmt8)

print("\nUsers Older Than 20:")
for row in filtered_users:
    print(row)

print("\nAccounts with Type 'Savings':")
for row in savings_accounts:
    print(row)

print("\nUser Johnson _and function:")
for row in user_Johnson:
    print(row)

print("\nUser Johnson & bitwise operator:")
for row in user_Johnson2:
    print(row)

print("\nUsers _or function:")
for row in users_or:
    print(row)

print("\nUsers | bitwise operator:")
for row in users_or2:
    print(row)

print("\ncomplex select with and_ and or_ function:")
for row in complex_select:
    print(row)

print("\ncomplex select with & and | bitwise operators:")
for row in complex_select2:
    print(row)
