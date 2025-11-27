import json
import requests
api_url = "http://localhost:58000/api/v1/network-device"

headers={"X-Auth-Token": "NC-10-cd4d8320fa6941268742-nbi"}

resp = requests.get(api_url, headers=headers)

print("Request status: ", resp.status_code)

response_json = resp.json()
print()
print()
print (response_json)
print()
print()
networkDevices = response_json["response"]

for networkDevice in networkDevices:
    hostname = networkDevice.get("hostname")
    if hostname:
        print(hostname, "\t", networkDevice.get("platformId"), "\t", networkDevice.get("managementIpAddress"))

