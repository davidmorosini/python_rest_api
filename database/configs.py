from os import getenv

DATABASE = dict(
    host=getenv("DATABASE_HOST"),
    user=getenv("DATABASE_USER"),
    password=getenv("DATABASE_PASSWORD"),
    database=getenv("DATABASE_NAME"),
    port=int(getenv("DATABASE_PORT", 5432))
)
