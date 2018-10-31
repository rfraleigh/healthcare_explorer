import json,os,pprint,glob

files = glob.glob('*_*.json')
out_data = dict()
out_data['files']=[]
for file in files:
    out_data['files'].append(file)

with open('file-lookup.json','w') as f:
    f.write(json.dumps(out_data))
f.close()