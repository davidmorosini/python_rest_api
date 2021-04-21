import peewee
import logging
from playhouse.postgres_ext import DateTimeTZField, JSONField
from database.utils import now_br
from database.models.base import BaseModel

logger = logging.getLogger("Events")


class Events(BaseModel):
    id = peewee.AutoField(primary_key=True)
    user = peewee.CharField()
    route = peewee.CharField()
    address = peewee.CharField()
    method = peewee.CharField()
    request_body = JSONField(null=True)
    response_body = JSONField(null=True)
    status_code = peewee.IntegerField()
    created_at = DateTimeTZField(default=now_br)

    class Meta:
        table_name = "Events"

    @classmethod
    async def async_create(cls, **kwargs):
        return await super().async_create(**kwargs)
