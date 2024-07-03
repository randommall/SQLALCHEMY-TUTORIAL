from db_engine import *
from sqlalchemy import outerjoin, join

stmt1 = select(users, accounts).select_from(users.outerjoin(accounts, users.c.id == accounts.c.user_id))

stmt2 = select(users, accounts).select_from(outerjoin(users, accounts))

stmt3 = select(users, accounts).select_from(users.join(accounts, users.c.id == accounts.c.user_id, isouter=True))

stmt4 = select(users, accounts).select_from(users.join(accounts, isouter=True))

stmt5 = select(users.c.name, users.c.id, accounts.c.type).select_from(users.join(accounts, isouter=True))

stmt6 = select(users, accounts).select_from(users.join(accounts, isouter=True)).where(accounts.c.type == 'savings')

stmt7 = select(users, accounts, addresses).select_from(users.join(accounts, isouter=True)).join(addresses, users.c.id == addresses.c.user_id)

with mysql_engine.connect() as conn:
    result1 = conn.execute(stmt1)
    result2 = conn.execute(stmt2)
    result3 = conn.execute(stmt3)
    result4 = conn.execute(stmt4)
    result5 = conn.execute(stmt5)
    result6 = conn.execute(stmt6)
    result7 = conn.execute(stmt7)

print('\nstatement1 - with onclause and with outerjoin() function: ')
for row in result1:
    print(row)


print('\nstatement2 - without onclause and with outerjoin() function: ')
for row in result2:
    print(row)

print('\nstatement3 - with onclause and  with join(isouter=True) function: : ')
for row in result3:
    print(row)

print('\nstatement4 - without onclause and with join(isouter=True) function:  ')
for row in result4:
    print(row)

print('\nstatement5 - without onclause and with join(isouter=True) function and specific columns:  ')
for row in result5:
    print(f'(name: {row[0]}) - (id: {row[1]} ) - (account type: {row[2]})')

print('\nstatement6 - without onclause and with join(isouter=True) function and where clause:  ')
for row in result6:
    print(row)

print('\nstatement7 - joining three tables: ')
for row in result7:
    print(f'[user]==> id: {row[0]}, name: {row[1]}, email: {row[2]}, age:  {row[3]}, [account]==> id: {row[4]}, type: {row[5]}, user_id{row[6]}, [address]==> id: {row[7]}, user_id: {row[8]}, address: {row[9]}')
