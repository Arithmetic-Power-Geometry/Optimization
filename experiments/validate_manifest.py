"""E13 manifest schema and preregistration guard; stdlib only."""
import json
from pathlib import Path

def validate(path=None):
    path=Path(path) if path else Path(__file__).with_name("E13_MANIFEST.json")
    x=json.loads(path.read_text(encoding="utf-8"))
    assert x["schema"]=="e13-manifest-v1"
    assert x["status"]=="PLANNED_NOT_EXECUTED"
    assert len(x["paired_seeds"])==len(set(x["paired_seeds"]))>=10
    assert x["analysis"]["alpha"]==0.05
    assert x["analysis"]["multiple_testing"]=="Holm correction across predeclared comparisons"
    assert x["limits"]["oracle_timeout_seconds"]>0
    assert x["budgets"]["time_rule"]=="repair_plus_probe"
    assert "exact_oracle" in x["policies"]
    return x

if __name__=="__main__":
    x=validate()
    print("E13 manifest valid:",x["schema"],"paired seeds:",len(x["paired_seeds"]))
