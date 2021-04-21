import logging
from database import run_migrations

logger = logging.getLogger("listeners")


async def notify_server_started(app, loop):
    response = await run_migrations()
    logger.info(f"Migrations complete: {response}")
