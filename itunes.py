import requests 
import sys

if len(sys.argv) !=2:
    sys.exit()



response=requests.get("C:\Users\World\OneDrive\Desktop"+sys.argv[1])

print(response.json())