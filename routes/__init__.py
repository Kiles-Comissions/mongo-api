from .aggregate import aggregate
from .find import find
from .insert import insert
from .update import update
from .delete import delete

all_routes = [
    aggregate,
    find,
    insert,
    update,
    delete
]

__all__ = ["all_routes"]