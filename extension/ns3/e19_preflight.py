"""E19 ns-3 availability preflight. Standard library; no simulation performed."""
import importlib.util
import json
import os
import platform
import shutil
import socket
from pathlib import Path

def inspect():
    commands={name:shutil.which(name) for name in ("ns3","ns-3","waf","cmake","ninja","g++","git")}
    locations={str(p):p.exists() for p in map(Path,("/opt/ns-3","/usr/local/ns-3","/home/oai/share/ns-3","/mnt/data/ns-3"))}
    modules={}
    for name in ("ns","ns3","cppyy"):
        try: modules[name]=importlib.util.find_spec(name) is not None
        except (ImportError,ValueError): modules[name]=False
    try: socket.getaddrinfo("github.com",443); dns="RESOLVED"
    except OSError as exc: dns="BLOCKED: "+str(exc)
    return {"schema":"e19-preflight-v1","platform":platform.platform(),
            "python":platform.python_version(),"uid":os.geteuid(),
            "commands":commands,"source_locations":locations,
            "python_modules":modules,"github_dns":dns,
            "ns3_executable_detected":bool(commands["ns3"] or commands["ns-3"]),
            "note":"This is a host preflight, NOT a simulator run or proof of functional ns-3."}

if __name__=="__main__":
    print(json.dumps(inspect(),indent=2,sort_keys=True))
