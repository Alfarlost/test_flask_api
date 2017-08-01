from flask_api.models import database
from flask_api.models.hero import Hero

database.connect()
database.create_tables([Hero])
