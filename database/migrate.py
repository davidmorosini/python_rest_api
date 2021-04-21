import os
import logging
import alembic.config

logger = logging.getLogger("Migrations")

alembicArgs = [
    "--raiseerr",
    "upgrade",
    "head"
]


async def run_migrations():
    user = os.getenv("DATABASE_USER")
    password = os.getenv("DATABASE_PASSWORD")
    host = os.getenv("DATABASE_HOST")
    port = int(os.getenv("DATABASE_PORT", 5432))
    database = os.getenv("DATABASE_NAME")
    url = f"postgresql://{user}:{password}@{host}:{port}/{database}"
    os.environ["DB_URL"] = url

    try:
        alembic.config.main(argv=alembicArgs)
    except Exception as e:
        return str(e)

    return "Successful migration!"
