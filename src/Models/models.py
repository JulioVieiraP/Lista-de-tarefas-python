from peewee import Model, CharField, BooleanField
from src.database import db


class Task(Model):
    title = CharField(max_length=255)
    complete = BooleanField(default=False)

    class Meta:
        database = db


db.connect()
db.create_tables([Task])
