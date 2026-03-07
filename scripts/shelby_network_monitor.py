import requests
from datetime import datetime

print("Shelby Network Monitor")
print(f"Timestamp: {datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S UTC')}")
print("=" * 40)

explorer_url = "https://explorer.shelby.xyz/shelbynet"

try:
    response = requests.get(explorer_url, timeout=10)

    if response.status_code == 200:
        print("Shelby Explorer: reachable")
        print("Network Status: Active")
    else:
        print("Shelby Explorer: reachable but unexpected response")
        print("Network Status: Unknown")

except Exception as e:
    print("Shelby Explorer: unreachable")
    print("Network Status: Down")
