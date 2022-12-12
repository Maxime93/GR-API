from apiflask import APIFlask, Schema, abort
from apiflask.fields import Integer, String, List, Nested
from apiflask.validators import Length, OneOf

import json
from sqlalchemy import create_engine

app = APIFlask(__name__)

db_path = "sqlite:///db/database.db"
engine = create_engine(db_path, echo=False)

# <TODO> Private, function, only callable by this package.
def execute_query(query):
    with engine.begin() as con:
        return con.execute(query).fetchall()

def get_min_product(product):
    return {'id': product['id'], 'name': product['name'], 'sellin': product['sellin'], 'quality': product['quality'], 'price': product['price']}

@app.get('/categories')
def get_categories():
    data = execute_query("SELECT * FROM category")
    if not data:
        return {'message': "no categories were found"}
    return json.dumps([(dict(row.items())) for row in data])

# Get all the products from one category that were not purchased
@app.get('/products/<int:category_id>')
def get_products(category_id):
    query = f"SELECT id, name, sellin, quality, price FROM product WHERE category_id={category_id} AND purchased=0"
    data = execute_query(query)
    if not data:
        return {'message': f"product id `{category_id}` was not found"}
    return json.dumps([(dict(row.items())) for row in data])

# Get product
@app.get('/product/<int:product_id>')
def get_product(product_id):
    query = f"SELECT id, name, sellin, quality, price, purchased FROM product WHERE id={product_id}"
    data = execute_query(query)
    if not data:
        return {'message': f"product id `{product_id}` was not found"}
    return json.dumps([(dict(row.items())) for row in data])

# Get product bundle (more details)
@app.get('/product_bundle/<int:product_id>')
def get_product_bundle(product_id):
    query = f"SELECT * FROM product WHERE id={product_id}"
    data = execute_query(query)
    if not data:
        return {'message': f"product id `{product_id}` was not found"}
    return json.dumps([(dict(row.items())) for row in data])


# Do a very simple, non optimized search
@app.get('/search/<string:search_string>')
def search(search_string):
    result = []

    query = f"SELECT * FROM product where name like '%{search_string}%'"
    data = execute_query(query)
    if not data:
        return {'message': f"no results found for search `{search_string}` was not found"}
    return json.dumps([(dict(row.items())) for row in data])

# Get an account
@app.get('/account/<int:account_id>')
def get_account(account_id):
    query = f"SELECT * FROM account WHERE id={account_id}"
    data = execute_query(query)
    if not data:
        return {'message': f"account id `{account_id}` was not found"}
    return json.dumps([(dict(row.items())) for row in data])

# Login gets an email and returns an account id
@app.get('/login/<string:mail>')
def login(mail):
    query = f"SELECT id FROM account WHERE mail='{mail}'"
    data = execute_query(query)
    if not data:
        return {'message': f"account with email `{mail}` was not found"}
    return json.dumps([(dict(row.items())) for row in data])

# Get cart for an account
@app.get('/cart/<int:account_id>')
def get_cart(account_id):
    query = f"""
    SELECT product.name, product.sellin, product.quality, product.price, account.mail
    FROM cart
    LEFT JOIN product ON cart.product_id = product.id LEFT JOIN account ON cart.account_id = account.id 
    WHERE cart.account_id={account_id}
    AND cart.purchased=0
    AND product.purchased=0
    """
    # query = f"SELECT * FROM cart WHERE account_id='{account_id}'"
    data = execute_query(query)
    if not data:
        return {'message': f"cart for account `{account_id}` is empty"}
    return json.dumps([(dict(row.items())) for row in data])

# COMMENTS FOR LATER

# class CategoryIn(Schema):
#     name = String(required=True, validate=Length(0, 10))
#     category = String(required=True, validate=OneOf(['dog', 'cat']))

# class MinProductOut(Schema):
#     id = Integer()
#     name = String()
#     category = String()

# class FullProductOut(Schema):
#     id = Integer()
#     name = String()
#     category = String()

# class CategoryOut(Schema):
#     id = Integer()
#     name = String()

# class CategoriesOut(Schema):
#     l = List(Nested(CategoryOut))

# @app.get('/categories')
# @app.output(CategoriesOut)
# def get_categories():
#     return categories


# @app.get('/pets/<int:pet_id>')
# @app.output(PetOut)
# def get_pet(pet_id):
#     if pet_id > len(pets) - 1:
#         abort(404)
#     # you can also return an ORM/ODM model class instance directly
#     # APIFlask will serialize the object into JSON format
#     return pets[pet_id]


# @app.patch('/pets/<int:pet_id>')
# @app.input(PetIn(partial=True))
# @app.output(PetOut)
# def update_pet(pet_id, data):
#     # the validated and parsed input data will
#     # be injected into the view function as a dict
#     if pet_id > len(pets) - 1:
#         abort(404)
#     for attr, value in data.items():
#         pets[pet_id][attr] = value
#     return pets[pet_id]
