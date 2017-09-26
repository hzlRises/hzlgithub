#! /usr/bin/env python
  
import requests
import json
  
def get_token():
  
  url='https://qyapi.weixin.qq.com/cgi-bin/gettoken'
  values = {'corpid' : '00000' ,
      'corpsecret':'00000',
       }
  req = requests.post(url, params=values)  
  data = json.loads(req.content)
  print data
  return data["access_token"]
  
def send_msg():
  url="https://qyapi.weixin.qq.com/cgi-bin/message/send?access_token="+get_token()
  values = """{"touser" : "00000",
      "msgtype" :"text",
      "agentid":"00000",
      "text":{
        "content": "dd"
      },
      "safe":0
      }""" 
   
  data = json.loads(values) 
  req = requests.post(url, params=values) 
  print req.content
  
if __name__ == '__main__':
  send_msg()
