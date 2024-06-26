from db_engine import *
from sqlalchemy import delete

try:
    with mysql_engine.begin() as conn:
        result = conn.execute(users.select())
except Exception as exc:
    print(f'An error occured: {exc}')

print('before delete: ')
for row in result:
    print(row)




users_stmt = delete(users).where(users.c.id == 1)
try:
    with mysql_engine.begin() as conn:
        conn.execute(users_stmt)
        result = conn.execute(users.select())
except Exception as exc:
    print(f'An error occured: {exc}')

print('after delete: ')
for row in result:
    print(row)
