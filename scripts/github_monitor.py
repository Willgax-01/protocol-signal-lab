import requests

repos = [
    "celestiaorg/celestia-node",
    "base-org/node",
    "eigenlayer/eigenlayer-contracts"
]

print("Protocol Signal Lab")
print("GitHub Infrastructure Monitor")
print("-" * 40)

for repo in repos:
    url = f"https://api.github.com/repos/{repo}"

    try:
        response = requests.get(url)
        data = response.json()

        print(f"\nRepository: {repo}")
        print(f"Stars: {data['stargazers_count']}")
        print(f"Forks: {data['forks_count']}")
        print(f"Open Issues: {data['open_issues_count']}")

    except:
        print(f"Could not fetch data for {repo}")
