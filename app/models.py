from app import db

"""
List of available APIs
GET /api/pokemon/
GET /api/pokemon/{species_id}
GET /api/type/
GET /api/spritename
GET /api/pokemon

"""
class Pokemon(db.Model):
	"""This class represents the Pokemon table."""

	__tablename__ = 'pokemon'

	id = db.Column(db.Integer, primary_key=True)
	name = db.Column()
