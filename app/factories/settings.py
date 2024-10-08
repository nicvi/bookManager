import os

class Settings:
    JSON_DATA_SOURCE = os.getenv(
        "JSON_DATA_SOURCE",
        "app/data/book_management_db.json"
    )

settings = Settings()
