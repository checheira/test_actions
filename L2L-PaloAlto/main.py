import requests
import xml.etree.ElementTree as ET

query = {'type':'keygen', 'user':'rest-api-user', 'password':'Password123'}

response = requests.get('https://palo-lab.local/api', params=query, verify=False)

# Parse the XML string
root = ET.fromstring(response.text)

# Find the key element and get its text
api_key = root.find(".//key").text

print(api_key)