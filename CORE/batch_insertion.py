from db_engine import *

users_values = [
    {"name": "Ben", "email": "Ben@email.com", "age": 100},
    {"name": "Alice", "email": "Alice@email.com", "age": 25}
]

acc_values = [
    {"user_id": 2},
    {"type": 'checkings', "user_id": 3}
]

try:
    with mysql_engine.begin() as conn:
        conn.execute(users.insert(), users_values)
        conn.execute(insert(accounts), acc_values)
except Exception as exc:
    print(f'failed batch insertion: {exc}')
finally:
    print('end of transaction')
