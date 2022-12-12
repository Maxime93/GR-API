curl http://127.0.0.1:5000/pets/0

curl -X 'PATCH' \
  'http://127.0.0.1:5000/pets/0' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
  "name": "otherCat"
}'