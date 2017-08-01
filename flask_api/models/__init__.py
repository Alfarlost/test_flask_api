from peewee import PostgresqlDatabase

database = PostgresqlDatabase(
    'flask_api',  # Required by Peewee.
    user='postgres',  # Will be passed directly to psycopg2.
    password='',  # Ditto.
    host='localhost',  # Ditto.
)
