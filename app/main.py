
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from . import models
from .database import engine
from .routers import post, user, auth, vote
from .config import settings

print(settings.database_password)

# 03. Create the database tables

# models.Base.metadata.create_all(bind=engine) comment this out after created alembic migrations

app = FastAPI()

# 07 Create a Pydantic model for the Post named as schema.py
# 08 import the schema and changed Post as schemas.Post (request schema)``
# 09 extend the schemas for create and update
# 10 define how repose should look like

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(post.router)
app.include_router(user.router)
app.include_router(auth.router)
app.include_router(vote.router)

@app.get("/")
def root():
    return {"message": "welcome to my API "}
