import requests
from datetime import datetime

print("Shelby Network Monitor")
print("Timestamp:", datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S UTC"))
print("=" * 50)

url = "https://explorer.shelby.xyz/shelbynet"

try:
    response = requests.get(url, timeout=10)

    if response.status_code == 200:
        print("Shelby Explorer reachable")
        print("Network Status: Active")
    else:
        print("Shelby Explorer responded but status unclear")

except Exception:
    print("Could not reach Shelby network explorer")
