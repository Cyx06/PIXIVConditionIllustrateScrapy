import requests
import json
import time
import random

ip = ['20.213.247.195','13.74.59.33','145.40.121.101','45.167.125.97','157.100.12.138','173.244.48.9','51.79.205.165','190.15.103.66','45.42.177.50','8.219.64.236']
url='https://www.pixiv.net/ajax/search/illustrations/'
headers = {
    'user-agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Mobile Safari/537.36 Edg/105.0.1343.42',
    # 'cookie': 'your cookie'
}
cookie ={
    'login_ever':'yes',
    'user_id':'8 bit numberm, for example: 86311421'
}

like=[]
il_url = []

def bubbleSort(arr, arr2):
    n = len(arr)   
    for i in range(n):        
        for j in range(0, n-i-1): 
            if int(arr[j]) < int(arr[j+1]) :
                arr[j], arr[j+1] = arr[j+1], arr[j]
                arr2[j], arr2[j+1] = arr2[j+1], arr2[j]

def pixiv_get(keyword, page, rating_count):
    for a in range(1, page+1):
        params = {
            'p':str(a),
            'type': 'illust_and_ugoira',
            'word': keyword,
            'mode': 'all',
            'order': 'date_d',
            's_mode': 's_tag_full',
            'lang': 'zh_tw'
        }
        web = requests.get(url+params['word']+'?', headers=headers , params=params,  proxies={'http':ip[random.randint(0,9)]})
        print(web)
        js=web.json()['body']['illust']['data']
        # response = requests.get('https://www.pixiv.net/ajax/search/manga/' + params['word'] + '?', params = params)
        # print(json.dumps(response.json(), sort_keys = True, indent = 4, ensure_ascii = False))
        print("js", js)
        time.sleep(random.uniform(1, 2))

        for i in js:
            print("i", i)
            print("----------------------------------------------")
            url2='https://www.pixiv.net/touch/ajax/illust/details?'
            params2 ={
                'illust_id':i['id'],
                'ref': 'https://www.pixiv.net/manage/requests',
                'lang': 'zh_tw'
            }
            web2 =requests.get(url2, headers=headers, params=params2,cookies=cookie, proxies={'http':ip[random.randint(0,9)]})
            if int(web2.json()['body']['illust_details']['rating_count']) > rating_count:
                like.append(web2.json()['body']['illust_details']['rating_count'])
                z = i['url'].replace('i.pximg.net/c/250x250_80_a2', 'i.pixiv.cat')
                il_url.append(z)
            else:
                pass    
        print('第' + str(a) + '頁')    

    bubbleSort(like, il_url)

    name = 1
    for d in il_url:
        jpg = requests.get(d)     
        f = open(f'/output/path/text_{name}.jpg', 'wb')    
        f.write(jpg.content)   
        f.close()              
        name += 1

keyword = '中野四葉' # 'input your key word, for example: 中野四葉'
page = 1 # 'page number you want to scrapy'
rating_count = 100 # good number limit, you only will scrapy higher than this number's pic

pixiv_get(keyword, page, rating_count)
