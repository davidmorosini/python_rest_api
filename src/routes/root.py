import os
from datetime import datetime
from sanic import Blueprint, response, request


bp_root = Blueprint("root")


@bp_root.route("/test")
@bp_root.route("/status")
async def status(request: request.Request) -> response.BaseHTTPResponse:
    return response.json({
        "status": "ok",
        "application": "rest-api",
        "environment": os.environ.get("APP_ENV", "development"),
        "date": datetime.now().isoformat()
    })
