import requests
from datetime import datetime, timedelta

repos = [
    "celestiaorg/celestia-node",
    "base-org/node",
    "Layr-Labs/eigenlayer-contracts"
]

print("Protocol Signal Lab")
print("GitHub Infrastructure Monitor")
print("Timestamp:", datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S UTC"))
print("=" * 50)

since = (datetime.utcnow() - timedelta(days=1)).isoformat() + "Z"

for repo in repos:

    repo_url = f"https://api.github.com/repos/{repo}"
    commit_url = f"https://api.github.com/repos/{repo}/commits?since={since}"
    contributors_url = f"https://api.github.com/repos/{repo}/contributors?per_page=100"

    try:
        repo_data = requests.get(repo_url).json()
        commits = requests.get(commit_url).json()
        contributors = requests.get(contributors_url).json()

        commit_24h = len(commits) if isinstance(commits, list) else 0

        total_commits = 0
        if isinstance(contributors, list):
            total_commits = sum(c.get("contributions", 0) for c in contributors)

        print("\n" + "-" * 50)
        print(f"Repository: {repo}")
        print(f"Stars: {repo_data.get('stargazers_count', 0)}")
        print(f"Forks: {repo_data.get('forks_count', 0)}")
        print(f"Open Issues: {repo_data.get('open_issues_count', 0)}")
        print(f"Commits (24h): {commit_24h}")
        print(f"Total Commits: {total_commits}")

    except Exception:
        print(f"\nCould not fetch data for {repo}")
