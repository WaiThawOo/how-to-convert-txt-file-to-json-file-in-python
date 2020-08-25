import json
datas = []

with open('D:\\Pathtofile\\household_power_consumption.txt', 'r') as data:
    for line in data:
        line = line.strip()
        ldata = line.split(';')
        tempdata = {
            'Date':ldata[0],
            'Time':ldata[1],
            'Global_active_power':ldata[2],
            'Global_reactive_power':ldata[3],
            'Voltage':ldata[4],
            'Global_intensity':ldata[5],
            'Sub_metering_1':ldata[6],
            'Sub_metering_2':ldata[7],
            'Sub_metering_3':ldata[8]
        }
        datas.append(tempdata)
with open('D:\\Pathtofile\\household_power_consumption.json', 'w') as fp:
    json.dump(datas, fp, indent=4)
    #json.loads(datas, object_hook=jsonKeys2int)
    #dict(json.loads(json.dumps(datas.items())))
    #json.loads(datas, object_hook=lambda d: {int(k) if k.lstrip('-').isdigit() else k: v for k, v in d.items()})
from pprint import pprint
pprint(datas)
