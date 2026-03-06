import datetime

# Simple signal collector prototype for Protocol Signal Lab

signals = [
    {
        "source": "Base Ecosystem",
        "type": "Infrastructure",
        "observation": "Stablecoin liquidity expansion discussions"
    },
    {
        "source": "EigenLayer GitHub",
        "type": "Developer Activity",
        "observation": "Increased repository commits and development updates"
    },
    {
        "source": "Governance Forums",
        "type": "Governance",
        "observation": "DeFi risk parameter discussions emerging"
    }
]

def generate_signal_report():
    today = datetime.date.today()

    print("Protocol Signal Lab")
    print("Signal Collection Report")
    print("Date:", today)
    print("-" * 40)

    for i, signal in enumerate(signals, start=1):
        print(f"\nSignal {i}")
        print("Source:", signal["source"])
        print("Type:", signal["type"])
        print("Observation:", signal["observation"])

if __name__ == "__main__":
    generate_signal_report()
