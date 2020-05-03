import json

with open('/home/wagio/repos/virustotal/vt_clean.json', 'r') as f:
    data = json.load(f)
    for sample in data:
        print(str(sample) + ' & ' + str(data[sample]['positives']) + "/" + str(data[sample]['total']) + " & " + str(data[sample]['scan_date'])[:10])