import json
import os
from jsonschema import validate

BASE_DIR = os.path.dirname(os.path.dirname(__file__))

SCHEMA_MAP = {
    "success": os.path.join(BASE_DIR, "schemas", "movie_success_schema.json"),
    "error": os.path.join(BASE_DIR, "schemas", "movie_error_schema.json")
}

def validate_schema(data, schema_type):
    schema_path = SCHEMA_MAP[schema_type]
    with open(schema_path) as f:
        schema = json.load(f)
    validate(instance=data, schema=schema)
