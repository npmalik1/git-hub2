prof = dict1['profession']
city_type = dict1['city_type']
salary = dict1['salary']  # 50000
if prof == "developer":
    if city_type == "metropolitan":
        if dict1['id']>150:  # 144>150
            dict1["salary"] = salary+10000
        else:
            dict1['salary'] = salary-10000
    else:
        dict1["salary"] = salary+5000

print(dict1)