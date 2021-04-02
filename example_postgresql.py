import time

import psycopg2

from get_docker_secret import get_docker_secret


def database_connection(autocommit=True, retries=3, sec_between_retries=1):
    user = get_docker_secret('postgres_user')
    pw = get_docker_secret('postgres_pw')
    for _ in range(3):
        try:
            conn = psycopg2.connect(
                host="database",
                port="5432",
                user=user,
                password=pw,
            )
            conn.autocommit = autocommit
            return conn
        except Exception:
            time.sleep(sec_between_retries)

    raise Exception("Failed to connect to database")


def setup_database(conn_autocommit, database_name="database_name", schema_name="schema_name", table_name="table_name"):
    with conn_autocommit.cursor() as cur:
        cur.execute(f"SELECT 1 FROM pg_catalog.pg_database WHERE datname = '{database_name}';")
        exists = cur.fetchone()
        if not exists:
            cur.execute(f"CREATE DATABASE {database_name}")

        cur.execute(f"CREATE SCHEMA IF NOT EXISTS {schema_name};")
        cur.execute(f"CREATE TABLE IF NOT EXISTS {schema_name}.{table_name} (i integer);")


def main():
    schema_name = "flathunter"
    table_name = "example_table"
    conn_autocommit = database_connection(autocommit=True)
    setup_database(conn_autocommit, database_name="database",
                   schema_name=schema_name,
                   table_name=table_name)
    with conn_autocommit.cursor() as cur:
        cur.execute(f"INSERT INTO {schema_name}.{table_name} VALUES (10);")
        cur.execute(f"SELECT * FROM {schema_name}.{table_name}")
        print(cur.fetchall())


if __name__ == "__main__":
    main()
