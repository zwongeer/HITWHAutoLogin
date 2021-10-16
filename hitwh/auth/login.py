import random
import re
#import requests
import aiohttp


from bs4 import BeautifulSoup

import hitwh
from hitwh.config import auth_url
from hitwh.utils import get_random_string, HITWH_LoginError

async def isloggedin(session : aiohttp.ClientSession) -> bool:
    # response = await session.get(f"{auth_url}/authserver/index.do")
    # return str(response.url) == f"{auth_url}/authserver/index.do"
    return True

async def login(username : str, passwd : str) -> aiohttp.ClientSession:
    session = aiohttp.ClientSession()
    # use custom headers
    session.headers.update(hitwh.config.request_headers)

    response = await session.get(f"{auth_url}/authserver/login")

    # the parameter in the JS file
    response_text = await response.text()
    pwdDefaultEncryptSalt = re.search(r'var pwdDefaultEncryptSalt = "(.*?)";', response_text).groups()[0]
    
    encryptedPasswd = hitwh.utils.getEncryptedpasswd(passwd, pwdDefaultEncryptSalt)
    soup = BeautifulSoup(response_text, 'html.parser')
    cookies = session.cookie_jar.filter_cookies(f"{auth_url}")
    custom_headers = session.headers
    custom_headers["Content-Type"] = "application/x-www-form-urlencoded"
    from urllib.parse import urlencode
    data_dict = dict({
        "username": username,
        "password": encryptedPasswd,
        "rememberMe": hitwh.config.rememberMe,
        "lt": soup.find('input', {'name': 'lt'})['value'],
        "dllt": soup.find('input', {'name': 'dllt'})['value'],
        "execution": soup.find('input', {'name': 'execution'})['value'],
        "_eventId": soup.find('input', {'name': '_eventId'})['value'],
        "rmShown": soup.find('input', {'name': 'rmShown'})['value']
    })
    print(urlencode(data_dict))
    r = await session.post(str(response.url), data=urlencode(data_dict), headers=custom_headers)

    if await isloggedin(session):
        return session
    raise HITWH_LoginError("Login failed")