import requests

# Simple GitHub signal monitor

REPOSITORIES = [
    "Layr-Labs/eigenlayer-contracts",
    "celestiaorg/celestia-node",
    "base-org/node"
]

def check_repo(repo):
    url = f"https://api.github.com/repos/{repo}"
   headers = {"Accept": "application/vnd.github+json"}
response = requests.get(url, headers=headers)

    if response.status_code != 200:
        print(f"Could not fetch data for {repo}")
        return

    data = response.json()

    print("\nRepository:", repo)
    print("Stars:", data["stargazers_count"])
    print("Forks:", data["forks_count"])
    print("Open Issues:", data["open_issues_count"])

def main():
    print("Protocol Signal Lab")
    print("GitHub Infrastructure Monitor")
    print("-" * 40)

    for repo in REPOSITORIES:
        check_repo(repo)

if __name__ == "__main__":
    main()
