def get_data(name):  #传入食物名称字符串,搜索并返回食物营养信息
    import json
    with open('finall_result', "r", encoding="UTF-8") as f:
        data = f.read()
    result = []
    data = json.loads(data)
    for i in range(len(data)):
        if name in data[i]['name']:
            result.append(data[i])
    return result

def compute_nutrition(data):   #传入食物信息字典列表,返回各营养素之和
    result = {'carbohydrates':0, 'fat':0, 'heat':0, 'protein':0}
    for i in range(len(data)):
        result['carbohydrates'] += float(data[i]['carbohydrates'])
        result['fat'] += float(data[i]['fat'])
        result['heat'] += float(data[i]['heat'])
        result['protein'] += float(data[i]['protein'])
    return result

def compete_demand(infor):  #传入基本信息列表,返回各营养素的需求
    rrsult =



#print(compute_nutrition(get_data('米饭')))
#infor = [体重(kg), 身高(cm), 模式(bool),  ]