import json

with open('/home/wagio/repos/virustotal/vt_clean.json','r') as f:
    stats = json.load(f)

with open('/home/wagio/repos/TFG/statistics_testing_new.json','r') as f:
    stats2 = json.load(f)

i=0
for sample in stats2:
    if sample in stats and stats[sample]['positives'] != 'null' and int(stats[sample]['positives']) == 0:
        print(str(sample))
        i += 1


print(f"{i}/{str(len(stats2))}")