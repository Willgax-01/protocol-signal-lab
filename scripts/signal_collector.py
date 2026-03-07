import subprocess

def run_monitor(script_name):
    print(f"\nRunning: {script_name}")
    print("-" * 40)

    process = subprocess.Popen(
        ["python", f"scripts/{script_name}"],
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
        text=True
    )

    output = ""

    for line in process.stdout:
        print(line, end="")  # show in GitHub Actions log
        output += line

    process.wait()

    with open("reports/latest_report.txt", "w") as f:
        f.write(output)
        f.write("\n")


def main():
    print("Protocol Signal Lab")
    print("Infrastructure Signal Engine")
    print("=" * 40)

    monitors = [
        "github_monitor.py",
        "shelby_network_monitor.py"
    ]

    for monitor in monitors:
        run_monitor(monitor)


if __name__ == "__main__":
    main()
