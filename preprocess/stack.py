import pandas as pd
import json

if __name__ == "__main__":
    df = pd.read_excel('data/dataset.xlsx')
    data = df.values
    
    select_province = ['四川省', '山西省', '河北省', '湖南省', '江苏省', '北京市', '黑龙江省', '广东省', '陕西省']
    select_acc_type = ['爆炸', '交通事故', '结构事故', '气体或化学品泄漏', '水浸', '其他']
    select_field = ['重工业', '建筑业', '环卫行业', '煤炭工业', '制造业', '维修养护业', '其他']

    clean_data = {'province': {}, 'type': {}, 'field': {}}

    for item in data:
        time = item[1].split('-')[0]
        time = "year_" + time
        province = item[3]
        field = item[5].split('（')[0]
        accident_type = item[-3]
        if type(accident_type) == type(1.0):
            accident_type = '其他'
        accident_type = accident_type.split('/')[0]

        if (province not in clean_data['province']) and (province in select_province):
            clean_data['province'][province] = {
                'year_2014': 0,
                'year_2015': 0,
                'year_2016': 0,
                'year_2017': 0,
                'year_2018': 0,
                'year_2019': 0,
                'year_2020': 0,
                'year_2021': 0,
                'year_2022': 0
            }
        if province in select_province:
            clean_data['province'][province][time] += 1

        if (field not in clean_data['field']) and (field in select_field):
            clean_data['field'][field] = {
                'year_2014': 0,
                'year_2015': 0,
                'year_2016': 0,
                'year_2017': 0,
                'year_2018': 0,
                'year_2019': 0,
                'year_2020': 0,
                'year_2021': 0,
                'year_2022': 0
            }
        if field in select_field:
            clean_data['field'][field][time] += 1

        if (accident_type not in clean_data['type']) and (accident_type in select_acc_type):
            clean_data['type'][accident_type] = {
                'year_2014': 0,
                'year_2015': 0,
                'year_2016': 0,
                'year_2017': 0,
                'year_2018': 0,
                'year_2019': 0,
                'year_2020': 0,
                'year_2021': 0,
                'year_2022': 0
            }
        if accident_type in select_acc_type:
            clean_data['type'][accident_type][time] += 1
    
    reorder = []
    for key in clean_data['province']:
        cc = {}
        cc['name'] = key
        for year in clean_data['province'][key]:
            cc[year] = clean_data['province'][key][year]
        reorder.append(cc)
    clean_data['province'] = reorder

    reorder = []
    for key in clean_data['type']:
        cc = {}
        cc['name'] = key
        for year in clean_data['type'][key]:
            cc[year] = clean_data['type'][key][year]
        reorder.append(cc)
    clean_data['type'] = reorder

    reorder = []
    for key in clean_data['field']:
        cc = {}
        cc['name'] = key
        for year in clean_data['field'][key]:
            cc[year] = clean_data['field'][key][year]
        reorder.append(cc)
    clean_data['field'] = reorder

    with open("data/stack.json", 'w', encoding='utf8') as json_file:
        json.dump(clean_data, json_file, ensure_ascii=False)