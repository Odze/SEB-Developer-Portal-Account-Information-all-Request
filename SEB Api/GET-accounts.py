import requests
import json

token = 'K6xHn95AHKmZswNVOdCI'
url = "https://api-sandbox.sebgroup.com/ais/v7/identified2/accounts"

headers = {
  'Accept': 'application/json',
  'X-Request-ID': 'F3cslD9NcG5IDK6DKexzUysqbwEyVZ90',
  'PSU-IP-Address': '127.0.0.1',
  'withBalance': 'false',
  'Authorization': 'Bearer '+token,
  'Cookie': 'C0WNET=5a9f8b9f-60eb-4a23-a208-fac04354f4a0; AMWEBJCT!%2Fmga!JSESSIONID=0000zYagw71Rbp_o_FXWsx_Sduj:938ed943-3c20-4801-ace0-52dd1dd31f86; PGNET=43a28955-60ef-44e2-a63e-f3fc6af39838; TS018787d1=0107224bed389992e29a09ef281a55f610fa11e27e69780e5ecaadca06990b5940915c27ab7a82555e9b35f0530d94d00dc33feea0'
}

response = requests.request("GET", url, headers=headers).json()

print(json.dumps(response, indent=3, separators=(',', ':'), sort_keys=True))


