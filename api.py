from apiflask import APIFlask, Schema, abort
from apiflask.fields import Integer, String, List, Nested
from apiflask.validators import Length, OneOf

categories = [
    {'id': 0, 'name': 'STANDARD'},
    {'id': 1, 'name': 'BRIE'},
    {'id': 2, 'name': 'SULFURAS'},
    {'id': 3, 'name': 'CONJURED'}
]

products = [
    {'id':0, 'name':'product1', 'sellin': 9, 'quality':12, 'description':'description1', 'photo':'www.photo.com', 'price': 13.99, 'category_id': 0},
    {'id':1, 'name':'product2', 'sellin': 9, 'quality':12, 'description':'description2', 'photo':'www.photo.com', 'price': 23.99, 'category_id': 0},
    {'id':2, 'name':'product3', 'sellin': 9, 'quality':12, 'description':'description3', 'photo':'www.photo.com', 'price': 43.99, 'category_id': 1},
    {'id':3, 'name':'product4', 'sellin': 9, 'quality':12, 'description':'description4', 'photo':'www.photo.com', 'price': 53.99, 'category_id': 2}
]

app = APIFlask(__name__)

def get_min_product(product):
    return {'id': product['id'], 'name': product['name'], 'sellin': product['sellin'], 'quality': product['quality'], 'price': product['price']}

@app.get('/categories')
def get_categories():
    return categories

# Get all the products from one category
@app.get('/products/<int:category_id>')
def get_products(category_id):
    result = []
    for product in products:
        if product['category_id'] == category_id:
            result.append(get_min_product(product))
    if not result:
        result = {'message': f"product id `{id}` was not found"}
    return result

# Get product
@app.get('/product/<int:product_id>')
def get_product(id):
    p = {'message': f"product id `{id}` was not found"}
    for product in products:
        if product['id'] == id:
            return get_min_product(product)
    return p

# Get product bundle (more details)
@app.get('/product_bundle/<int:product_id>')
def get_product_bundle(id):
    p = {'message': f"product id `{id}` was not found"}
    for product in products:
        if product['id'] == id:
            return product
    return p


# Do a very simple, non optimized search
@app.get('/search/<string:search_string>')
def search(search_string):
    result = []
    for product in products:
        if search_string in product['name']:
            result.append(product)
    if not result:
        result = {'message': f"your search `{search_string}` did not yield any results"}
    return result


# get_categories() -> []string
# get_products(pagination, category, sort: {sortBy: "sellIn" | "quality", order: "asc" | "desc")}) -> []min_products
# get_product(id) -> min_product ({name, sellin, quality}) // min_product == compact ver.
# get_product_bundle(id) -> product
# search(string) -> []min_product

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
