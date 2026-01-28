# Simulated Citrix environment data

sessions = [
    {"UserName": "jsmith", "MachineName": "VDA-01", "SessionState": "Active"},
    {"UserName": "rpatel", "MachineName": "VDA-02", "SessionState": "Disconnected"},
    {"UserName": "akumar", "MachineName": "VDA-03", "SessionState": "Active"}
]

vdas = [
    {"MachineName": "VDA-01", "RegistrationState": "Registered", "PowerState": "On"},
    {"MachineName": "VDA-02", "RegistrationState": "Registered", "PowerState": "On"},
    {"MachineName": "VDA-03", "RegistrationState": "Unregistered", "PowerState": "Off"}
]

licenses = [
    {"Product": "Citrix Virtual Apps", "InUse": 47, "Total": 100}
]
