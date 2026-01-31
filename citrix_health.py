from sample_data import sessions, vdas, licenses
import csv


def print_header():
    print("\n==============================")
    print("  CITRIX HEALTH CHECK REPORT  ")
    print("==============================\n")


def analyze_sessions(sessions):
    active = 0
    disconnected = 0

    print("🔹 SESSION DETAILS")
    for s in sessions:
        print(
            f"User: {s['UserName']:<8} | "
            f"Machine: {s['MachineName']:<6} | "
            f"State: {s['SessionState']}"
        )
        if s["SessionState"] == "Active":
            active += 1
        else:
            disconnected += 1

    return active, disconnected


def analyze_vdas(vdas):
    print("\n🔹 VDA STATUS")
    unregistered = []

    for v in vdas:
        print(
            f"{v['MachineName']} | "
            f"Registered: {v['RegistrationState']} | "
            f"Power: {v['PowerState']}"
        )
        if v["RegistrationState"] != "Registered":
            unregistered.append(v["MachineName"])

    return unregistered


def analyze_licenses(licenses):
    print("\n🔹 LICENSE USAGE")
    for l in licenses:
        usage_percent = (l["InUse"] / l["Total"]) * 100
        print(
            f"{l['Product']} → {l['InUse']} / "
            f"{l['Total']} ({usage_percent:.1f}%)"
        )


def export_csv(sessions, vdas):
    filename = "reports/citrix_health_report.csv"

    with open(filename, "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["Category", "Name", "Status"])

        for v in vdas:
            writer.writerow(
                ["VDA", v["MachineName"], v["RegistrationState"]]
            )

        for s in sessions:
            writer.writerow(
                ["Session", s["UserName"], s["SessionState"]]
            )

    print(f"\n✅ CSV report generated: {filename}\n")


def main():
    print_header()

    active, disconnected = analyze_sessions(sessions)
    unregistered_vdas = analyze_vdas(vdas)
    analyze_licenses(licenses)

    print("\n🔹 HEALTH SUMMARY")
    print(f"Active Sessions      : {active}")
    print(f"Disconnected Sessions: {disconnected}")
    print(f"Unregistered VDAs    : {len(unregistered_vdas)}")

    if unregistered_vdas:
        print("⚠️  Attention Needed: Unregistered VDAs detected")

    export_csv(sessions, vdas)


if __name__ == "__main__":
    main()
