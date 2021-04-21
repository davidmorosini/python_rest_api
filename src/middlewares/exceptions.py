import logging
from sanic import response


logger = logging.getLogger("middlewares")


async def handle_internal_error(request, exception):
    if isinstance(exception, str):
        message = exception
    else:
        message, reason, fail_point = exception
    logger.exception(message)
    return response.json({"message": message}, status=500)


async def handle_request_timeout(request, exception):
    exception = exception.args[0]
    if isinstance(exception, str):
        message = exception
    else:
        message, reason, fail_point = exception

    return response.json({"error": message}, status=408)


async def handle_unauthorized(request, exception):
    exception = exception.args[0]
    if isinstance(exception, str):
        message = exception
    else:
        message, reason, fail_point = exception

    return response.json({"message": message}, status=401)


async def handle_not_found(request, exception):
    logger.info("hahahahahah")
    return response.json({"message": "Not Found route"}, status=404)
