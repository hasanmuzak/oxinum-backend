from db import config

def get_db():
    db = config.Session()
    try:
        yield db
    finally:
        db.close()