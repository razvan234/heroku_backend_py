import os
from pydantic import BaseSettings
from functools import lru_cache


class PlacesAPI(BaseSettings):
    app_key: str = os.getenv("PlacesAPI", "[MASKED]")
    
@lru_cache()
def get_places_settings() -> BaseSettings:
    return PlacesAPI()