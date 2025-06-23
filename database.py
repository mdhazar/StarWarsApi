from mongoengine import connect


def setup_database(app):
    connect(
        db=app.config["MONGODB_SETTINGS"]["db"],
        host=app.config["MONGODB_SETTINGS"]["host"],
        port=app.config["MONGODB_SETTINGS"]["port"],
    )
