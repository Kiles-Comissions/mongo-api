from .utils import get_database, is_authorized, serialize
from flask import Blueprint, request

aggregate = Blueprint("aggregate", __name__)


@aggregate.route("/aggregate", methods=["POST"])
def aggregate_route():
    if not is_authorized(request.headers):
        return {"error": "Unauthorized"}, 401
    
    if request.json is None:
        return {"error": "Invalid JSON"}, 400
    
    collection = request.json.get("collection")
    pipeline = request.json.get("pipeline")

    if not pipeline or not collection:
        return {"error": "Pipeline and collection parameters are required"}, 400
    
    result = get_database(request)[collection].aggregate(pipeline)
    return serialize(result), 200
