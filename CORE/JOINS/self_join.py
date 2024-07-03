from db_engine import *

# values = [
#     {"name": "Johnson Bourne", "email": "Johnson@email.com", "position": "CEO"},
#     {"name": "Jayson Bourne", "email": "Jayson@email.com", "position": "CTO", "manager_id": 1},
#     {"name": "Jane Dennis", "email": "Jane@email.com", "position": "Manager", "manager_id": 1},
#     {"name": "Ben Lionel", "email": "Lionel@email.com", "position": "Engineer", "manager_id": 2},
#     {"name": "Carl Jayson", "email": "Carl@email.com", "position": "Accountant", "manager_id": 3}
#     ]

# with mysql_engine.begin() as conn:
#     conn.execute(employees.insert(), values)

managers = employees.alias('managers')

stmt1 = select(employees, managers).select_from(employees.join(managers, employees.c.manager_id == managers.c.id))

with mysql_engine.connect() as conn:
    result1 = conn.execute(stmt1)

print("\nstatement1 - basic self join for all columns:")
for row in result1:
    print(row)

stmt2 = select(
    employees.c.id.label('employee_id'),
    employees.c.name.label('employee_name'),
    employees.c.position.label('employee_position'),
    managers.c.id.label('manager_id'),
    managers.c.name.label('manager_name'),
    managers.c.position.label('manager_position'),
).select_from(employees.join(managers, employees.c.manager_id == managers.c.id))

with mysql_engine.connect() as conn:
    result2 = conn.execute(stmt2)


print("\nstatement2 - self join for selected columns:")
for row in result2:
    print(f"Employee: \nid: {row[0]}, name: {row[1]}, position: {row[2]}")
    print(f"Manager: \nid: {row[3]}, name: {row[4]}, position: {row[5]}")

stmt3 = select(
    employees.c.id.label('employee_id'),
    employees.c.name.label('employee_name'),
    employees.c.position.label('employee_position'),
    managers.c.id.label('manager_id'),
    managers.c.name.label('manager_name'),
    managers.c.position.label('manager_position'),
).select_from(employees.join(managers, employees.c.manager_id == managers.c.id)).where(employees.c.manager_id == 1)

with mysql_engine.connect() as conn:
    result3 = conn.execute(stmt3)


print("\nstatement2 - self join for selected columns:")
for row in result3:
    print(f"Employee: \nid: {row[0]}, name: {row[1]}, position: {row[2]}")
    print(f"Manager: \nid: {row[3]}, name: {row[4]}, position: {row[5]}")
