from uuid import uuid4
from fastapi import APIRouter, HTTPException
from passlib.context import CryptContext

from app.schemas.schemas import User_Pydantic, UserCreate,  Game_Pydantic, PlayedGame_Pydantic, User, PlayedGame, Game

game_router = APIRouter()


pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


@game_router.post("/users", response_model=User_Pydantic)
async def create_user(user: UserCreate):
    # Überprüfe, ob die E-Mail bereits verwendet wird
    existing_user = await User.filter(email=user.email).first()
    if existing_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    
    # Erstelle den neuen Benutzer
    user_obj = await User.create(
        username=user.username,
        email=user.email,
        password_hash=pwd_context.hash(user.password)
    )
    return await User_Pydantic.from_tortoise_orm(user_obj)


@game_router.get("/users", response_model=list[User_Pydantic])
async def get_users():
    users = await User.all()
    return await User_Pydantic.from_queryset(users)


@game_router.post("/games", response_model=Game_Pydantic)
async def create_game():
    game_obj = await Game.create(game_id=str(uuid4()))
    return await Game_Pydantic.from_tortoise_orm(game_obj)


@game_router.post("/games/{game_id}/join", response_model=Game_Pydantic)
async def join_game(game_id: str, user_id: int):
    game = await Game.get(game_id=game_id)
    user = await User.get(id=user_id)
    await game.players.add(user)
    return await Game_Pydantic.from_tortoise_orm(game)


@game_router.post("/games/{game_id}/end", response_model=PlayedGame_Pydantic)
async def end_game(game_id: str, loser_id: int):
    game = await Game.get(game_id=game_id)
    loser = await User.get(id=loser_id)
    played_game = await PlayedGame.create(game=game, loser=loser)
    return await PlayedGame_Pydantic.from_tortoise_orm(played_game)


@game_router.get("/games/{game_id}", response_model=Game_Pydantic)
async def get_game(game_id: str):
    game = await Game.get(game_id=game_id)
    return await Game_Pydantic.from_tortoise_orm(game)


@game_router.get("/played_games/{game_id}", response_model=PlayedGame_Pydantic)
async def get_played_game(game_id: str):
    played_game = await PlayedGame.get(game_id=game_id)
    return await PlayedGame_Pydantic.from_tortoise_orm(played_game)
