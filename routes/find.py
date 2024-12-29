from .utils import get_database, is_authorized, serialize
from flask import Blueprint, request

find = Blueprint("find", __name__)


@find.route("/find", methods=["POST"])
def find_route():
    if not is_authorized(request.headers):
        return {"error": "Unauthorized"}, 401

    if request.json is None:
        return {"error": "Invalid JSON"}, 400

    collection = request.json.get("collection", None)
    filter = request.json.get("filter", None)

    if collection is None or filter is None:
        return {"error": "Collection and filter parameters are required"}, 400

    results = get_database(request)[collection].find(filter)
    return serialize(results)


@find.route("/findOne", methods=["POST"])
def find_one_route():
    if not is_authorized(request.headers):
        return {"error": "Unauthorized"}, 401

    if request.json is None:
        return {"error": "Invalid JSON"}, 400

    collection = request.json.get("collection", None)
    filter = request.json.get("filter", None)

    if not collection or not filter:
        return "Collection and filter parameters are required", 400

    result = get_database(request)[collection].find_one(filter)

    if not result:
        return {}, 200

    return serialize(result), 200
