import requests
from datetime import datetime

print("Shelby Ecosystem Monitor")
print(f"Timestamp: {datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S UTC')}")
print("=" * 40)

score = 0

checks = [
    ("Shelby Explorer", "https://explorer.shelby.xyz/shelbynet"),
    ("Shelby Docs", "https://docs.shelby.xyz/"),
    ("Shelby Website", "https://shelby.xyz/")
]

for name, url in checks:
    try:
        r = requests.get(url, timeout=10)
        if r.status_code == 200:
            print(f"{name}: reachable")
            score += 20
        else:
            print(f"{name}: unexpected response")
            score += 10
    except:
        print(f"{name}: unreachable")

print("-" * 40)

# GitHub ecosystem check
repos = [
    "shelby/examples",
    "shelby/feedback"
]

for repo in repos:
    try:
        url = f"https://api.github.com/repos/{repo}"
        r = requests.get(url, timeout=10)
        data = r.json()

        stars = data.get("stargazers_count", 0)

        print(f"Repo: {repo}")
        print(f"Stars: {stars}")

        if stars > 0:
            score += 20

    except:
        print(f"Could not fetch repo: {repo}")

print("-" * 40)
print(f"Shelby Ecosystem Health Score: {score} / 100")
