import pytest
from api.movies_client import get_movie
from utils.data_loader import load_test_data
test_data =load_test_data("data/movies.json")

@pytest.mark.parametrize("movie",test_data)
def test_get_movies_by_title(base_url,api_key,movie):
    params ={
        "apikey":api_key,
        "t":movie["title"]
    }
    response =get_movie(base_url,params)
    body=response.json()

    assert body["Response"]== movie["expected"]