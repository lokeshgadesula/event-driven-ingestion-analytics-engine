from datetime import datetime,timezone
def dedupe(es):
 seen=set();out=[]
 for e in es:
  if e["event_id"] not in seen:seen.add(e["event_id"]);out.append(e)
 return out
def aggregate(es):
 out={}
 for e in dedupe(es):
  dt=datetime.fromisoformat(e["timestamp"].replace("Z","+00:00")).astimezone(timezone.utc);k=(dt.strftime("%Y-%m-%dT%H:00Z"),e["event_type"]);x=out.setdefault(k,{"count":0,"value_sum":0.0});x["count"]+=1;x["value_sum"]+=float(e.get("value",0))
 return out
