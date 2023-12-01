from flask import Blueprint, request

from .data.search_data import USERS

bp = Blueprint("search", __name__, url_prefix="/search")

@bp.route("")
def search():
    return search_users(request.args.to_dict()), 200

def search_users(args):
    """Search users database

    Parameters:
        args: a dictionary containing the following search parameters:
            id: string
            name: string
            age: string
            occupation: string

    Returns:
        a list of users that match the search parameters
    """
    search_results = set()  # Use a set to avoid duplicates

    # Include user with the specified ID
    if 'id' in args:
        user_with_id = next((user for user in USERS if user['id'] == args['id']), None)
        if user_with_id:
            search_results.add(user_with_id)

    # Partially match and case-insensitive search for name
    if 'name' in args:
        search_results.update(user for user in USERS if args['name'].lower() in user['name'].lower())

    # Range search for age
    if 'age' in args:
        try:
            age = int(args['age'])
            search_results.update(user for user in USERS if user['age'] in range(age - 1, age + 2))
        except ValueError:
            pass  # Ignore invalid age values

    # Partially match and case-insensitive search for occupation
    if 'occupation' in args:
        search_results.update(user for user in USERS if args['occupation'].lower() in user['occupation'].lower())

    return list(search_results)

# Example user data for testing
USERS = [
    {"id": "1", "name": "John Doe", "age": 30, "occupation": "Engineer"},
    {"id": "2", "name": "Jane Doe", "age": 28, "occupation": "Doctor"},
    {"id": "3", "name": "Joe Doe", "age": 25, "occupation": "Teacher"}
]
