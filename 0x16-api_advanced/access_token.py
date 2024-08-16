#!/usr/bin/python3
"""
Generate/Refresh access token
"""
import requests


base_url = 'https://www.reddit.com/'
data = {'grant_type': 'authorization_code', 'code': 'M8x345PCjK5Kwrji5FNUCLetopH-Ww', 'redirect_uri': 'http://localhost:8080'}
headers = {
    'user-agent': 'Ubuntu:qrMl883hmAyK8IRqBCr99Q:v1.0(by /u/Yermehyaw)',
    'content-type': 'application/x-www-form-urlencoded'
}
auth = requests.auth.HTTPBasicAuth('qrMl883hmAyK8IRqBCr99Q', 'K6A2JsE3qRH9wW_TE3dqxKkOPTp2Xg')
r = requests.post(
    base_url + 'api/v1/access_token',
    data=data,
    headers=headers,
    auth=auth
)

r_json = r.json()
print(r_json)
