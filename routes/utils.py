from pymongo import MongoClient, cursor, command_cursor
from bson import ObjectId, Timestamp
from os import environ
from typing import Iterable, Mapping, Any
from flask import Request

client = MongoClient(environ["MONGO_URI"])
DB = client[environ["DB_NAME"]]


def is_authorized(headers):
    if "Authorization" not in headers:
        return False
    return environ["API_KEY"] == headers["Authorization"]

def get_database(request: Request):
    if request.json.get("database", False): # type: ignore
        return client[request.json.get("database")] # type: ignore
    return DB


def serialize_doc(doc: dict | Mapping[str, Any]) -> dict:
    """Serializes any ObjectId fields in a document"""
    new = {}
    # We don't want to the properties of the original document to be modified
    # because pymongo does not like that
    for key, value in doc.items():
        if isinstance(value, ObjectId):
            new[key] = str(value)
        elif isinstance(value, Timestamp):
            new[key] = value.time
        elif isinstance(value, bytes):
            new[key] = str(value)
        elif isinstance(value, dict):
            new[key] = serialize_doc(value)
        elif isinstance(value, list):
            new[key] = serialize(value)
        else:
            new[key] = value
    return new


def serialize(
    doc: cursor.Cursor | command_cursor.CommandCursor | Iterable | Mapping[str, Any],
) -> list[Mapping[str, Any]] | dict:
    """Serializes any ObjectId fields in a document"""
    if isinstance(doc, dict):
        return serialize_doc(doc)
    else:  # If the doc is a list
        return [serialize_doc(doc) for doc in doc] # type: ignore
