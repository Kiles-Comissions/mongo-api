from .utils import get_database, is_authorized, serialize
from flask import Blueprint, request

insert = Blueprint("insert", __name__)

@insert.route("/insertOne", methods=["POST"])
def insert_one_route():
    if not is_authorized(request.headers):
        return {"error": "Unauthorized"}, 401
    
    if request.json is None:
        return {"error": "Invalid JSON"}, 400

    collection = request.json.get("collection", None)
    document = request.json.get("document", None)

    if not document or not collection:
        return {"error": "Document and collection parameters are required"}, 400

    result = get_database(request)[collection].insert_one(document)
    return serialize({"_id": result.inserted_id}), 200

@insert.route("/insertMany", methods=["POST"])
def insert_many_route():
    if not is_authorized(request.headers):
        return {"error": "Unauthorized"}, 401
    
    if request.json is None:
        return {"error": "Invalid JSON"}, 400

    collection = request.json.get("collection", None)
    documents = request.json.get("documents", None)

    if not documents or not collection:
        return {"error": "Documents and collection parameters are required"}, 400

    result = get_database(request)[collection].insert_many(documents)
    return serialize([{"_id": i} for i in result.inserted_ids ]), 200