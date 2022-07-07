import requests

print ("Hello World")
print ("testing CI/CD BNI")

response = requests.get("https://www.google.com")

print (response.text)