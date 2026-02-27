from dataclasses import dataclass
from typing import List, Dict, Union
from flask import Flask, request, jsonify
import re

# ==== Type Definitions, feel free to add or modify ===========================
@dataclass
class CookbookEntry:
	name: str

@dataclass
class RequiredItem():
	name: str
	quantity: int

@dataclass
class Recipe(CookbookEntry):
	required_items: List[RequiredItem]

@dataclass
class Ingredient(CookbookEntry):
	cook_time: int


# =============================================================================
# ==== HTTP Endpoint Stubs ====================================================
# =============================================================================
app = Flask(__name__)

# Store your recipes here!
cookbook: Dict[str, CookbookEntry] = {}

# Task 1 helper (don't touch)
@app.route("/parse", methods=['POST'])
def parse():
	data = request.get_json()
	recipe_name = data.get('input', '')
	parsed_name = parse_handwriting(recipe_name)
	if parsed_name is None:
		return 'Invalid recipe name', 400
	return jsonify({'msg': parsed_name}), 200

# [TASK 1] ====================================================================
# Takes in a recipeName and returns it in a form that 
def parse_handwriting(recipeName: str) -> Union[str | None]:
	recipeName = recipeName.replace('-', ' ').replace('_', ' ')
	recipeName = re.sub(r'[^a-zA-Z\s]', '', recipeName)
	words = recipeName.split()
	parsed_name = ' '.join(word.capitalize() for word in words)
	return parsed_name if len(parsed_name) > 0 else None


# [TASK 2] ====================================================================
# Endpoint that adds a CookbookEntry to your magical cookbook
@app.route('/entry', methods=['POST'])
def create_entry():
	data = request.get_json()
	if not isinstance(data, dict):
		return 'Invalid format', 400

	type_ = data.get('type')
	name = str(data.get('name', ''))

	if type_ not in ['recipe', 'ingredient']:
		return 'Invalid type', 400
	if name in cookbook:
		return 'Name must be unique', 400

	if type_ == 'ingredient':
		cook_time = int(data.get('cookTime', -1) if data.get('cookTime') is not None else -1)
		if cook_time < 0 or not isinstance(data.get('cookTime'), int):
			return 'Invalid cookTime', 400
		cookbook[name] = Ingredient(name=name, cook_time=cook_time)

	elif type_ == 'recipe':
		required_items_data = data.get('requiredItems', [])
		seen_items = set()
		required_items = []
		for item in required_items_data:
			item_name = str(item.get('name', ''))
			if item_name in seen_items:
				return 'Duplicate item in recipe', 400
			seen_items.add(item_name)
			required_items.append(RequiredItem(name=item_name, quantity=int(item.get('quantity', 0))))
		cookbook[name] = Recipe(name=name, required_items=required_items)

	return '', 200


# [TASK 3] ====================================================================
# Endpoint that returns a summary of a recipe that corresponds to a query name
@app.route('/summary', methods=['GET'])
def summary():
	recipe_name = request.args.get('name')
	if recipe_name not in cookbook:
		return 'Recipe not found', 400

	entry = cookbook[recipe_name]
	if not isinstance(entry, Recipe):
		return 'Not a recipe', 400

	def sum_recipe(name: str, base_ingredients: Dict[str, int]) -> int:
		if name not in cookbook:
			return -1
		
		item = cookbook[name]
		if isinstance(item, Ingredient):
			base_ingredients[name] = base_ingredients.get(name, 0) + 1
			return item.cook_time

		total_cook_time = 0
		if isinstance(item, Recipe):
			for req_item in item.required_items:
				temp_ingredients: Dict[str, int] = {}
				item_time = sum_recipe(req_item.name, temp_ingredients)
				
				if item_time == -1:
					return -1
					
				total_cook_time += item_time * req_item.quantity
				
				for ing_name, count in temp_ingredients.items():
					base_ingredients[ing_name] = base_ingredients.get(ing_name, 0) + (count * req_item.quantity)

		return total_cook_time

	base_ingredients: Dict[str, int] = {}
	total_cook_time = sum_recipe(recipe_name, base_ingredients)

	if total_cook_time == -1:
		return 'Recipe requires unknown items', 400

	ingredients_list = [{'name': name, 'quantity': quantity} for name, quantity in base_ingredients.items()]

	return jsonify({
		'name': recipe_name,
		'cookTime': total_cook_time,
		'ingredients': ingredients_list
	}), 200


# =============================================================================
# ==== DO NOT TOUCH ===========================================================
# =============================================================================

if __name__ == '__main__':
	app.run(debug=True, port=8080)
