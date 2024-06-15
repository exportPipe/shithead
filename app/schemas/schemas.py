from pydantic import BaseModel, EmailStr
from tortoise.contrib.pydantic import pydantic_model_creator

from app.database.models.models import User, Game, PlayedGame


class UserCreate(BaseModel):
    username: str
    email: EmailStr
    password: str


# Pydantic models for data validation and serialization
User_Pydantic = pydantic_model_creator(User, name="User")
UserIn_Pydantic = pydantic_model_creator(User, name="UserIn", exclude_readonly=True)
Game_Pydantic = pydantic_model_creator(Game, name="Game")
PlayedGame_Pydantic = pydantic_model_creator(PlayedGame, name="PlayedGame")
