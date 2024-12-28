from .utils import get_database, is_authorized, serialize
from flask import Blueprint, request

delete = Blueprint("delete", __name__)

@delete.route("/deleteOne", methods=["POST"])
def delete_one_route():
    if not is_authorized(request.headers):
        return {"error": "Unauthorized"}, 401
    
    if request.json is None:
        return {"error": "Invalid JSON"}, 400

    collection = request.json.get("collection", None)
    filter = request.json.get("filter", None)

    if not filter or not collection:
        return {"error": "Filter and collection parameters are required"}, 400

    result = get_database(request)[collection].delete_one(filter)
    return serialize(result.raw_result), 200

@delete.route("/deleteMany", methods=["POST"])
def delete_many_route():
    if not is_authorized(request.headers):
        return {"error": "Unauthorized"}, 401
    
    if request.json is None:
        return {"error": "Invalid JSON"}, 400

    collection = request.json.get("collection", None)
    filter = request.json.get("filter", None)

    if not filter or not collection:
        return {"error": "Filter and collection parameters are required"}, 400

    result = get_database(request)[collection].delete_many(filter)
    return serialize(result.raw_result), 200