from database.connection import database_connection
from database.setup_database import setup_database


def main():
    schema_name = "flathunter"
    table_name = "example_table"
    conn_autocommit = database_connection(autocommit=True)
    setup_database(conn_autocommit)
    with conn_autocommit.cursor() as cur:
        cur.execute(f"CREATE SCHEMA IF NOT EXISTS {schema_name};")
        cur.execute(f"CREATE TABLE IF NOT EXISTS {schema_name}.{table_name} (i integer);")

        cur.execute(f"INSERT INTO {schema_name}.{table_name} VALUES (10);")
        cur.execute(f"SELECT * FROM {schema_name}.{table_name}")
        print(cur.fetchall())


if __name__ == "__main__":
    main()
