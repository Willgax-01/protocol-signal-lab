import subprocess

def run_monitor(script_name):
    print(f"\nRunning: {script_name}")
    print("-" * 40)

    result = subprocess.run(
        ["python", f"scripts/{script_name}"],
        capture_output=True,
        text=True
    )

    output = result.stdout

    # Print output to GitHub Actions log
    print(output)

    # Save output to report file
    with open("reports/latest_report.txt", "a") as f:
        f.write(output)
        f.write("\n")


def main():
    print("Protocol Signal Lab")
    print("Infrastructure Signal Engine")
    print("=" * 40)

    monitors = [
        "github_monitor.py"
    ]

    for monitor in monitors:
        run_monitor(monitor)


if __name__ == "__main__":
    main()
