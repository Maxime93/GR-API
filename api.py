from apiflask import APIFlask, Schema, abort
from apiflask.fields import Integer, String, List, Nested
from apiflask.validators import Length, OneOf
from flask import request

import json
from sqlalchemy import create_engine

app = APIFlask(__name__)

db_path = "sqlite:///db/database.db"
engine = create_engine(db_path, echo=False)

# <TODO> Private, function, only callable by this package.
def execute_query(query):
    with engine.begin() as con:
        return con.execute(query).fetchall()

def insert_query(query):
    with engine.begin() as con:
        return con.execute(query)

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

# Purchase available items in cart for an account
@app.post('/purchase/<int:account_id>')
def purchase(account_id):
    cart_data = json.loads(get_cart(account_id))

    if not cart_data:
        return {"message": "nothing in cart for account `{account_id}`"}

    for product in cart_data:
        # Update the cart table
        query = f"UPDATE cart SET purchased = 1 WHERE id={product['cart_id']}"
        insert_query(query)
        # Update the product table
        query = f"UPDATE product SET purchased = 1 WHERE id={product['product_id']}"
        insert_query(query)

    return {"message": "success"}

# Get cart for an account
@app.get('/cart/<int:account_id>')
def get_cart(account_id):
    query = f"""
    SELECT cart.id as cart_id, product.id as product_id, product.name, product.sellin, product.quality, product.price, account.mail
    FROM cart
    LEFT JOIN product ON cart.product_id = product.id LEFT JOIN account ON cart.account_id = account.id 
    WHERE cart.account_id={account_id}
    AND cart.purchased=0
    AND product.purchased=0
    """
    data = execute_query(query)
    if not data:
        return {'message': f"cart for account `{account_id}` is empty"}
    return json.dumps([(dict(row.items())) for row in data])

# Add product(s) to the inventory
@app.post('/add_product')
def add_product():
    data = request.get_json()
    columns = ['name', 'sellin', 'quality', 'description', 'photo', 'price', 'category_id']
    for col in columns:
        if data.get(col) is None:
            return {'message': f'cannot add product, missing {col} information'}

    query = f"""
    INSERT INTO product (name, sellin, quality, description, photo, price, category_id)
    VALUES ('{data["name"]}', '{data["sellin"]}', '{data["quality"]}', '{data["description"]}', '{data["photo"]}', '{data["price"]}', '{data["category_id"]}');
    """

    qty = data.get('qty')
    if qty is not None:
        for i in range(qty):
            insert_query(query)
    else:
        insert_query(query)

    insert_query(query)
    return {'message': 'success'}
