import logging
import peewee_async
import peewee_asyncext
from database.configs import DATABASE


MAX_CONNECTIONS = 5
logger = logging.getLogger("DatabaseControllerPeewee")

# Start connection pool and objects manager
database_config = peewee_asyncext.PooledPostgresqlExtDatabase(
    **DATABASE,
    autorollback=True,
    max_connections=MAX_CONNECTIONS,
    register_hstore=False
)
manager = peewee_async.Manager(database_config)


async def execute(sql):
    return await database_config.execute(sql)


async def close_connections():
    database_config.close()
