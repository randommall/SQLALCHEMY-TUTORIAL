from db_engine import *
from sqlalchemy import join

stmt1  = select(users, accounts).select_from(users.join(accounts, users.c.id == accounts.c.user_id))

stmt2 = select(users, accounts).select_from(join(users, accounts))

stmt3 = select(users.c.name, users.c.id, accounts.c.type).select_from(users.join(accounts))

with mysql_engine.connect() as conn:
    result1 = conn.execute(stmt1)
    result2 = conn.execute(stmt2)
    result3 = conn.execute(stmt3)

print('\nstatement1 - with onclause: ')
for row in result1:
    print(row)

print('\nstatement2 - without onclause: ')
for row in result2:
    print(row)

print('\nstatement3 - without onclause and with column specifications: ')
for row in result3:
    print(f'(name: {row[0]}) - (id: {row[1]} ) - (account type: {row[2]})')

stmt4 = select(users, accounts).select_from(users.join(accounts)).where(accounts.c.type == 'savings')

stmt5 = select(users, accounts, addresses).select_from(users.join(accounts)).join(addresses, users.c.id == addresses.c.user_id)

with mysql_engine.connect() as conn:
    result4 = conn.execute(stmt4)
    result5 = conn.execute(stmt5)

print('\nstatement4 - without onclause and with the where clause: ')
for row in result4:
    print(row)

print('\nstatement5 - without onclause and joining three tables: ')
for row in result5:
    print(f'[user]==> id: {row[0]}, name: {row[1]}, email: {row[2]}, age:  {row[3]}, [account]==> id: {row[4]}, type: {row[5]}, user_id{row[6]}, [address]==> id: {row[7]}, user_id: {row[8]}, address: {row[9]}')
