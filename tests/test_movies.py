from api.client import get
from utils.schema_validator import validate_schema
def test_get_movies_by_title(base_url,api_key):
    params ={
        "apikey":api_key,
        "t":"Inception"
    }
    response = get(base_url,params)
    assert response.status_code==200
    body =response.json()
    print("Response Body:",body)
    validate_schema(body,"schemas/movie_schema.json")
    assert body["Title"]=="Inception"
    assert body["Response"]=="True"

