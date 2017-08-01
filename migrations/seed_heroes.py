from flask_api.models import database
from flask_api.models.hero import Hero

database.connect()

for hero in Hero.select():
    hero.delete_instance()

heroes = [
  'Mr. Nice',
  'Narco',
  'Bombasto',
  'Celeritas',
  'Magneta',
  'RubberMan',
  'Dynama',
  'Dr IQ',
  'Magma',
  'Tornado'
]

for hero in heroes:
    Hero.create(name=hero)

if not database.is_closed():
        database.close()

