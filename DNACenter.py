
import requests
import json
from pprint import pprint

user = 'devnetuser'
pw = 'Cisco123!'

def gettoken(): 
    url = "https://sandboxdnac.cisco.com/dna/system/api/v1/auth/token"
    header = {
       'Content-Type' : 'application/json',
       'Accept' : 'application/json'
    }
    response = requests.post(url, auth=(user, pw), headers=header, verify=False)
    json_response = json.loads(response.text)
    return json_response['Token']

def get_site_health():
    url = "https://sandboxdnac.cisco.com/dna/intent/api/v1/site-health"
    token = gettoken()
    header = {
        'X-Auth-Token' : token,
       'Content-Type' : 'application/json',
       'Accept' : 'application/json'
    }
    response = requests.get(url, headers=header, verify=False)
    #json_response = json.loads(response.text)
    return response.text

pprint(get_site_health(), indent=4)


