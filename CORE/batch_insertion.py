from db_engine import *

users_values = [
    {"name": "Johnson", "email": "johnson@email.com", "age": 20},
    {"name": "Ben", "email": "Ben@email.com", "age": 123},
    {"name": "Alice", "email": "Alice@email.com", "age": 25},
    {"name": "Cleo", "email": "Cleo@email.com", "age": 19},
    {"name": "Bousquet", "email": "Bousquet@email.com", "age": 19},
    {"name": "Vinicius", "email": "Vinicius@email.com", "age": 19},
    {"name": "Guler", "email": "Guler@email.com", "age": 19}
]

acc_values = [
    {"type": 'checkings', "user_id": 1},
    {"user_id": 2, "type": "savings"},
    {"user_id": 3, "type": "savingss"},
    {"type": "checkings", "user_id": 4},
    {"user_id": None, "type": "savingss"},
    {"user_id": None, "type": "savingss"},
    {"user_id": None, "type": "savingss"},
]

addr_values = [
    {"address": "1010 Wayne street, CAL", "user_id": 1},
    {"address": "2020 Wayne street, CAL", "user_id": 2},
    {"address": "3030 Wayne street, CAL", "user_id": 3},
    {"address": "4040 Wayne street, CAL", "user_id": 4},
    {"address": "4040 Wayne street, CAL", "user_id": 5},
    {"address": "4040 Wayne street, CAL", "user_id": None},
    {"address": "4040 Wayne street, CAL", "user_id": None}
]

try:
    with mysql_engine.begin() as conn:
        conn.execute(users.insert(), users_values)
        conn.execute(insert(accounts), acc_values)
        conn.execute(addresses.insert(), addr_values)
except Exception as exc:
    print(f'failed batch insertion: {exc}')
finally:
    print('end of transaction')
