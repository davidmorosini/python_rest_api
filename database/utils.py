import os
import pytz
import datetime


def now():
    return datetime.datetime.utcnow().replace(tzinfo=pytz.UTC)


def now_br():
    return now().astimezone(pytz.timezone("America/Sao_Paulo"))
