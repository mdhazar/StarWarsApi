import os


class Config:
    MONGODB_SETTINGS = {
        "db": "starwarsapi",
        "host": "localhost",
        "port": 27017,
    }

    API_TITLE = "Star Wars Characters API"
    API_VERSION = "v1"
    API_DESCRIPTION = """
    A REST API for Star Wars.
    """

    CORS_ORIGINS = ["http://localhost:3000", "http://127.0.0.1:3000"]

    DEBUG = os.getenv("FLASK_DEBUG", "True").lower() == "true"
