import requests
import json

token = 'OIYRtEtUB9pNTTvfgFaZ'
url = "https://api-sandbox.sebgroup.com/ais/v7/identified2/accounts/5a59028c-e757-4f22-b88c-3ba90573383c/transactions?bookingStatus=booked"

headers = {
  'Accept': 'application/json',
  'X-Request-ID': 'F3cslD9NcG5IDK6DKexzUysqbwEyVZ90',
  'PSU-IP-Address': '127.0.0.1',
  'withBalance': 'false',
  'Authorization': 'Bearer ' + token,
  'Cookie': 'C0WNET=5a9f8b9f-60eb-4a23-a208-fac04354f4a0; AMWEBJCT!%2Fmga!JSESSIONID=0000zYagw71Rbp_o_FXWsx_Sduj:938ed943-3c20-4801-ace0-52dd1dd31f86; PD-SESSION-ID=1_4_1_1EGeO0hIiW2ohF3QYHv75ae7LFczR48So36HnHkZC6p2I7kc; PGNET=43a28955-60ef-44e2-a63e-f3fc6af39838; TS01136fc4=0107224bed70f812756a17a506c3df84499c7d7de52d60e36c959b9eff82eb6dbfd09c04095bf39c965e9a19f14991488dd48c6cd6; TS018787d1=0107224bed389992e29a09ef281a55f610fa11e27e69780e5ecaadca06990b5940915c27ab7a82555e9b35f0530d94d00dc33feea0'
}

response = requests.request("GET", url, headers=headers).json()

print(json.dumps(response, indent=3, separators=(',', ':'), sort_keys=True))