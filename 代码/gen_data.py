import json
import requests as rs
import time
import uuid
import pandas as pd
def gen_uuid():
	return str(uuid.uuid4()).replace('-','')
def gen_ts():
	return int(time.time())
#华尔街
#1642736450
def gen_wrj_data(ts): 
        url='https://api-one.wallstcn.com/apiv1/content/lives?accept=live%2Cvip-live&channel=global-channel&cursor={}&first_page=1&limit=30'.format(ts)#cursor上一段时间戳
        header={
        'Host': 'api-one.wallstcn.com',
        'X-Taotie-Device-Id': r'0ED7F1F4-6F6B-4C40-A9D3-65ED677DE4ED',
        'X-Language': 'zh',
        'Accept': '*/*',
        'X-Track-Info': '{"connectionType":"WIFI","orientation":"UNKNOWN","osName":"iOS","channel":"app-store","appId":"finance.News.ios","osVersion":"15.1","locale":"zh_CN","deviceModel":"iPad12,1","deviceBrand":"iPad","appVersion":"6.8.12","resolution":"2160x1620","carrier":"UNKNOWN"}',
        'Cookie': 'virtual_key=3WClDXcCZgKBpZbDhh+CY2Uq0RuOIHZoa82LQUUBqpQ99xa5AKqWHA7gi4HY4sDqMAdhTUf6LMWz/unaCJCmFvpQh81V/BAzJthvZ9x3Ogm0MTL00n+xlF2mmDbIVhSIB2Iq+AiJ6/4evb3SxkFW36AmakCsFHt64qCgLQ+fv5dTtfo32/Z0fISYJyL5vCJ5GvOInscIbd+cSKOSEuvNVadihX1nYznxBn0yxenAOA/A5ApCxzIrjJ6vq/NbGZIywv8VtByLh2w6oDXt2U2ICPFh+VyU9T2plr3HLFLQRTQGsUO8GrW7hCdQBzpGIz4txEcQVpuZg7IQRoMITy2Yow==',
        'X-Ivanka-Platform': 'wscn-platform',
        'X-Ivanka-vipApp': 'wscn|iOS|6.8.12|15.1|0|finance.News',
        'X-Ivanka-Token': '3WClDXcCZgKBpZbDhh+CY2Uq0RuOIHZoa82LQUUBqpQ99xa5AKqWHA7gi4HY4sDqMAdhTUf6LMWz/unaCJCmFvpQh81V/BAzJthvZ9x3Ogm0MTL00n+xlF2mmDbIVhSIB2Iq+AiJ6/4evb3SxkFW36AmakCsFHt64qCgLQ+fv5dTtfo32/Z0fISYJyL5vCJ5GvOInscIbd+cSKOSEuvNVadihX1nYznxBn0yxenAOA/A5ApCxzIrjJ6vq/NbGZIywv8VtByLh2w6oDXt2U2ICPFh+VyU9T2plr3HLFLQRTQGsUO8GrW7hCdQBzpGIz4txEcQVpuZg7IQRoMITy2Yow==',
        'Accept-Language': 'zh-Hans-CN;q=1',
        'User-Agent': 'WSCN/6.8.12 (iPad; iOS 15.1; Scale/2.00)',
        'X-Device-Id': '0ED7F1F4-6F6B-4C40-A9D3-65ED677DE4ED',
        'X-Ivanka-App': 'wscn|iOS|6.8.12|15.1|0|finance.News',
        'Connection': 'Keep-Alive',
        'X-Device-Identify': '00000000-0000-0000-0000-000000000000',
        'X-Client-Type': 'pad',
        'Accept-Encoding': 'gzip, deflate, br'
                }
        
        res=rs.get(url,headers=header)
        info=json.loads(res.text)['data']
        return info
'''
info=gen_wrj_data(gen_ts())
items=[]
for t in range(300):
        print(t)
        for i in range(30):
                items.append(info['items'][i]['content_text'])
        info=gen_wrj_data(info['next_cursor'])
        time.sleep(5)
s=pd.DataFrame(items,columns=['text'])
s.to_csv('huaerjie.csv',encoding='utf_8_sig')
'''
#print(info['items'][0]['content_text'])

#print("nextcursor:{}".format(info['next_cursor']))


#res=rs.get("https://www.baidu.com?")
#print(res)
#print(time.time())
'''
#每日经济新闻1642737404
def gen_nbd(lt='2022-02-11 09:59:54'):
        url1='https://api.nbd.com.cn/3/columns/multi_columns_articles.json?app_key=d401a38c50a567882cd71cec43201c78&app_version_name=6.4.5&client_key=iPhone&column_ids=376%3A377%3A378%3A379%3A380%3A381%3A725%3A1320%3A1321%3A1441%3A1447%3A1531%3A1532%3A1533%3A1534%3A1535%3A1536%3A1537%3A1538%3A1539%3A1556&count=15&page=1&published_at={}&timestamp={}&uuid={}'.format(lt,gen_ts(),gen_uuid())

        header={
                'Host': 'api.nbd.com.cn',
                'Accept': '*/*',
                'User-Agent': 'NBD2/100 (iPad; iOS 15.1; Scale/2.00)',
                'Accept-Language': 'zh-Hans-CN;q=1',
                'Accept-Encoding': 'gzip, deflate',
                'Connection': 'keep-alive'
        }
        res=rs.get(url1,headers=header)
        info=json.loads(res.text)
        return info

info=gen_nbd()
items=[]
for t in range(3):
        lt=info['data'][-1]['published_at']
        for i in range(15):
                items.append(info['data'][i]['title'])
        info=gen_nbd(lt)

'''
'''
#央视
def gen_cctv(page=1):
        url='https://financeapi.cctv.cn/financemobileinf/rest/cctv/cardgroups'
        header={
                'Host': 'financeapi.cctv.cn',
                'Content-Type': 'application/x-www-form-urlencoded',
                'Cookie': 'SERVERID=4abfe7ceafacdfe7efe3ac15e1662f35|1642735276|1642735255; acw_tc=76b20f8716427352551855941e5db6afbd0d3f0f317ab078f9cba18c200553; aliyungf_tc=fa8c1111ccf977013fa671ef809c1d5bfa042593b5a900e83976068d2c287b97',
                'Connection': 'keep-alive',
                'Accept': '*/*',
                'User-Agent': 'yang shi cai jing/8.3.1 (iPad; iOS 15.1; Scale/2.00)',
                'Accept-Language': 'zh-Hans-CN;q=1',
                'Content-Length': '312',
                'Accept-Encoding': 'gzip, deflate, br'
        }

        params={
                'appcommon':{"ap":"ios_phone","adid":"00000000-00000000-00000000","av":"8.3.1","an":"央视财经"},
                'json':
                '{"paging":{"page_no":'+str(page)+',"page_size":"20"},"cardgroups":"HOUR","userId":""}'
        }
        res=rs.post(url,headers=header,data=params)
        return json.loads(res.text)

items=[]
for t in range(3):
        info=gen_cctv(page=t)
        for i in range(20):
                items.append(info['cardgroups'][i]['cards'][0]['title'])
        #info=gen_nbd(lt)



'''
'''
#eastmoney
#eastmoney
def gen_es(code='SH510300',p=1):
        headers={
                "Host": "gbapi-wg.eastmoney.com",
        'EM-GT': '897E980B2CE34A0681EE755B54C7BC4e',
        'Accept': '*/*',
        'EM-CT': '',
        'EM-VER': '9.9',
        'EM-UT': '',
        'Accept-Encoding': 'gzip',
        'Accept-Language': 'zh-cn',
        'EM-OS': 'iOS',
        'EM-MD': 'MkJCOUZGNkItRjU2NS00MDcyLUEwQjUtRkUyMUMwRUUyMDAw',
        'User-Agent': 'app-iphone-client-iPad12,1-2BB9FF6B-F565-4072-A0B5-FE21C0EE2000',
        'EM-PKG': 'com.eastmoney.iphone',
        'Content-Length': '252',
        'Connection': 'keep-alive',
        'Content-Type': 'application/x-www-form-urlencoded'
        }
        url='https://gbapi-wg.eastmoney.com/apparticlelist/api/Article/Articlelist?code=SH510300'
        data={'code': code, 'ps': '20', 'p': p, 'type': '0', 'sorttype': '0', 'uid': '', 'is_deal_user': '0', 'cachetag': '', 'firstps': '10', 'deviceid': '1e904461ae7fabe242035b19daad1451', 'version': '9009000', 'ctoken': '', 'utoken': '', 'product': 'EastMoney', 'plat': 'Iphone', 'randomtext': 'AFk25xzYkl-AyJXsyoVzSd2LhNlqykPB11XSjwaiPAFHss8dlBZdgA'}
        res=rs.post(url,headers=headers,data=data)
        return json.loads(res.text)#['re'][0]['post_content']
codes=['SH510300','SH513300']
items=[]
for code in codes:
        for t in range(800):
                print('code:{} t:{}'.format(code,t))
                info=gen_es(code=code,p=t)
                for i in range(10):
                        items.append(info['re'][i]['post_content'])
                time.sleep(2)
s=pd.DataFrame(items,columns=['text'])
s.to_csv('es.csv',encoding='utf_8_sig',index=False)
'''
from bs4 import BeautifulSoup as bs

headers={
        'Host': 'gz.lianjia.com',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:64.0) Gecko/20100101 Firefox/64.0',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
        'Accept-Language': 'zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2',
        'Accept-Encoding': 'gzip, deflate, br',
        'Referer': 'https://gz.lianjia.com/ershoufang/co32rs%E5%B9%BF%E5%B7%9E/',
        'onnection': 'keep-alive',
        'Cookie':'BMAP_SECKEY=XrwbXzjsJVoGG-0eX0Udx0Od5X0dQ_w0C0plao2fafQpaqHM_oR41oOuvmt2araq0OxZbE7Q0OvploZ-bA5MPq9rlObDbE43gTe7VKgGDLRK7m2cDHoNgrRBRHpWN0h6gyTewnrrEtdj6oFMI0uTvYgXXoJON3kXYReA9qYn2V8yIplvyWXp2syxB7Rkrttm; lianjia_ssid=bfe15044-d922-4c3e-a227-ba1320135b31; lianjia_uuid=d6a74fd3-e6c9-4aef-a99f-80e1966efaab; select_city=440100; _smt_uid=62089bb4.5c2da171; UM_distinctid=17ef1a03914449-0d41ff24fddbf7-4c312e7e-144000-17ef1a03916694; CNZZDATA1255849599=1944897891-1644730753-https%253A%252F%252Fwww.baidu.com%252F%7C1644751732; CNZZDATA1254525948=873006938-1644726131-https%253A%252F%252Fwww.baidu.com%252F%7C1644750231; CNZZDATA1255633284=1602131109-1644721425-https%253A%252F%252Fwww.baidu.com%252F%7C1644744761; CNZZDATA1255604082=581366039-1644728652-https%253A%252F%252Fwww.baidu.com%252F%7C1644751659; _jzqa=1.3680079862575101400.1644731317.1644746190.1644753611.4; _jzqc=1; _jzqy=1.1644731317.1644731317.1.jzqsr=baidu.-; _jzqckmp=1; _qzja=1.731834270.1644731317408.1644746189680.1644753611056.1644754170656.1644754185532.0.0.0.30.4; _qzjc=1; _qzjto=30.4.0; sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%2217ef1a03d1c571-06eab094a5af22-4c312e7e-1327104-17ef1a03d1d4f9%22%2C%22%24device_id%22%3A%2217ef1a03d1c571-06eab094a5af22-4c312e7e-1327104-17ef1a03d1d4f9%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E7%9B%B4%E6%8E%A5%E6%B5%81%E9%87%8F%22%2C%22%24latest_referrer%22%3A%22%22%2C%22%24latest_referrer_host%22%3A%22%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC_%E7%9B%B4%E6%8E%A5%E6%89%93%E5%BC%80%22%7D%7D; sajssdk_2015_cross_new_user=1; srcid=eyJ0Ijoie1wiZGF0YVwiOlwiMzE5ODUzYTUxMDQ2MmM5ZDU3NmQwZDVlMzk1ZTVmYjM1ZDY4ZTYzYmViZjIyOGY4NGM2Y2Q5MGZjYjEyOGU1ZjMwOTFkZjJlMDdiM2EyOTQ2MGU3NDcwOGU1OTAzMjU1YmU1YjZlYTRhYTk3N2U2ZTgyMjA1MDhiMTM0ZmM1ODYyYmMxMzBhZDZmNDczZjY5ZWIzZDg5OTBiY2Y1YTU1ODFhMDJiNDIxOGRiYjEzNTU2MmNlMjlkNzQwMTg3ZDQ3NDE0OWM2NjdlZWU1MWY3MjE0OTdkYTNkNWVhMDJkN2NlNTFlODhlYTBiYjQyYWI5ZGVlYjQ4ZDhjNzg2MjZlN1wiLFwia2V5X2lkXCI6XCIxXCIsXCJzaWduXCI6XCJhNmRjOTUyMFwifSIsInIiOiJodHRwczovL2d6LmxpYW5qaWEuY29tL2Vyc2hvdWZhbmcvMTA4NDAzMDcxMzM5Lmh0bWwiLCJvcyI6IndlYiIsInYiOiIwLjEifQ==; Hm_lvt_9152f8221cb6243a53c83b956842be8a=1644731324; Hm_lpvt_9152f8221cb6243a53c83b956842be8a=1644754186; _ga=GA1.2.1641224034.1644731342; _gid=GA1.2.1336423666.1644731342; _jzqx=1.1644746190.1644753611.2.jzqsr=gz%2Elianjia%2Ecom|jzqct=/ershoufang/pg6co6rs%e5%b9%bf%e5%b7%9e/.jzqsr=gz%2Elianjia%2Ecom|jzqct=/ershoufang/co32rs%e5%b9%bf%e5%b7%9e/',
        'Upgrade-Insecure-Requests': '1',
        'Cache-Control': 'max-age=0'
        }
items=[]
index=['地址', '地区', '房屋信息', '总价', '每平米单价', '房屋户型', '所在楼层', '建筑面积', '户型结构', '套内面积', '建筑类型', '房屋朝向', '建筑结构', '装修情况', '梯户比例', '配备电梯', '挂牌时间', '交易权属', '上次交易', '房屋用途', '房屋年限', '产权所属', '抵押信息', '房本备件']
for k in range(60,80):
        print(k)
        time.sleep(0.5)
        url='https://gz.lianjia.com/ershoufang/pg{}co32rs%E5%B9%BF%E5%B7%9E/'.format(k)
        res=rs.get(url,headers)
        soup=bs(res.text,'html.parser')
        info=soup.find('ul',attrs={'class':"sellListContent"})
        info_list=info.find_all(attrs={'class':'info clear'})
        for num in range(len(info_list)):#
                ar=info_list[num].contents[1].find_all('a')
                item=[]

                time.sleep(0.1)
                addr=ar[0].text
                region=ar[1].text
                houseInfo=info_list[num].contents[2].div.text
                prices=info_list[num].contents[5].find_all('span')
                price=float(prices[0].string)
                per_price=prices[1].string
                
                detail=rs.get(info_list[num].contents[0].a['href'],headers)
                soup1=bs(detail.text,'html.parser')
                for _ in [addr,region,houseInfo,price,per_price]:
                      item.append(_)  
                
                ul=soup1.find_all('ul')[4].find_all('li')
                for i in ul:
                       item.append(i.text[4:])
                       #index.append(i.text[:4])

                ul=soup1.find_all('ul')[5].find_all('li')
                for i in ul:
                       item.append(i.find_all('span')[1].text.replace('\n','').strip())
                       #index.append(i.find_all('span')[0].text.replace('\n','').strip())
                #print(len(item))
                if len(item)==24:
                        items.append(item)
'''
for i in range(0,25):
	print('{}:{}'.format(index[i],items[0][i]))
'''
s=pd.DataFrame(items,columns=index)
s.to_csv('data3.csv',encoding='utf_8_sig',index=False)
