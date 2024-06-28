from db_engine import *
from sqlalchemy import union_all

left_stmt = select(users.c.id, users.c.name, accounts.c.type).select_from(users.outerjoin(accounts))

right_stmt = select(users.c.id, users.c.name, accounts.c.type).select_from(accounts.join(users, isouter=True))

full_outer_join_subquery = union_all(left_stmt, right_stmt).subquery()

full_outer_join_stmt = select(full_outer_join_subquery).distinct()

with mysql_engine.connect() as conn:
    result = conn.execute(full_outer_join_stmt)

print('\nfull outer join: \n(id),   (name),   (account type)')
for row in result:
    print(row)
print("-" * 50)

left_stmt = select(users.c.id, users.c.name, accounts.c.type, addresses.c.address).select_from(users.outerjoin(accounts)).outerjoin(addresses, users.c.id == addresses.c.user_id)

right_stmt = select(users.c.id, users.c.name, accounts.c.type, addresses.c.address).select_from(accounts.join(users, isouter=True)).outerjoin(addresses, users.c.id == addresses.c.user_id)

full_outer_join_subquery = union_all(left_stmt, right_stmt).subquery()

full_outer_join_stmt = select(full_outer_join_subquery).distinct()

with mysql_engine.connect() as conn:
    result = conn.execute(full_outer_join_stmt)

# Print the results
print('\nfull outer join 3 tables: \n(id),   (name),   (acc_type),   (address)')
for row in result:
    print(row)
