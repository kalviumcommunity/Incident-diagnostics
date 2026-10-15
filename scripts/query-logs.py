import argparse,json,subprocess,sys
p=argparse.ArgumentParser();p.add_argument('--request-id',required=True);args=p.parse_args()
text=subprocess.check_output(['docker','compose','exec','-T','app','cat','/app/logs/requests.jsonl'],text=True)
matches=[]
for line in text.splitlines():
 d=json.loads(line)
 if d.get('request_id')==args.request_id and 'level' in d:matches.append(d)
for d in matches:print(json.dumps(d))
if not matches:sys.exit('No schema-valid matching log record')
