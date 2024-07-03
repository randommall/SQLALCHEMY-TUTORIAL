from db_engine import *
from sqlalchemy import event

# @event.listens_for(mysql_engine, 'before_cursor_execute', retval=True)
# def update_order(conn, cursor, statement, parameters, context, executemany):
#     print('-' * 50)
#     print('\nconn: ', conn)
#     print('\ncursor: ', cursor)
#     print('\nstatement: ', statement)
#     print('\nparams: ', parameters)
#     print('\ncontext: ', context)
#     print('\nexecutemany: ', executemany)

#     parameters['age'] = 25
#     print('\nparams: ', parameters)
#     return statement, parameters

@event.listens_for(mysql_engine, 'after_execute')
def create_order_counts_entry(conn, clauseelement, multiparams, params, execution_options, result):
    # print('\nconn: ', conn)
    # print('\nclauseelement: ', clauseelement)
    # print('\nclauseelement.table.name: ', clauseelement.table.name)
    # print('\nresult: ', result)
    # print('\nresult.inserted_params: ', result.last_inserted_params())
    # print('\nresult.inserted_primary_key: ', result.inserted_primary_key)
    # print('\nresult.inserted_primary_key_rows: ', result.inserted_primary_key_rows)
    # print('\nresult.is_insert: ', result.is_insert)
    # print('-' * 50)

    table_name = clauseelement.table.name

    if table_name == 'users' and result.is_insert:
        try:
            user_id = result.inserted_primary_key[0]

            stmt = order_counts.insert().values(user_id=user_id, order_count=0)
            conn.execute(stmt)
        except Exception as exc:
            print(f'An error occurred: {exc}')
        finally:
            print('end of transaction for create_order_counts_entry!')
            print('-' * 50)

@event.listens_for(mysql_engine, 'after_execute')
def update_order_counts(conn, clauseelement, multiparams, params, execution_options, result):
    table_name = clauseelement.table.name

    if table_name == 'orders' and result.is_insert:
        try:
            params = result.last_inserted_params()
            print(params)
            user_id = params.get('user_id')

            stmt = order_counts.update().where(order_counts.c.user_id == user_id).values({order_counts.c.order_count: order_counts.c.order_count + 1})

            conn.execute(stmt)

        except Exception as exc:
            print(f'An error occurred: {exc}')
        finally:
            print('end of transaction for create_order_counts_entry!')
            print('-' * 50)


def table_insertion(table, vals):
    try:
        if isinstance(vals, list):
            with mysql_engine.begin() as conn:
                conn.execute(table.insert(), vals)
        elif isinstance(vals, dict):
            with mysql_engine.begin() as conn:
                conn.execute(table.insert().values(**vals))
    except Exception as exc:
        print(f'An error occured: {exc}')
    finally:
        print('end of insertion!')
        print('-' * 50)

# create multiple user row values
batch_users_values = [
    {"name": "Gladis", "email": "Gladis@email.com", "age": 18},
    {"name": "O'well", "email": "O'well@email.com", "age": 29},
]

# create single user row values
single_user_values = {"name": 'Bengal', "email": "Bengal@email.com", "age": 23}

# create single order row values
single_order_values = {"item": "Headphones", "user_id": 9}

table_insertion(orders, single_order_values)
