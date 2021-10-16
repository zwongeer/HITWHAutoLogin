import requests

import hitwh
import aiohttp
from hitwh.config import auth_url

async def logout(session : aiohttp.ClientSession):
    if session is None:
        return
    await session.get(f"{auth_url}/authserver/logout?service=/authserver/login")