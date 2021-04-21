import logging
import json
from database.models import Events

logger = logging.getLogger("middlewares")


async def rate_limit(request):
    pass


async def authenticate(request):
    anonymous_routes = ["/status", "/test"]

    request_path = request.path
    if request_path in anonymous_routes:
        return


async def treat_request_body(request):
    pass


async def logging_request(request):
    body = request.body or "{}"
    logger.info(json.loads(body))


async def logging_response(request, response):
    body = response.body or "{}"
    response_body = json.loads(body)
    logger.info(response_body)

    body = request.body or "{}"
    request_body = json.loads(body)

    event = {
        "user": "david",
        "route": request.path,
        "address": "localhost",
        "method": "GET",
        "request_body": request_body,
        "response_body": response_body,
        "status_code": response.status
    }
    await Events.async_create(**event)
