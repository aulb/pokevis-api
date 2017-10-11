# What I want to do
"""
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

| HTTP Method | URI | Action |
| --- | --- | --- |
| GET | /v1/pokemon | Retrieve all Pokemon (+forms) |
| GET | /v1/pokemon/{id} | Retrieve a Pokemon |
| GET | /v1/spritename | Retrieve the spritename for a Pokemon |

# Goals for this project
1) Clear TDD
2) Initial installation with Flask
3) Proper documentations
4) More commits and necessary branchings

# Resources
http://www.vinaysahni.com/best-practices-for-a-pragmatic-restful-api
https://hackernoon.com/restful-api-designing-guidelines-the-best-practices-60e1d954e7c9
http://flask.pocoo.org/docs/0.12/patterns/sqlalchemy/
https://stackoverflow.com/questions/30967822/when-do-i-use-path-params-vs-query-params-in-a-restful-api
https://scotch.io/tutorials/build-a-restful-api-with-flask-the-tdd-way

# Commands needed
`brew services start postgresql`
`pip install Flask-Script` 

setenv when run venv
createdb
turn on psql

# Test database
createdb test_pokevis_api
dropdb -> to drop

# Main database
pokevis_api
