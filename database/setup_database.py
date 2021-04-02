
def setup_database(conn_autocommit, database_name="default_database"):
    with conn_autocommit.cursor() as cur:
        cur.execute(f"SELECT 1 FROM pg_catalog.pg_database WHERE datname = '{database_name}';")
        exists = cur.fetchone()
        if not exists:
            cur.execute(f"CREATE DATABASE {database_name}")