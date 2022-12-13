# Get categories
curl http://127.0.0.1:5000/categories
# [{"id": 1, "name": "STANDARD"}, {"id": 2, "name": "BRIE"}, {"id": 3, "name": "SULFURAS"}, {"id": 4, "name": "CONJURED"}]

# Get products in a category
curl http://127.0.0.1:5000/products/1
# [{"id": 7, "name": "myproduct", "sellin": 2, "quality": 4, "price": 12.44}, {"id": 8, "name": "massproduct", "sellin": 2, "quality": 4, "price": 12.44}, {"id": 9, "name": "massproduct", "sellin": 2, "quality": 4, "price": 12.44}, {"id": 10, "name": "massproduct", "sellin": 2, "quality": 4, "price": 12.44}, {"id": 11, "name": "massproduct", "sellin": 2, "quality": 4, "price": 12.44}, {"id": 12, "name": "massproduct", "sellin": 2, "quality": 4, "price": 12.44}, {"id": 13, "name": "massproduct", "sellin": 2, "quality": 4, "price": 12.44}, {"id": 14, "name": "massproduct", "sellin": 2, "quality": 4, "price": 12.44}, {"id": 15, "name": "massproduct", "sellin": 2, "quality": 4, "price": 12.44}, {"id": 16, "name": "massproduct", "sellin": 2, "quality": 4, "price": 12.44}, {"id": 17, "name": "massproduct", "sellin": 2, "quality": 4, "price": 12.44}, {"id": 18, "name": "massproduct", "sellin": 2, "quality": 4, "price": 12.44}]

# Get a specific product
curl http://127.0.0.1:5000/product/2
# [{"id": 2, "name": "product2", "sellin": 9, "quality": 9, "price": 23.99, "purchased": 1}]

# Get product bundle
curl http://127.0.0.1:5000/product_bundle/2
# [{"id": 2, "name": "product2", "sellin": 9, "quality": 9, "description": "desc2", "photo": "www.photo.com", "price": 23.99, "category_id": 2, "purchased": 1}]

# Search
curl http://127.0.0.1:5000/search/pro
# [{"id": 1, "name": "product1", "sellin": 9, "quality": 9, "description": "desc1", "photo": "www.photo.com", "price": 13.99, "category_id": 1, "purchased": 1}, {"id": 2, "name": "product2", "sellin": 9, "quality": 9, "description": "desc2", "photo": "www.photo.com", "price": 23.99, "category_id": 2, "purchased": 1}, {"id": 3, "name": "product3", "sellin": 9, "quality": 9, "description": "desc3", "photo": "www.photo.com", "price": 33.99, "category_id": 3, "purchased": 1}, {"id": 4, "name": "product4", "sellin": 9, "quality": 9, "description": "desc4", "photo": "www.photo.com", "price": 43.99, "category_id": 4, "purchased": 0}, {"id": 5, "name": "product5", "sellin": 9, "quality": 9, "description": "desc5", "photo": "www.photo.com", "price": 33.99, "category_id": 3, "purchased": 0}, {"id": 6, "name": "product6", "sellin": 9, "quality": 9, "description": "desc6", "photo": "www.photo.com", "price": 53.99, "category_id": 1, "purchased": 1}, {"id": 7, "name": "myproduct", "sellin": 2, "quality": 4, "description": "bla", "photo": "photo", "price": 12.44, "category_id": 1, "purchased": 0}, {"id": 8, "name": "massproduct", "sellin": 2, "quality": 4, "description": "bla", "photo": "photo", "price": 12.44, "category_id": 1, "purchased": 0}, {"id": 9, "name": "massproduct", "sellin": 2, "quality": 4, "description": "bla", "photo": "photo", "price": 12.44, "category_id": 1, "purchased": 0}, {"id": 10, "name": "massproduct", "sellin": 2, "quality": 4, "description": "bla", "photo": "photo", "price": 12.44, "category_id": 1, "purchased": 0}, {"id": 11, "name": "massproduct", "sellin": 2, "quality": 4, "description": "bla", "photo": "photo", "price": 12.44, "category_id": 1, "purchased": 0}, {"id": 12, "name": "massproduct", "sellin": 2, "quality": 4, "description": "bla", "photo": "photo", "price": 12.44, "category_id": 1, "purchased": 0}, {"id": 13, "name": "massproduct", "sellin": 2, "quality": 4, "description": "bla", "photo": "photo", "price": 12.44, "category_id": 1, "purchased": 0}, {"id": 14, "name": "massproduct", "sellin": 2, "quality": 4, "description": "bla", "photo": "photo", "price": 12.44, "category_id": 1, "purchased": 0}, {"id": 15, "name": "massproduct", "sellin": 2, "quality": 4, "description": "bla", "photo": "photo", "price": 12.44, "category_id": 1, "purchased": 0}, {"id": 16, "name": "massproduct", "sellin": 2, "quality": 4, "description": "bla", "photo": "photo", "price": 12.44, "category_id": 1, "purchased": 0}, {"id": 17, "name": "massproduct", "sellin": 2, "quality": 4, "description": "bla", "photo": "photo", "price": 12.44, "category_id": 1, "purchased": 0}, {"id": 18, "name": "massproduct", "sellin": 2, "quality": 4, "description": "bla", "photo": "photo", "price": 12.44, "category_id": 1, "purchased": 0}]

# Get an account
curl http://127.0.0.1:5000/account/1
# [{"id": 1, "mail": "user1@mail.com"}]%

# Create an account
curl -X 'post' \
  'http://127.0.0.1:5000/create_account' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
  "mail": "user6@mail.com"
}'
# {"message":"success"}

# Login
curl http://127.0.0.1:5000/login/user6@mail.com
# [{"id": 5}]%

# Add to cart
curl -X 'post' \
  'http://127.0.0.1:5000/add_to_cart/5' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
  "product_id":17
}'
# {"message":"success"}

# Purchase
curl -X 'post' \
  'http://127.0.0.1:5000/purchase/5' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json'
# {"message":"success"}

curl http://127.0.0.1:5000/cart/4
# [{"cart_id": 4, "product_id": 4, "name": "product4", "sellin": 9, "quality": 9, "price": 43.99, "mail": "user4@mail.com"}]%

curl -X 'post' \
  'http://127.0.0.1:5000/add_product' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
  "name": "my new little product", "sellin":2, "quality":4, "description":"bla", "photo":"photo", "price":9.99, "category_id":2, "qty":10
}'
# {"message":"success"}
