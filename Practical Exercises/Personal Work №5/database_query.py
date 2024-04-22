import sqlite3 as sql

connection = sql.connect("insurance_company.db")


def log_decorator(func):
    def wrapper(*args, **kwargs):
        print(f"\nCall function: {func.__name__}")
        return func(*args, **kwargs)
    return wrapper


@log_decorator
def select_from_database_all_clients():
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM Clients")
    for row in cursor.fetchall():
        print(row)


@log_decorator
def select_clients_join_with_contracts():
    cursor = connection.cursor()
    cursor.execute("select id, first_name, last_name, passport, contracts_№, object_id from Clients "
                   "join main.Contracts C on Clients.id = C.client_id")
    for row in cursor.fetchall():
        print(row)


@log_decorator
def select_contracts_with_objects():
    cursor = connection.cursor()
    cursor.execute("select contracts_№, client_id, object, contract_date, insurance_payment, object from Contracts "
                   "join main.Insurance_Objects IO on IO.id = Contracts.object_id")
    for row in cursor.fetchall():
        print(row)


select_from_database_all_clients()
select_clients_join_with_contracts()
select_contracts_with_objects()
