from analytics_engine.local import dedupe,aggregate
E=[{"event_id":"1","event_type":"click","timestamp":"2026-01-01T10:01:00Z","value":2},{"event_id":"1","event_type":"click","timestamp":"2026-01-01T10:01:00Z","value":2},{"event_id":"2","event_type":"click","timestamp":"2026-01-01T10:20:00Z","value":3}]
def test_dedupe():assert len(dedupe(E))==2
def test_aggregate():
 x=aggregate(E)[("2026-01-01T10:00Z","click")];assert x["count"]==2 and x["value_sum"]==5
