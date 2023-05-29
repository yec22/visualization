import pandas as pd
import json

if __name__ == "__main__":
    df = pd.read_excel('data/dataset.xlsx')
    data = df.values
    
    clean_data = {}
    for item in data:
        time = item[1].split('-')[0]
        time = "year_" + time
        if time not in clean_data:
            clean_data[time] = {}
        accident_type = item[-3]
        if type(accident_type) == type(1.0):
            accident_type = '其他'
        accident_type = accident_type.split('/')[0]
        if accident_type not in clean_data[time]:
            clean_data[time][accident_type] = 0
        clean_data[time][accident_type] += 1
    
    for year in clean_data:
        reorder = []
        for accident in clean_data[year]:
            reorder.append({'type': accident, 'number': clean_data[year][accident]})
        clean_data[year] = reorder

    with open("data/pie.json", 'w', encoding='utf8') as json_file:
        json.dump(clean_data, json_file, ensure_ascii=False)