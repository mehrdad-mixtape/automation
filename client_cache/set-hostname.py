#!/usr/bin/python3
import requests
import urllib3
import json

ip_address = '192.168.119.100'
username = 'test'
password = 'test'

def get_token():
    """
    Authenticate and get token
    """

    url = 'https://%s:55443/api/v1/auth/token-services' % ip_address
    auth = (username, password) 
    headers = {'Content-Type':'application/json'}
    response = requests.post(url, auth=auth, headers=headers, verify=False)
    json_data = json.loads(response.text)
    token = json_data['token-id']
    print('We received token: %s' % token)
    return token

def set_hostname(token):
    """
    Set Hostname on CSR 1000V router.
    """
    url = 'https://%s:55443/api/v1/global/host-name' % (ip_address)
    headers={ 'Content-Type': 'application/json', 'Accept':'application/json', 'X-auth-token': token}

    payload = {
	"host-name": "Webinar-Netowrk-Automation"
	}

    response = requests.put(url, headers=headers, json=payload, verify=False)
    print('The router responds with status code: %s ' % response.status_code)

# Disable unverified HTTPS request warnings.
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

# Get token.
token = get_token()

#Call Def
set_hostname(token)
