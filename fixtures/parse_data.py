import json

def parse_json_data(json_filename):
	with open(json_filename, 'r') as opened_file:
		json_data = json.load(opened_file)
		return json_data
