
import logging
import os
import time

from psycopg2 import pool

logger = logging.getLogger(__name__)

connection_pool = None


def initialize_database():
    global connection_pool

    if connection_pool is not None:
        return

    delay = 1

    while True:
        try:
            connection_pool = pool.ThreadedConnectionPool(
                minconn=1,
                maxconn=10,
                host=os.environ["DB_HOST"],
                port=int(os.getenv("DB_PORT", "5432")),
                dbname=os.environ["DB_NAME"],
                user=os.environ["DB_USER"],
                password=os.environ["DB_PASSWORD"],
                connect_timeout=3,
            )

            logger.info("Database connection pool ready")
            return

        except Exception as error:
            logger.warning(
                "Database unavailable: %s. Retrying in %s seconds",
                error,
                delay,
            )

            time.sleep(delay)
            delay = min(delay * 2, 10)


def get_connection():
    if connection_pool is None:
        raise RuntimeError("Database pool not initialized")

    return connection_pool.getconn()


def release_connection(connection):
    if connection_pool is not None:
        connection_pool.putconn(connection)


def database_is_ready():
    connection = None

    try:
        connection = get_connection()

        with connection.cursor() as cursor:
            cursor.execute("SELECT 1")
            cursor.fetchone()

        return True

    except Exception:
        if connection is not None:
            connection.rollback()
        return False

    finally:
        if connection is not None:
            release_connection(connection)
