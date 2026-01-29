from sample_data import sessions, vdas, licenses
import csv
from datetime import datetime

print("\n==============================")
print("  CITRIX HEALTH CHECK REPORT  ")
print("==============================\n")

# Sessions
active_sessions = 0
disconnected_sessions = 0

print("🔹 SESSION DETAILS")
for s in sessions:
    print(f"User: {s['UserName']:<8} | Machine: {s['MachineName']:<6} | State: {s['SessionState']}")
    if s["SessionState"] == "Active":
        active_sessions += 1
    else:
        disconnected_sessions += 1

# VDA Health
print("\n🔹 VDA STATUS")
unregistered_vdas = []

for v in vdas:
    print(f"{v['MachineName']} | Registered: {v['RegistrationState']} | Power: {v['PowerState']}")
    if v["RegistrationState"] != "Registered":
        unregistered_vdas.append(v["MachineName"])

# License Usage
print("\n🔹 LICENSE USAGE")
for l in licenses:
    usage_percent = (l["InUse"] / l["Total"]) * 100
    print(f"{l['Product']} → {l['InUse']} / {l['Total']} ({usage_percent:.1f}%)")

# Summary
print("\n🔹 HEALTH SUMMARY")
print(f"Active Sessions      : {active_sessions}")
print(f"Disconnected Sessions: {disconnected_sessions}")
print(f"Unregistered VDAs    : {len(unregistered_vdas)}")

if unregistered_vdas:
    print("⚠️  Attention Needed: Unregistered VDAs detected")

# Export CSV
with open("reports/citrix_health_report.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["Category", "Name", "Status"])

    for v in vdas:
        writer.writerow(["VDA", v["MachineName"], v["RegistrationState"]])

    for s in sessions:
        writer.writerow(["Session", s["UserName"], s["SessionState"]])

print("\n✅ CSV report generated: reports/citrix_health_report.csv\n")
