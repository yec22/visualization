import json

result = {}

with open('pie_prov.json', 'r', encoding='utf-8') as f:
    data = json.load(f)
    for key in data:
        infos = data[key]
        for info in infos:
            prov = info['type']
            number = info['number']
            if prov == '内蒙古自治区':
                prov = '内蒙古'
            elif prov == '黑龙江省':
                prov = '黑龙江'
            else:
                prov = prov[:2]
            if prov not in result:
                result[prov] = number
            else:
                result[prov] += number

for key in result:
    print('if (name == "{}") {{ info = "{}2014年至2022年事故总数：{}"; }}'.format(key, key, result[key]))
