
import pytest
import json 


@pytest.fixture(scope="session")
def config():
    with open("config/prod_config.json") as f:
        return json.load(f)
    

@pytest.fixture(scope="session")
def base_url(config):
    return config["base_url"]
    



@pytest.fixture(scope="session")
def api_key(config):
    return config["api_key"]
