import os
import logging
from sanic_json_logging import setup_json_logging
from src.app import app


if os.getenv("APP_ENV") != "live":
    import sys

    LOG_FORMAT = (
        '{"timestamp": "%(asctime)s", "name": "%(name)s", '
        '"level": "%(levelname)s", "message": %(message)s}'
    )
    logging.basicConfig(
        format=LOG_FORMAT,
        level=logging.INFO,
        handlers=[logging.StreamHandler(sys.stdout)]
    )
else:
    setup_json_logging(app)

logger = logging.getLogger("server")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000, access_log=False)
