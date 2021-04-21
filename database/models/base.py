from peewee import Model
from database import controller


class BaseModel(Model):
    _manager = controller.manager

    class Meta:
        database = controller.database_config

    @classmethod
    async def async_select(cls, *args):
        if len(args) > 0:
            statement = cls.select().where(*args)
        else:
            statement = cls.select()
        return await cls._manager.execute(statement)

    @classmethod
    async def async_get(cls, *args):
        return await cls._manager.get(cls.select().where(*args))

    @classmethod
    async def async_get_last(cls, *args):
        return await cls._manager.get(
            cls.select().where(*args).order_by(cls.id.desc())
        )

    @classmethod
    async def async_create(cls, **kwargs):
        return await cls._manager.create(cls, **kwargs)

    @classmethod
    async def async_get_or_create(cls, **kwargs):
        return await cls._manager.get_or_create(cls, **kwargs)

    @classmethod
    async def async_create_or_get(cls, **kwargs):
        return await cls._manager.create_or_get(cls, **kwargs)

    @classmethod
    async def async_count(cls, *args):
        return await cls._manager.count(cls.select().where(*args))

    async def async_save(self):
        return await self._manager.update(self, only=self.dirty_fields)

    async def async_delete(self):
        return await self._manager.delete(self)
