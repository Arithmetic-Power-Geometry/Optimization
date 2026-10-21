"""E18 dependency preflight. Standard library, safe without network privileges."""
import importlib.util
import json
import os
import platform
import shutil
import socket
from pathlib import Path

def inspect():
    commands={name:shutil.which(name) for name in ("mn","ovs-vsctl","ovs-ofctl","ip","ping")}
    try:
        dns=socket.getaddrinfo("github.com",443)
        github_dns="RESOLVED" if dns else "EMPTY"
    except OSError as exc:
        github_dns="BLOCKED: "+str(exc)
    try:
        mininet_installed=importlib.util.find_spec("mininet") is not None
    except (ModuleNotFoundError,ValueError):
        mininet_installed=False
    ready=all(commands.values()) and mininet_installed and os.geteuid()==0
    return {"schema":"e18-preflight-v1","python":platform.python_version(),
            "platform":platform.platform(),"euid":os.geteuid(),
            "commands":commands,"mininet_python_installed":mininet_installed,
            "github_dns":github_dns,"ready_to_attempt":bool(ready),
            "note":"Preflight does not prove Mininet/OVS dataplane readiness."}

if __name__=="__main__":
    print(json.dumps(inspect(),indent=2,sort_keys=True))
