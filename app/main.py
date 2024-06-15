# app/main.py
from fastapi import FastAPI
from tortoise.contrib.fastapi import register_tortoise

from starlette.middleware.cors import CORSMiddleware

from app.api.game_router import game_router

app = FastAPI()

register_tortoise(
    app,
    db_url="sqlite://db.sqlite3",
    modules={"models": ["app.database.models.models"]},
    generate_schemas=True,
    add_exception_handlers=True,
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)


app.include_router(game_router, prefix='/api')
