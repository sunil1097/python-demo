import pytest
from api.movies_client import get_movie
from utils.data_loader import load_json_data
from utils.schema_validator import validate_schema

test_data = load_json_data("data/movies.json")

@pytest.mark.parametrize("movie", test_data)
def test_get_movies_by_title(base_url, api_key, movie, request):
    # Apply marker dynamically
    request.node.add_marker(getattr(pytest.mark, movie["type"]))

    params = {
        "apikey": api_key,
        "t": movie["title"]
    }

    response = get_movie(base_url, params)
    body = response.json()

    # 🔑 SCHEMA VALIDATION (data-driven)
    validate_schema(body, movie["schema"])

    # 🔑 BUSINESS ASSERTION
    assert body["Response"] == movie["expected_response"]

    # 🔑 ERROR MESSAGE CHECK (only when expected)
    if movie["expected_response"] == "False":
        assert body["Error"] == movie["expected_error"]
