import json,os,pprint,glob

datafiles = glob.glob('*.json')

for file in datafiles:
    print(file)
    data = json.loads(open(file,'r').read())
    intensity = sorted(set([item[2] for item in data]))
    pprint.pprint(intensity)
    print('\n\n')
