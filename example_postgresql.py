import psycopg2


def database_connection(autocommit=True):
    conn = psycopg2.connect(
        host="localhost",
        port="5432",
        user="postgres",
        password="example",
    )
    conn.autocommit = autocommit
    return conn


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
