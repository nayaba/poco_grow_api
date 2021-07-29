#!/bin/bash

curl "http://localhost:8000/prompt/" \
  --include \
  --request POST \
  --header "Content-Type: application/json" \
  --header "Authorization: Token ${TOKEN}" \
  --data '{
    "prompt": {
      "content": "'"${CONTENT}"'"
    }
  }'

echo
