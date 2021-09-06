import random
import re
import requests

from bs4 import BeautifulSoup

import hitwh
from hitwh.config import auth_url
from hitwh.utils import get_random_string, HITWH_LoginError

def isloggedin(session : requests.Session) -> bool:
    response = session.get(f"{auth_url}/authserver/index.do")
    return response.status_code == 200

def login(username : str, passwd : str) -> requests.Session:
    session = requests.Session()
    # use custom headers
    session.headers.update(hitwh.config.request_headers)

    response = session.get(f"{auth_url}/authserver/login")

    # the parameter in the JS file
    pwdDefaultEncryptSalt = re.search(r'var pwdDefaultEncryptSalt = "(.*?)";', response.text).groups()[0]

    encryptedPasswd = hitwh.utils.getEncryptedpasswd(passwd, pwdDefaultEncryptSalt)
    soup = BeautifulSoup(response.text, 'html.parser')
    r = session.post(response.url, data={
        "username": username,
        "password": encryptedPasswd,
        "rememberMe": hitwh.config.rememberMe,
        "lt": soup.find('input', {'name': 'lt'})['value'],
        "dllt": soup.find('input', {'name': 'dllt'})['value'],
        "execution": soup.find('input', {'name': 'execution'})['value'],
        "_eventId": soup.find('input', {'name': '_eventId'})['value'],
        "rmShown": soup.find('input', {'name': 'rmShown'})['value']
    })

    if isloggedin(session):
        return session
    raise HITWH_LoginError("Login failed")