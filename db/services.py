from db import session


def create_tables():
    return session.Base.metadata.create_all(bind=session.engine)

def get_db():
    db = session.SessionLocal()
    try:
        yield db
    finally:
        db.close()