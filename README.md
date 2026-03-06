# Protocol Signal Lab

Protocol Signal Lab is a small automated tool that monitors key crypto infrastructure repositories and generates simple activity signals.

The system runs automatically using GitHub Actions and collects development metrics from selected protocol repositories.

## What it tracks

For each monitored repository the tool collects:

* Stars
* Forks
* Open Issues
* Commits in the last 24 hours
* Total commits
* Signal Score (0–100)

These metrics help provide a quick overview of repository popularity, development activity, and maintenance pressure.

## How it works

GitHub Actions runs the signal collection workflow automatically.

Pipeline:

GitHub Actions
→ signal_collector.py
→ github_monitor.py
→ GitHub API
→ Report generation

The system fetches repository data from the GitHub API, calculates a signal score, ranks the repositories, and generates a report.

## Example output

Repository: base-org/node
Stars: 68708
Forks: 3215
Open Issues: 15
Commits (24h): 1
Total Commits: 188
Signal Score: 31.66 / 100

## Project Structure

```
protocol-signal-lab
│
├ .github/workflows
│   └ signal.yml
│
├ scripts
│   ├ signal_collector.py
│   └ github_monitor.py
│
├ reports
│   └ latest_report.txt
│
└ requirements.txt
```

## Goal

The goal of this project is to provide a lightweight infrastructure signal engine for monitoring development activity in important blockchain protocol repositories.
