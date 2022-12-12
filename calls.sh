
curl -X 'post' \
  'http://127.0.0.1:5000/add_product' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
  "name": "myproduct", "sellin":2, "quality":4, "description":"bla", "photo":"photo", "price":12.44, "category_id":1
}'

curl http://127.0.0.1:5000/cart/2

curl http://127.0.0.1:5000/products/2

curl http://127.0.0.1:5000/products/5