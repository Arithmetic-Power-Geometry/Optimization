"""E18 Mininet/OVS fixed-path link failure/repair prototype.
PROPOSED / NOT EXECUTED. Linux root + Mininet + OVS required.
Run: sudo python3 extension/mininet/e18_mininet.py --topology Abilene --seed 101
Uses real historical topology structure with synthetic injected link failure.
"""
import argparse
import csv
import hashlib
import json
import os
import platform
import random
import shutil
import sys
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
NAMES=("Abilene","Geant2012","Arpanet19728")

def topology_edges(name):
    if name not in NAMES:
        raise ValueError("unknown verified topology")
    path=ROOT/"data"/"E15_clean"/(name+".edges.csv")
    with path.open(newline="") as f:
        edges=[(int(row["u"]),int(row["v"])) for row in csv.DictReader(f)]
    if len(set(tuple(sorted(e)) for e in edges))!=len(edges):
        raise ValueError("duplicate topology edges")
    return edges

def check_environment():
    try:
        import mininet.net
        import mininet.node
        import mininet.link
    except ImportError as exc:
        raise RuntimeError("BLOCKED: Python Mininet module unavailable") from exc
    missing=[tool for tool in ("ovs-vsctl","ovs-ofctl","ip","ping") if not shutil.which(tool)]
    if missing:
        raise RuntimeError("BLOCKED: missing required executables "+",".join(missing))
    if os.geteuid()!=0:
        raise RuntimeError("BLOCKED: root privilege required")
    return True

def experiment(name,seed,repair_budget=1):
    check_environment()
    from mininet.net import Mininet
    from mininet.node import OVSBridge
    from mininet.link import TCLink
    from mininet.log import setLogLevel
    setLogLevel("warning")
    edges=topology_edges(name)
    nodes=sorted(set(v for e in edges for v in e))
    if len(nodes)<2:
        raise RuntimeError("insufficient nodes")
    net=Mininet(controller=None,switch=OVSBridge,link=TCLink,build=False,autoSetMacs=True)
    switches={v:net.addSwitch("s"+str(v),failMode="standalone") for v in nodes}
    links={}
    for u,v in edges:
        links[(u,v)]=net.addLink(switches[u],switches[v])
    h0=net.addHost("hstart",ip="10.0.0.1/24")
    h1=net.addHost("hend",ip="10.0.0.2/24")
    net.addLink(h0,switches[nodes[0]])
    net.addLink(h1,switches[nodes[-1]])
    events=[]
    try:
        net.build()
        net.start()
        def verify(label):
            # Host-to-host reachability is NOT fixed-route reachability.
            # A redundant topology may reroute around the failed link.
            cmd=h0.cmd("ping -n -c 1 -W 2 10.0.0.2")
            ok=("1 received" in cmd or "1 packets received" in cmd)
            events.append({"event":label,"host_ping_success":ok,"raw_ping":cmd.strip()[-600:]})
            return ok
        def observe():
            # Valid only for the configured monitor pair; no hidden-state read.
            return verify("observe")
        def repair(edge):
            if edge not in links:
                raise ValueError("edge absent")
            a,b=edge
            net.configLinkStatus("s"+str(a),"s"+str(b),"up")
            events.append({"event":"repair","edge":[a,b]})
        verify("before_failure")
        rng=random.Random(seed)
        failed=edges[rng.randrange(len(edges))]
        net.configLinkStatus("s"+str(failed[0]),"s"+str(failed[1]),"down")
        events.append({"event":"synthetic_failure","edge":list(failed),"seed":seed})
        observe()
        if repair_budget:
            repair(failed) # DIAGNOSTIC ORACLE ONLY; uses hidden failure identity.
        verify("after_repair")
        return {"status":"EXECUTED","topology":name,"seed":seed,
                "repair_budget":repair_budget,"events":events,
                "warning":"Repair action is a diagnostic oracle, not a deployable policy."}
    finally:
        net.stop()

def main():
    parser=argparse.ArgumentParser()
    parser.add_argument("--topology",choices=NAMES,default="Abilene")
    parser.add_argument("--seed",type=int,default=101)
    parser.add_argument("--repair-budget",type=int,choices=(0,1),default=1)
    parser.add_argument("--output",type=Path)
    args=parser.parse_args()
    # Do not claim success or create fake measurements on missing dependencies.
    try:
        result=experiment(args.topology,args.seed,args.repair_budget)
    except Exception as exc:
        print("E18 BLOCKED:",exc,file=sys.stderr)
        return 2
    output=args.output or ROOT/"results"/"E18_MININET_ACTUAL.json"
    output.parent.mkdir(parents=True,exist_ok=True)
    result["host"]={"python":platform.python_version(),"platform":platform.platform()}
    output.write_text(json.dumps(result,indent=2)+"\n",encoding="utf-8")
    print(output)
    return 0

if __name__=="__main__":
    raise SystemExit(main())
