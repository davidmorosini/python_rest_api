from database.models import Clients
from database.models import Events
from database.models import Routes
import src.controllers.database_peewee as database_peewee_ctrl


async def create_tables():
    database_peewee_ctrl.database.create_tables(
        [Clients, Events, Routes],
        safe=True
    )
