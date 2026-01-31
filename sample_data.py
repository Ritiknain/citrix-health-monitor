# Simulated Citrix environment data (enterprise-scale dummy dataset)

# -----------------------------
# User Sessions
# -----------------------------
sessions = [
    {"UserName": "user01", "MachineName": "VDA-01", "SessionState": "Active"},
    {"UserName": "user02", "MachineName": "VDA-02", "SessionState": "Disconnected"},
    {"UserName": "user03", "MachineName": "VDA-03", "SessionState": "Active"},
    {"UserName": "user04", "MachineName": "VDA-04", "SessionState": "Active"},
    {"UserName": "user05", "MachineName": "VDA-05", "SessionState": "Disconnected"},
    {"UserName": "user06", "MachineName": "VDA-06", "SessionState": "Active"},
    {"UserName": "user07", "MachineName": "VDA-07", "SessionState": "Active"},
    {"UserName": "user08", "MachineName": "VDA-08", "SessionState": "Disconnected"},
    {"UserName": "user09", "MachineName": "VDA-09", "SessionState": "Active"},
    {"UserName": "user10", "MachineName": "VDA-10", "SessionState": "Active"},
    {"UserName": "user11", "MachineName": "VDA-11", "SessionState": "Disconnected"},
    {"UserName": "user12", "MachineName": "VDA-12", "SessionState": "Active"},
    {"UserName": "user13", "MachineName": "VDA-13", "SessionState": "Active"},
    {"UserName": "user14", "MachineName": "VDA-14", "SessionState": "Disconnected"},
    {"UserName": "user15", "MachineName": "VDA-15", "SessionState": "Active"},
    {"UserName": "user16", "MachineName": "VDA-03", "SessionState": "Active"},
    {"UserName": "user17", "MachineName": "VDA-06", "SessionState": "Disconnected"},
    {"UserName": "user18", "MachineName": "VDA-09", "SessionState": "Active"},
    {"UserName": "user19", "MachineName": "VDA-10", "SessionState": "Active"},
    {"UserName": "user20", "MachineName": "VDA-12", "SessionState": "Disconnected"},
]

# -----------------------------
# VDA Machines
# -----------------------------
vdas = [
    {"MachineName": "VDA-01", "RegistrationState": "Registered", "PowerState": "On"},
    {"MachineName": "VDA-02", "RegistrationState": "Registered", "PowerState": "On"},
    {"MachineName": "VDA-03", "RegistrationState": "Registered", "PowerState": "On"},
    {"MachineName": "VDA-04", "RegistrationState": "Registered", "PowerState": "On"},
    {"MachineName": "VDA-05", "RegistrationState": "Unregistered", "PowerState": "Off"},
    {"MachineName": "VDA-06", "RegistrationState": "Registered", "PowerState": "On"},
    {"MachineName": "VDA-07", "RegistrationState": "Registered", "PowerState": "On"},
    {"MachineName": "VDA-08", "RegistrationState": "Unregistered", "PowerState": "Off"},
    {"MachineName": "VDA-09", "RegistrationState": "Registered", "PowerState": "On"},
    {"MachineName": "VDA-10", "RegistrationState": "Registered", "PowerState": "On"},
    {"MachineName": "VDA-11", "RegistrationState": "Registered", "PowerState": "On"},
    {"MachineName": "VDA-12", "RegistrationState": "Registered", "PowerState": "On"},
    {"MachineName": "VDA-13", "RegistrationState": "Unregistered", "PowerState": "Off"},
    {"MachineName": "VDA-14", "RegistrationState": "Registered", "PowerState": "On"},
    {"MachineName": "VDA-15", "RegistrationState": "Registered", "PowerState": "On"},
]

# -----------------------------
# License Usage
# -----------------------------
licenses = [
    {
        "Product": "Citrix Virtual Apps",
        "InUse": 120,
        "Total": 250
    },
    {
        "Product": "Citrix Virtual Desktops",
        "InUse": 95,
        "Total": 200
    }
]
