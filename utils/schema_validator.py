import json
from jsonschema import validate
def validate_schema(data,schema_path):
    with open(schema_path) as f:
        schema =json.load(f)

    validate(instance=data,schema=schema)