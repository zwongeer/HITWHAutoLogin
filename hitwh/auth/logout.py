import requests

import hitwh
from hitwh.config import auth_url

def logout(session : requests.Session):
    if session is None:
        return
    session.get(f"{auth_url}/authserver/logout?service=/authserver/login")