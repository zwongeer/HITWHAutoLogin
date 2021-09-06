import json

import hitwh
from hitwh.auth import *

hitwh.config.request_headers = {
    'Connection': 'keep-alive',
    'Cache-Control': 'max-age=0',
    'Upgrade-Insecure-Requests': '1',
    # Chrome
    #'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Safari/537.36',
    # Firefox
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:91.0) Gecko/20100101 Firefox/91.0',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'Accept-Language': 'zh-CN,zh;q=0.8,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2'
}

if __name__ == "__main__":
    data = json.load(open('account.json'))
    session = login(data["username"], data["password"])
    
    session.get("http://jwts.hitwh.edu.cn/loginCAS")
    response = session.get("http://172.26.64.16/xfj/queryListXfj")
    print(response.text)
    session.get("http://172.26.64.16/logout")
    logout(session)