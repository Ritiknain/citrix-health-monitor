------------------------------
Citrix Health Monitoring Tool
------------------------------
This project is a Python-based script that simulates daily Citrix health checks.
It reflects basic monitoring tasks performed by a Citrix administrator, such as checking user sessions, VDA status, and license usage.

The script uses simulated data so it can be run locally without access to a real Citrix environment.

--------------------------------------------------
WHAT THIS TOOL DOES
--------------------------------------------------
- Displays active and disconnected user sessions
- Checks VDA registration and power state
- Shows Citrix license usage
- Prints a health summary in the terminal
- Generates a CSV health report

--------------------------------------------------
PROJECT STRUCTURE
--------------------------------------------------

Before running the script:

```text
citrix-health-monitor/
|-- citrix_health.py        (Main script for health checks)
|-- sample_data.py          (Simulated Citrix data - demo only)
|-- README.md
|-- reports/

After running the script:

citrix-health-monitor/
|-- citrix_health.py
|-- sample_data.py
|-- README.md
|-- reports/
    |-- citrix_health_report.csv
```
The CSV file is generated automatically when the script is executed.

--------------------------------------------------
HOW TO RUN
--------------------------------------------------
Requirement:
- Python 3.9 or higher

Run command:
python citrix_health.py

--------------------------------------------------
SAMPLE OUTPUT
--------------------------------------------------

CITRIX HEALTH CHECK REPORT
```
Active sessions        : 2
Disconnected sessions  : 1
Unregistered VDAs      : 1
License usage          : 47 / 100
```
--------------------------------------------------
ABOUT THE SAMPLE DATA
--------------------------------------------------
The sample_data.py file contains simulated Citrix data only.

- No real users
- No real machines or domains
- No real license information

--------------------------------------------------
NOTES
--------------------------------------------------
- The repository contains only source code.
- The CSV report is generated output and not a static file.
- In production, data would be pulled from Citrix PowerShell SDK or APIs.

--------------------------------------------------
AUTHOR
--------------------------------------------------
Ritik Nain

