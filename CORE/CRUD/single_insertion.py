from db_engine import *

statement1 = users.insert().values(name="Johnson",
                                   email="johnson@email.com",
                                   age=100)

acc_values = {
    'type': 'checkings',
    'user_id': 1
}

statement2 = insert(accounts).values(**acc_values)

# try:
#     with mysql_engine.connect() as conn:
#         conn.execute(statement1)
#         conn.execute(statement2)

#         conn.commit()
# except Exception as exc:
#     conn.rollback()
#     print(f'error inserting values: {exc}')
# finally:
#     print('end of transaction')

try:
    with mysql_engine.begin() as conn:
        conn.execute(statement1)
        conn.execute(statement2)
except Exception as exc:
    print(f'error inserting values: {exc}')
finally:
    print('end of transaction')
