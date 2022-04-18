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

#每日经济新闻1642737404
'''
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
for t in range(800):
        print('nbd:{}'.format(t))
        lt=info['data'][-1]['published_at']
        for i in range(15):
                items.append(info['data'][i]['title'])
        info=gen_nbd(lt)
        time.sleep(3)
s=pd.DataFrame(items,columns=['text'])
s.to_csv('nbd.csv',encoding='utf_8_sig')
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
'''
items=[]
for t in range(3):
        info=gen_cctv(page=t)
        for i in range(20):
                items.append(info['cardgroups'][i]['cards'][0]['title'])
        #info=gen_nbd(lt)



'''

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
        url='https://gbapi-wg.eastmoney.com/apparticlelist/api/Article/Articlelist?code={}'.format(code)
        data={'code': code, 'ps': '20', 'p': p, 'type': '0', 'sorttype': '0', 'uid': '', 'is_deal_user': '0', 'cachetag': '', 'firstps': '10', 'deviceid': '1e904461ae7fabe242035b19daad1451', 'version': '9009000', 'ctoken': '', 'utoken': '', 'product': 'EastMoney', 'plat': 'Iphone', 'randomtext': 'AFk25xzYkl-AyJXsyoVzSd2LhNlqykPB11XSjwaiPAFHss8dlBZdgA'}
        res=rs.post(url,headers=headers,data=data)
        return json.loads(res.text)#['re'][0]['post_content']
'''
codes=['SH510300','SH513300']
items=[]
for code in codes:
        for t in range(1):
                print('code:{} t:{}'.format(code,t))
                info=gen_es(code=code,p=t)
                for i in range(10):
                        items.append([info['re'][i]['post_publish_time'],info['re'][i]['post_content']])
                time.sleep(2)
s=pd.DataFrame(items,columns=['time','text'])
s.to_csv('es30.csv',encoding='utf_8_sig',index=False)
'''
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
        'Cookie':'BMAP_SECKEY=XrwbXzjsJVoGG-0eX0Udx6NmC2p4jSAn_fW_IyyL3emad-fTY_Rb1wo62UjgwHDnRyAm4AFZRiPXE6Us9ocgW-2lUbCKqeiSmsT87Vk8Y6o2oY_dgTqOhNzPbkIXeKT39QpKfnlzn8vrL1cpw__p3Q3Zpgy1lSrOyjriPAp8exvOsT1VS-ZQGdO5YuI0FtTq; SECKEY_ABVK=+FrjTgPJBSTFoQvUuVtVmQFWV5S3+8kQDuFUhT+QN0w%3D; lianjia_uuid=d6a74fd3-e6c9-4aef-a99f-80e1966efaab; select_city=440100; _smt_uid=62089bb4.5c2da171; UM_distinctid=17ef1a03914449-0d41ff24fddbf7-4c312e7e-144000-17ef1a03916694; CNZZDATA1255849599=1944897891-1644730753-https%253A%252F%252Fwww.baidu.com%252F%7C1644795807; CNZZDATA1254525948=873006938-1644726131-https%253A%252F%252Fwww.baidu.com%252F%7C1644758531; CNZZDATA1255633284=1602131109-1644721425-https%253A%252F%252Fwww.baidu.com%252F%7C1644797056; CNZZDATA1255604082=581366039-1644728652-https%253A%252F%252Fwww.baidu.com%252F%7C1644761052; _jzqa=1.3680079862575101400.1644731317.1644767153.1644805443.9; _jzqy=1.1644731317.1644731317.1.jzqsr=baidu.-; _jzqckmp=1; _qzja=1.731834270.1644731317408.1644767153186.1644805442991.1644767250266.1644805442991.0.0.0.41.9; sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%2217ef1a03d1c571-06eab094a5af22-4c312e7e-1327104-17ef1a03d1d4f9%22%2C%22%24device_id%22%3A%2217ef1a03d1c571-06eab094a5af22-4c312e7e-1327104-17ef1a03d1d4f9%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E7%9B%B4%E6%8E%A5%E6%B5%81%E9%87%8F%22%2C%22%24latest_referrer%22%3A%22%22%2C%22%24latest_referrer_host%22%3A%22%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC_%E7%9B%B4%E6%8E%A5%E6%89%93%E5%BC%80%22%7D%7D; Hm_lvt_9152f8221cb6243a53c83b956842be8a=1644731324; _ga=GA1.2.1641224034.1644731342; _gid=GA1.2.1336423666.1644731342; _jzqx=1.1644746190.1644805443.5.jzqsr=gz%2Elianjia%2Ecom|jzqct=/ershoufang/pg6co6rs%e5%b9%bf%e5%b7%9e/.jzqsr=gz%2Elianjia%2Ecom|jzqct=/ershoufang/pg6co32rs%e5%b9%bf%e5%b7%9e/; _jzqc=1; _qzjc=1; srcid=eyJ0Ijoie1wiZGF0YVwiOlwiMzE5ODUzYTUxMDQ2MmM5ZDU3NmQwZDVlMzk1ZTVmYjM1ZDY4ZTYzYmViZjIyOGY4NGM2Y2Q5MGZjYjEyOGU1ZjMwOTFkZjJlMDdiM2EyOTQ2MGU3NDcwOGU1OTAzMjU1YmU1YjZlYTRhYTk3N2U2ZTgyMjA1MDhiMTM0ZmM1ODYyYmMxMzBhZDZmNDczZjY5ZWIzZDg5OTBiY2Y1YTU1OGM3NDFlNjNmZWM3Zjc1YjFlZWU2MWU1NjQ4MzE0ZTJkZjVmNTY5MDc5OGQ4NzIyZjYxMjRlZmUyNTk1MDQ1MWZkZGNjMWI0Mzg4ZDBjNGRlMDI2NWJiMjc2MWY5YTJlMlwiLFwia2V5X2lkXCI6XCIxXCIsXCJzaWduXCI6XCIxNjE0YTU2MVwifSIsInIiOiJodHRwczovL2d6LmxpYW5qaWEuY29tL2Vyc2hvdWZhbmcvcGc3Y28zMnJzJUU1JUI5JUJGJUU1JUI3JTlFLyIsIm9zIjoid2ViIiwidiI6IjAuMSJ9; Hm_lpvt_9152f8221cb6243a53c83b956842be8a=1644805443; f-token=ybhZaq9CZ5OJx/PSq0NggKV2TEsAiqSOmEEJicbdIayRSfg0mpNyXL6DhWB2oGMNShan9lnFmgGX0REF+ad6TKDWoSeYqVcP6hBYn/THdnKhO0uugOH+/mP6vzHfNx2T6ldSxXj4a2hs6okQFJEXlTC6; cy_ip=61.140.170.177; lianjia_ssid=34b1aa41-0d31-4766-8467-98b6f4d9450e; _jzqb=1.1.10.1644805443.1; _qzjb=1.1644805442991.1.0.0.0; _qzjto=1.1.0; _gat=1; _gat_global=1; _gat_new_global=1; _gat_dianpu_agent=1',
        'Upgrade-Insecure-Requests': '1',
        'Cache-Control': 'max-age=0'
        }
items=[]
index=['地址', '地区', '房屋信息', '总价', '每平米单价', '房屋户型', '所在楼层', '建筑面积', '户型结构', '套内面积', '建筑类型', '房屋朝向', '建筑结构', '装修情况', '梯户比例', '配备电梯', '挂牌时间', '交易权属', '上次交易', '房屋用途', '房屋年限', '产权所属', '抵押信息', '房本备件']
for k in range(2,5):
        print(k)
        time.sleep(0.3)
        url='https://gz.lianjia.com/ershoufang/pg{}co32rs%E5%B9%BF%E5%B7%9E/'.format(k)
        res=rs.get(url,headers)
        soup=bs(res.text,'html.parser')
        info=soup.find('ul',attrs={'class':"sellListContent"})
        info_list=info.find_all(attrs={'class':'info clear'})
        for num in range(len(info_list)):#
                ar=info_list[num].contents[1].find_all('a')
                item=[]
                print('{}:{}'.format(k,num))
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

for i in range(0,25):
	print('{}:{}'.format(index[i],items[0][i]))

s=pd.DataFrame(items,columns=index)
s.to_csv('data4.csv',encoding='utf_8_sig',index=False)
''' 


def gen_news():
    info=gen_cctv()
    items=[]
    for i in range(20):
        items.append(info['cardgroups'][i]['cards'][0]['title'])
    s=pd.DataFrame(items,columns=['text'])
    s.to_excel('cctvt.xlsx',encoding='utf_8_sig',index=False)


def trans(sen):
    url='https://fanyi.baidu.com/transapi'
    headers={
            'Host': 'fanyi.baidu.com',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:64.0) Gecko/20100101 Firefox/64.0',
            'Accept': '*/*',
            'Accept-Language': 'zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2',
            'Accept-Encoding': 'gzip, deflate, br',
            'Referer': 'https://fanyi.baidu.com/?aldtype=16047',
            'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
            'X-Requested-With': 'XMLHttpRequest',
            'Content-Length': '149',
            'Connection': 'keep-alive',
            'Cookie': 'BIDUPSID=6BE677652E430978CA842C507962F903; PSTM=1546257104; REALTIME_TRANS_SWITCH=1; FANYI_WORD_SWITCH=1; HISTORY_SWITCH=1; SOUND_SPD_SWITCH=1; SOUND_PREFER_SWITCH=1; Hm_lvt_64ecd82404c51e03dc91cb9e8c025574=1646188010; BAIDUID=FF36BC5AE675AA11C6DBE2DC67901CF9:FG=1; BDUSS=U16djhaRVREdC04VFMtNmMycjJQfkRRaVQzYXNmU3c2eX5KNFRPTjVpeE8zVzFmSVFBQUFBJCQAAAAAAAAAAAEAAAAmX5QwY3k1MjB6eTEwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAE5QRl9OUEZfL; __yjs_duid=1_01f003a45057bbcae8e688c9d209cd081617933423287; MCITY=-%3A; BDORZ=FFFB88E999055A3F8A630C64834BD6D0; BDSFRCVID=gVFOJexroG0v0WnDy4Q-ulTyTwaDUYjTDYLtOwXPsp3LGJLVgaqOEG0PtEN4CutbVLvtogKK3gOTH4DF_2uxOjjg8UtVJeC6EG0Ptf8g0M5; H_BDCLCKID_SF=tJPH_K_KtCI3fP36q4oWht_th2cDbC62Kb39WKnvWJ5Tfp6-Df6O0p0n24RJJJ3GMT6B0lkaQRboShPC-tPM0hLVjlOKXU5A-ecxKCoG3l02V569e-t2ynLVMbof-PRMW20e0h7mWIbUsxA45J7cM4IseboJLfT-0bc4KKJxbnLWeIJIjjCKjTvBja8tJ6nJ-D6206uatRcoH6rnhPF32MKTXP6-35KHaC_LWprJ3poIOqjd-xQoLPuj-4tHth37JD6yLCQ7B-JAOPbbDf7EjnLr24oxJpO7QRbMopvaKf-hDqQvbURvDP-g3-AJ0U5dtjTO2bc_5KnlfMQ_bf--QfbQ0hOhqP-jBRIEoK0hJC-2bKvPKITD-tFO5eT22-usbRKj2hcHMPoosIJ-3M6CQMDdW-JJ3JvrbIviaKJjBMbUoqRHXnJi0btQDPvxBf7p5208Ll5TtUJM_UKzhfoMqfTbMlJyKMnitKv9-pP23pQrh459XP68bTkA5bjZKxtq3mkjbPbDfn028DKuDjtBDTvbjNRabK6aKC5bL6rJabC3e-5oXU6q2bDeQN0JqloZ3N64Lhn20tnafJ5oyT3JXp0vWtvJWbbvLT7johRTWqR4ep6S0UonDh83KUut0-JtHCOO_hOO5hvvhn3O3MAMQMKmDloOW-TB5bbPLUQF5l8-sq0x0bOte-bQXH_EJ6-8JRIqVCDQKt8_HRjYbb__-P4DeUJp0fRZ56bHWh0MbDJRDlbwjhLV5tA72JOf5x3PyCQnKUT1bp7boMJRK5bdQUIT3xJKbxR43bRTLp5kJpOhfboKXbjMhP-UyNbMWh37JgnlMKoaMp78jR093JO4y4Ldj4oxJpOJ5JbMopCafJOKHIC9e5Kh3e; H_PS_PSSID=31254_26350; delPer=0; PSINO=7; BDRCVFR[bOqe_OrD6-R]=mk3SLVN4HKm; BDRCVFR[S4-dAuiWMmn]=-iuku57F9iDfjDdnj0LPjDYg1DLgvwM; BDRCVFR[feWj1Vr5u3D]=mk3SLVN4HKm; BA_HECTOR=0h24a00421a18k05gq1h1tmch0r; Hm_lpvt_64ecd82404c51e03dc91cb9e8c025574=1646190257; APPGUIDE_10_0_2=1; ab_sr=1.0.1_YWQ0NjIzMmUyZDY4MDgyNWVhMjg3OTkzZWQ1ZjY5MDNjMDE2ZjNkM2Y1ODFmMGY1YjZhMTRjYjJlN2M0ZGEzYjllZTZmZjZkZDBlYzc0YzE3MjdlMTRhNWYzODlmNTllOTEzMDI2NjU1ZDVlOWIxMjJmNDI1NjhiOGVmMzgxMDhkZThiNTViNjhkNzIxM2Y2MjhmNDI4MWE0YjhmNTY0ZjU4MDIxMTY2ZjU1YWY3NjhjMDBiNDAwMmM4NmU1NjYx',
            'Pragma': 'no-cache',
            'Cache-Control': 'no-cache',
            }
    params={
            'from':'zh',
            'to':'en',
            'query':'{}'.format(sen),
            'source':'txt'
            }
    
    res=rs.post(url,headers=headers,data=params,timeout=10)
    
    if json.loads(res.text)['type']==1:
        h=json.loads(json.loads(res.text)['result'])
        en=list(h['content'][0]['mean'][0]['cont'].keys())[0]
    else:
        en=json.loads(res.text)['data'][0]['dst']
    
    params1={
            'from':'en',
            'to':'zh',
            'query':'{}'.format(en),
            'source':'txt'
            }
    res=rs.post(url,headers=headers,data=params1,timeout=10)
    js=json.loads(res.text)
    if js['type']==1:
        h=json.loads(js['result'])
        zh=list(h['content'][0]['mean'][0]['cont'].keys())[0]
    else:
        zh=js['data'][0]['dst']
    return zh 

'''
for i in range(len(conl)):
    print(i)
    
    cn = trans(conl[i])
    
    contents.append([cn,labels[i]])
    time.sleep(1)
s.append(pd.DataFrame(contents,columns=['text','label']),ignore_index=True)
s.to_csv('estrans.csv',encoding='utf_8_sig',index=False)
ans=trans('早上的阳光')
'''
def gen_vote():
    
    headers={
            'Host': 'vote.eastmoney.com',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:64.0) Gecko/20100101 Firefox/64.0',
            'Accept': 'application/json, text/javascript, */*; q=0.01',
            'Accept-Language': 'zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2',
            'Accept-Encoding': 'gzip, deflate, br',
            'Referer': 'https://vote.eastmoney.com/',
            'X-Requested-With': 'XMLHttpRequest',
            'Connection': 'keep-alive',
            'Cookie': 'qgqp_b_id=c5c2334bec2a996e37712ec8d49d7fd3; HAList=ty-1-000300-%u6CAA%u6DF1300%2Ca-sh-603899-%u6668%u5149%u6587%u5177; em_hq_fls=js; intellpositionL=1228.8px; intellpositionT=1157.4px; st_si=08865665378903; st_sn=17; st_psi=20220318214502603-0-0910974423; st_asi=delete; st_pvi=73808207229163; st_sp=2020-04-24%2014%3A51%3A04; st_inirUrl=https%3A%2F%2Fwww.baidu.com%2Flink',
            'Cache-Control': 'max-age=0, no-cache',
            'Pragma': 'no-cache',
            }
    url='https://vote.eastmoney.com/voteapi/Handlers/VoteResultHistoryHandler.ashx?PageSize=51&PageIndex=1'
    res=rs.get(url,headers=headers,timeout=10)
    j=json.loads(res.text)#['re'][0]['post_content']
    votels=j['VoteResults']
    items=[]
    for i in range(len(votels)):
        date=votels[i]['VoteDate']
        for j in ['FallCount','RiseCount','ConsolidationCount']:
            ty=''
            if j=='FallCount':
                ty='看跌'
            if j=='RiseCount':
                ty='看多'
            if j=='ConsolidationCount':
                ty='看平'
            items.append([date,ty,votels[i][j]])
        #items.append([votels[i]['VoteDate'],votels[i]['FallCount'],votels[i]['RiseCount'],votels[i]['ConsolidationCount']])
    index=['日期','类型','票数']#,'看空','看涨','看平'
    s=pd.DataFrame(items,columns=index)
    s.to_excel('vote.xlsx',encoding='utf_8_sig',index=False)
def updown_count(): 
    url='https://datacenter.eastmoney.com/securities/api/data/get?type=RPTAAA_DMSK_TS_CHANGESTATISTICS&?v=07713253295193976'
    res=rs.get(url,timeout=10)
    j=json.loads(res.text)
    dic=j['result']['data'][0]
    index=['类型','数量']
    items=[]
    t=['上涨','下跌','涨停','自然涨停','跌停','自然跌停','跌5%以上','跌1%-5%','跌0%-1%','平盘','涨0%-1%','涨1%-5%','涨5%以上']
    for i,p in enumerate(dic.items()):
        items.append([t[i],p[1]])
    s=pd.DataFrame(items,columns=index)
    s.to_excel('updown_count.xlsx',encoding='utf_8_sig',index=False)
