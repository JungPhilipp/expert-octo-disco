import time

import psycopg2

from get_docker_secret import get_docker_secret


def database_connection(autocommit=True, retries=3, sec_between_retries=1):
    user = get_docker_secret('postgres_user')
    pw = get_docker_secret('postgres_pw')
    for _ in range(retries):
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