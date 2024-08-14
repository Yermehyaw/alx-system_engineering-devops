#!/usr/bin/python3
"""
Generate/Refresh access token
"""
import requests


base_url = 'https://www.reddit.com/'
data = {'grant_type': 'password', 'username': 'Yermehyaw', 'password': 'Iye@omo1234'}
auth = requests.auth.HTTPBasicAuth('I_M-_KZ9Lnm_eSkmbag_GQ', 'B7uPvJvBFzZmKp_7excUK8XWOTlUpA')
r = requests.post(
            base_url + 'api/v1/access_token',
            data=data,
            headers={'user-agent': 'Ubuntu:I_M-_KZ9Lnm_eSkmbag_GQ:v1.0(by /u/Yermehyaw)'},
		    auth=auth
    )

r_json = r.json()
return r_json['access_token']
