import subprocess
import os


def run_monitor(script_name):
    print(f"\nRunning: {script_name}")
    print("-" * 40)

    result = subprocess.run(
        ["python", f"scripts/{script_name}"],
        capture_output=True,
        text=True
    )

    output = result.stdout

    print(output)

    # save output to report file
    with open("reports/latest_report.txt", "a") as f:
        f.write(f"\n===== {script_name} =====\n")
        f.write(output)


def main():
    print("Protocol Signal Lab")
    print("Infrastructure Signal Engine")
    print("=" * 40)

    # ensure reports folder exists
    os.makedirs("reports", exist_ok=True)

    # reset report file every run
    open("reports/latest_report.txt", "w").close()

    monitors = [
        "github_monitor.py"
    ]

    for monitor in monitors:
        run_monitor(monitor)


if __name__ == "__main__":
    main()
