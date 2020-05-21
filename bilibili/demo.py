# -*- coding: utf-8 -*-
"""
Spyder 编辑器

这是一个临时脚本文件。
"""
import requests,json,time,pymysql,xlwt



def getCommnet(pn):
    headers = {
        "authority": "api.bilibili.com",
        "method": "GET",
        "path": ":/x/v2/reply?type=1&oid=412935552&pn=%s"%pn,
        "scheme": "https",
        "accept":"*/*",
        "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
        "accept-encoding": "gzip, deflate, br",
        "accept-language": "zh-CN,zh;q=0.9",
        "cache-control":"max-age=0",
        "cookie": "_uuid=75E28C81-06B5-568E-86DF-87B5487A6EBE57282infoc; buvid3=637156B6-16FE-457D-93BB-5DBE7C91AAA353944infoc; CURRENT_FNVAL=16; LIVE_BUVID=AUTO4915870149023840; rpdid=|(k|ulYm|kmR0J'ul)~|uRm|l; DedeUserID=472541590; DedeUserID__ckMd5=a59a63be8b1829b8; SESSDATA=c8c0e7b0%2C1602566951%2C079f2*41; bili_jct=306da5325b9fe1d6341df6faba7a8612; CURRENT_QUALITY=80; bfe_id=393becc67cde8e85697ff111d724b3c8",
        "referer": "https://www.bilibili.com/video/BV1FV411d7u7",
        "sec-fetch-dest": "document",
        "sec-fetch-mode": "navigate",
        "sec-fetch-site": "none",
        "sec-fetch-user":"?1",
        "user-agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36"
        }
    params = {
        "pn": "%s"%pn,
        "type": "1",
        "oid": "412935552",
        
        }
    url = 'https://api.bilibili.com/x/v2/reply?type=1&oid=412935552&pn=%s'%pn

    r = requests.get(url,headers=headers,params=params)
    
    
   # with open('E:\\anaconda3\\demo\\result.txt',r'a+') as my:
      #  my.write(str(r.content))
        
    return r.content

def analyseCommet(comment):
    
    comment = json.loads(comment)#b'jQuery1720697274841346351_1589443585657
   # print (comment)
    for i in range(20):
        try:
            mid = comment['data']['replies'][i]['mid']
        except:
            mid = 'error'
        try:
            like = comment['data']['replies'][i]['like']
        except:
            like = 'error'
        try:
            uname = comment['data']['replies'][i]['member']['uname']
        except:
            uname = 'error'
        try:
            sex = comment['data']['replies'][i]['member']['sex']
        except:
            sex = 'error'
        try:
            sign = comment['data']['replies'][i]['member']['sign']
        except:
            sign = 'error'
        try:
            rank = comment['data']['replies'][i]['member']['rank']
        except:
            rank = 'error'
        try:
            current_level = comment['data']['replies'][i]['member']['level_info']['current_level']
        except:
            current_level = 'error'
        try:
            viptype = comment['data']['replies'][i]['member']['vip']['vipType']
        except:
            viptype = 'error'
            #vipDueDate = comment['data']['replies'][i]['member']['vip']['vipDueDate']
        try:
            message = comment['data']['replies'][i]['content']['message']
            #print (measage)
        except:
            message = 'error'
        #f.wrtie()
        
        
        with conn:
            cur = conn.cursor()
            #print (data[0],data[1],data[2],data[3],data[4],data[5],data[6],data[7],data[8])
            #sql = "insert into t_bilibili (mid,like,uname,sex,sign,rank,current_level,viptype,message) values('%s','%s','%s','%s','%s','%s','%s','%s','%s');" %(data[0],data[1],data[2],data[3],data[4],data[5],data[6],data[7],data[8])
            #sql = "insert into t_bilibili (mid,like,uname,sex,sign,rank,current_level,viptype,message) values('%s','%s','%s','%s','%s','%s','%s','%s','%s');" %(mid,like,uname,sex,sign,rank,current_level,viptype,message)
            try:
                sql = '''insert into t_bilibili values("%s","%s","%s","%s","%s","%s","%s","%s","%s");''' %(mid,like,pymysql.escape_string(uname),sex,sign,rank,current_level,viptype,pymysql.escape_string(message))
                cur.execute(sql)
                conn.commit()  
            except:
                print ('insert error')

       
        #return mid,like,uname,sex,sign,rank,current_level,viptype,message
        

    

def main():
    #52965/20
    for i in range(1700,2701):
        data = getCommnet(i)
        analyseCommet(data)
        time.sleep(0.5)
        print (i)
        #break
   
    

if __name__ == '__main__':
    conn = pymysql.connect('localhost','root','','d_bilibili',charset='utf8')
    f = open('result.txt',r'a+')
    
    main()
    
    conn.close()
    f.close()
    
