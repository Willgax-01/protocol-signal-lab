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

def calculate_score(stars, forks, issues, commits24h, total_commits):
    score = 0
    
    score += min(stars / 1000, 20)
    score += min(forks / 500, 20)
    score += min(commits24h * 5, 25)
    score += min(total_commits / 500, 20)
    
    penalty = min(issues / 100, 15)
    
    score = score - penalty
    
    return round(max(score, 0), 2)

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

        stars = repo_data.get("stargazers_count", 0)
        forks = repo_data.get("forks_count", 0)
        issues = repo_data.get("open_issues_count", 0)

        score = calculate_score(stars, forks, issues, commit_24h, total_commits)

        print("\n" + "-" * 50)
        print(f"Repository: {repo}")
        print(f"Stars: {stars}")
        print(f"Forks: {forks}")
        print(f"Open Issues: {issues}")
        print(f"Commits (24h): {commit_24h}")
        print(f"Total Commits: {total_commits}")
        print(f"Signal Score: {score} / 100")

    except Exception:
        print(f"\nCould not fetch data for {repo}")
