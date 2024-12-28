from .utils import get_database, is_authorized, serialize
from flask import Blueprint, request

update = Blueprint("update", __name__)


@update.route("/updateOne", methods=["POST"])
def update_one_route():
    if not is_authorized(request.headers):
        return {"error": "Unauthorized"}, 401

    if request.json is None:
        return {"error": "Invalid JSON"}, 400

    collection = request.json.get("collection", None)
    filter = request.json.get("filter", None)
    update = request.json.get("update", None)

    if not update or not filter or not collection:
        return {"error": "Filter, update, and collection parameters are required"}, 400

    result = get_database(request)[collection].update_one(filter, update)

    if result.raw_result is None:
        return {"error": "No document found"}, 404
    
    return serialize(result.raw_result), 200


@update.route("/updateMany", methods=["POST"])
def update_many_route():
    if not is_authorized(request.headers):
        return {"error": "Unauthorized"}, 401
    
    if request.json is None:
        return {"error": "Invalid JSON"}, 400

    collection = request.json.get("collection", None)
    filter = request.json.get("filter", None)
    update = request.json.get("update", None)

    if not update or not filter or not collection:
        return {"error": "Filter, update, and collection parameters are required"}, 400

    result = get_database(request)[collection].update_many(filter, update)

    if result.raw_result is None:
        return {"error": "No document found"}, 404

    return serialize(result.raw_result), 200
