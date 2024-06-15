from tortoise import fields, models


class User(models.Model):
    id = fields.IntField(pk=True)
    username = fields.CharField(max_length=50, unique=True)
    email = fields.CharField(max_length=100, unique=True)
    password_hash = fields.CharField(max_length=128)

    created_at = fields.DatetimeField(auto_now_add=True)

    def __str__(self):
        return self.username


class Game(models.Model):
    id = fields.IntField(pk=True)
    game_id = fields.UUIDField(unique=True)
    players = fields.ManyToManyField("models.User", related_name="games")
    status = fields.CharField(max_length=20, default="waiting")

    created_at = fields.DatetimeField(auto_now_add=True)

    def __str__(self):
        return f"Game {self.game_id}"


class PlayedGame(models.Model):
    id = fields.IntField(pk=True)
    game = fields.ForeignKeyField("models.Game", related_name="played_games")
    loser = fields.ForeignKeyField("models.User", related_name="lost_games")
    ended_at = fields.DatetimeField(auto_now_add=True)

    def __str__(self):
        return f"Played Game {self.game.id} - Loser: {self.loser.username}"
