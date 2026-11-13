#!/usr/bin/python3
import json
"""Module for converting Python objects to JSON strings."""


def to_json_string(my_obj):
    """Return JSON representation of an object."""
    return json.dumps(my_obj)
