
import logging
from sanic import Sanic
from sanic.blueprints import Blueprint
from sanic.exceptions import (
    Unauthorized,
    Forbidden,
    NotFound,
    ServerError,
    RequestTimeout
)
from src.routes import (
    bp_root
)
from src.middlewares import (
    handle_internal_error,
    handle_not_found,
    handle_request_timeout,
    handle_unauthorized,
    rate_limit,
    authenticate,
    treat_request_body,
    logging_request,
    logging_response,
    notify_server_started
)


url_prefix = "/1"
app = Sanic(__name__)

api = Blueprint.group(
    bp_root,
    url_prefix=url_prefix
)
app.blueprint(api)

logger = logging.getLogger("server")

configs = {
    "REQUEST_TIMEOUT": 60,  # 60s
    "RESPONSE_TIMEOUT": 60,  # 60s
    "KEEP_ALIVE": False,
    "GRACEFUL_SHUTDOWN_TIMEOUT": 10
}
app.config.update(configs)

# Register Listeners
app.register_listener(notify_server_started, "after_server_start")

# Register Middlewares
app.register_middleware(rate_limit, "request")
app.register_middleware(authenticate, "request")
app.register_middleware(treat_request_body, "request")
app.register_middleware(logging_request, "request")
app.register_middleware(logging_response, "response")

# Register Excptions Handlers
app.error_handler.add(ServerError, handle_internal_error)
app.error_handler.add(RequestTimeout, handle_request_timeout)
app.error_handler.add(Unauthorized, handle_unauthorized)
app.error_handler.add(Forbidden, handle_unauthorized)
app.error_handler.add(NotFound, handle_not_found)
