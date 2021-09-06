import base64
import random

def get_random_string(length : int, letters : str = None) -> str:
    if letters is None:
        # from http://authserver.hitwh.edu.cn/authserver/custom/js/encrypt/encrypt.wisedu.js (line 25)
        letters = "ABCDEFGHJKMNPQRSTWXYZabcdefhijkmnprstwxyz2345678"
    return ''.join(random.choice(letters) for i in range(length))

def encrypt(data : bytes, key : bytes, block_size : int) -> bytes:
    from Crypto.Util.Padding import pad
    from Crypto.Cipher import AES
    iv = get_random_string(16).encode()
    cipher = AES.new(key, AES.MODE_CBC, iv)
    ct = cipher.encrypt(pad(data, block_size))
    return base64.b64encode(ct)

def getEncryptedpasswd(passwd : str, salt : str) -> str:
    # something weird, please the these scripts
    """
    http://authserver.hitwh.edu.cn/authserver/custom/js/encrypt/encrypt.wisedu.js
    http://authserver.hitwh.edu.cn/authserver/custom/js/login.js
    http://authserver.hitwh.edu.cn/authserver/custom/js/login-wisedu_v1.0.js
    """
    # the default block size is 16 (in login-wisedu_v1.0.js)
    # use string.encode to convert string to bytes
    # see function encryptAES in file encrypt.wisedu.js (line 17)
    return encrypt((get_random_string(64) + passwd).encode(), salt.encode(), 16)


class HITWH_LoginError(Exception):
    def __init__(self, info : str):
        super().__init__(self)
        self.errorinfo = info
    def __str__(self):
        return f"{self.__name__}:{self.errorinfo}"