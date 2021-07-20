#!/bin/bash

curl "http://localhost:8000/prompt/${ID}/" \
  --include \
  --request PATCH \
  --header "Content-Type: application/json" \
  --header "Authorization: Token ${TOKEN}" \
  --data '{
    "prompt": {
      "content": "'"${CONTENT}"'"
    }
  }'

echo
