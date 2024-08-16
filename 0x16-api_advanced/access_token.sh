#!/usr/bin/env bash
# Retrieve reddit api access token
curl -X POST https://www.reddit.com/api/v1/access_token \
     -H 'content-type: application/x-www-form-urlencoded' \
     -A 'api-advanced-script' \
     -u 'qrMl883hmAyK8IRqBCr99Q:K6A2JsE3qRH9wW_TE3dqxKkOPTp2Xg' \
     -d 'grant_type=authorization_code&code=M8x345PCjK5Kwrji5FNUCLetopH-Ww&redirect_uri=http://localhost:8080'
