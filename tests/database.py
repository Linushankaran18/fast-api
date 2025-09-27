from fastapi.testclient import TestClient
import pytest
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base 
from app.database import SessionLocal, get_db
from app.main import app
from app.config import settings
from sqlalchemy.orm import sessionmaker

from app.database import Base


#SQLALCHEMY_DATABASE_URL = 'postgresql://postgres:Linush18@localhost:5432/fastapi_test'
SQLALCHEMY_DATABASE_URL = f"postgresql://{settings.database_username}:{settings.database_password}@{settings.database_hostname}:{settings.database_port}/{settings.database_name}_test"

engine = create_engine(SQLALCHEMY_DATABASE_URL)

TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base.metadata.create_all(bind=engine)


# 04. Create the database session dependency

def override_get_db():
    db = TestingSessionLocal()
    try:
        yield db
    finally:
        db.close()

client = TestClient(app)

app.dependency_overrides[get_db] = override_get_db

@pytest.fixture(scope="module")
def session():
    #run our code after we run our test finishes (just track the bugs using -x)
    Base.metadata.drop_all(bind=engine)
    #run our code before we run our test
    Base.metadata.create_all(bind=engine)
    # alembic also suitable for this

    db = TestingSessionLocal()
    try:
        yield db
    finally:
        db.close()

@pytest.fixture(scope="module")
def client(session):
    def override_get_db():
    
        try:
            yield session
        finally:
            session.close()
    app.dependency_overrides[get_db] = override_get_db
    yield TestClient(app)