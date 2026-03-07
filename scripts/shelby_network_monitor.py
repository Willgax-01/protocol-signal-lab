import requests
from datetime import datetime

print("Shelby Ecosystem Monitor")
print(f"Timestamp: {datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S UTC')}")
print("=" * 40)

score = 0

# ---------------------------------------------------
# Infrastructure Checks
# ---------------------------------------------------

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

    except Exception:
        print(f"{name}: unreachable")

print("-" * 40)

# ---------------------------------------------------
# Shelby GitHub Ecosystem Discovery
# ---------------------------------------------------

print("Shelby GitHub Ecosystem")

org_url = "https://api.github.com/orgs/shelby/repos"

try:
    r = requests.get(org_url, timeout=10)
    repos = r.json()

    if isinstance(repos, list):

        print(f"Total Shelby Repositories: {len(repos)}")
        print()

        # Show top 5 repos only to keep output clean
        for repo in repos[:5]:

            name = repo.get("name")
            stars = repo.get("stargazers_count", 0)

            print(f"Repo: shelby/{name}")
            print(f"Stars: {stars}")

            if stars > 0:
                score += 10

            print()

    else:
        print("Could not fetch Shelby repositories")

except Exception:
    print("GitHub API error while fetching Shelby repos")

print("-" * 40)

# ---------------------------------------------------
# Ecosystem Health Score
# ---------------------------------------------------

if score > 100:
    score = 100

print(f"Shelby Ecosystem Health Score: {score} / 100")
