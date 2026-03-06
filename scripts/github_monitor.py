import requests
from datetime import datetime

repos = [
    "celestiaorg/celestia-node",
    "base-org/node",
    "Layr-Labs/eigenlayer-contracts"
]

print("Protocol Signal Lab")
print("GitHub Infrastructure Monitor")
print("Timestamp:", datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S UTC")
print("=" * 50)

for repo in repos:
    url = f"https://api.github.com/repos/{repo}"

    try:
        response = requests.get(
            url,
            timeout=10,
            headers={
                "Accept": "application/vnd.github+json"
            }
        )

        data = response.json()

        print("\n" + "-" * 50)
        print(f"Repository: {repo}")
        print(f"Stars: {data['stargazers_count']}")
        print(f"Forks: {data['forks_count']}")
        print(f"Open Issues: {data['open_issues_count']}")

    except Exception:
        print(f"\nCould not fetch data for {repo}")
