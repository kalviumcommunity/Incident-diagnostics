import json,time,urllib.request
from pathlib import Path
name=json.loads(Path('monitoring/queries.json').read_text())['request_counter']
for i in range(2):
 text=urllib.request.urlopen('http://127.0.0.1:18084/metrics',timeout=5).read().decode()
 lines=[s for s in text.splitlines() if s.startswith(name+'{')]
 if not lines:raise SystemExit('No emitted metric matches the query')
 print(time.time(),*lines,sep='\n');time.sleep(1)
