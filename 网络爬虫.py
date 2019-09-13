def get_url():    #用于获取待解析网址
    def get_one_url(page):  #用于获取一页网页网址,参数传入int类型
        import re
        exp = '<a href="(.*?)" title=".*?" target=\'_blank\'>(.*?)</a>'
        url_list = []
        for i in range(10):
            j = i + 1
            if page:
                url = 'http://www.boohee.com/food/group/' + str(j) + '?page=' + str(page)
            else:
                url = 'http://www.boohee.com/food/group/' + str(j)
            fa_url = [url]
            file_url = get_source_and_save(fa_url)
            with open(file_url[0], "r", encoding="UTF-8") as f:
                fa_source = f.read()
            a = re.findall(exp,fa_source)
            url_list.append(a)
        return url_list
    result = []
    for i in range(10):
        j = i + 1
        a = get_one_url(j)
        result.append(a)
        print('1')
    return result
def process(chaotic_url):
    name = []
    url = []
    for a in range(10):
        b = chaotic_url[a]
        for c in range(10):
            d = b[c]
            for e in range(len(d)):
                f = list(d[e])
                g = 'http://www.boohee.com' + f[0]
                name.append(f[1])
                url.append(g)
        print('2')
    result = [url,name]
    return result
def get_source_and_save(url_line):  #用于获取网页源代码并保存,参数以列表形式传入
    file_url = []
    for i in range(len(url_line)):
        file_url.append('C:\\Users\\24253\Desktop\\营养计算器\\source' + str(i))
    #print(file_url)
    import requests as req
    for i in range(len(url_line)):
        obj = req.get(url_line[i])
        obj.encoding = 'UTF-8'
        file = open(file_url[i],'w',encoding='UTF-8')
        file.write(obj.text)
        print('3')
    return file_url
def find_number(url):   #用于分析网页源代码,url以字符串形式输入
    import re
    with open(url,"r",encoding="UTF-8") as f:
        source = f.read()
    exp_w = '热量\(大卡\)</span><span class="dd"><span class="stress red1">(.*?)</span></span></dd>'
    exp_c = '碳水化合物\(克\)</span><span class="dd">(.*?)</span></dd>'
    exp_p = '蛋白质\(克\)</span><span class="dd">(.*?)</span></dd>'
    exp_f = '脂肪\(克\)</span><span class="dd">(.*?)</span></dd>'
    exp_list = [exp_w,exp_c,exp_p,exp_f]
    result_list = []
    for i in range(4):
        result = re.findall(exp_list[i],source)
        result_list.append(result[0])
        print('4')
    return result_list
def every():
    url = get_url()
    url_and_name = process(url)
    url_list = url_and_name[0]
    file_url = get_source_and_save(url_list)
    number = []
    for i in range(len(file_url)):
        file = file_url[i]
        t = find_number(file)
        number.append(url_and_name[1][i])
        number = number + t
    return number
def save_to_json(number):
    json = []
    long = len(number) - 1
    i, j = 0, 0
    while True:
        n, x, y, z, m = i, i+1, i+2, i+3, i+4
        #print(n,x,y,z,m)
        dictionary = {'number':j,'name':number[n],'heat':number[x],
                      'carbohydrates':number[y],'protein':number[z],'fat':number[m]}
        json.append(dictionary)
        if m < long:
            i = i + 5
            j = j + 1
        else:
            break
        import json as js
        result = js.dumps(json, sort_keys=True, indent=4,ensure_ascii=False)
        url = 'C:\\Users\\24253\\Desktop\\营养计算器\\finall_result'
        with open(url, 'w', encoding = 'UTF-8') as f:
            f.write(result)
            f.close()
        print('5')
number = every()
save_to_json(number)




