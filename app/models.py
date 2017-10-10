from app import db

"""
# https://stackoverflow.com/questions/30967822/when-do-i-use-path-params-vs-query-params-in-a-restful-api
# https://scotch.io/tutorials/build-a-restful-api-with-flask-the-tdd-way
List of available APIs
GET /v1/pokemon 
GET /v1/pokemon?
	- type
	- type1
	- type2
	- generation
	- species
GET /v1/pokemon/{id}
GET /v1/type/
GET /v1/spritename
"""
class Pokemon(db.Model):
	"""This class represents the Pokemon table."""

	__tablename__ = 'pokemon'

	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String(64))
	species_id = db.Column(db.Integer)
	generation = db.Column(db.Integer)
	is_default = db.Column(db.Integer)

	def __init__(self, id, name, species_id, generation, is_default):
		self.id = id
		self.name = name
		self.species_id = species_id
		self.generation = generation
		self.is_default = is_default
	
	# Learn about decorator
	@staticmethod
	def get_all():
		return Pokemon.query.all()

	def __repr__(self):
		return '<Pokemon: {}>'.format(self.name)
