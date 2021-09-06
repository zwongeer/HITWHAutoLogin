## HITWHAutoLogin

`HITWHAutoLogin`可以用来自动完成统一身份认证的登录，可以获取一个登录了的`requests.Session`，可以用来进行各种操作，~~比如在教务系统退课~~。

### 样例
`main.py`实现了一个查询学分绩的功能

### 如何运行

首先安装pipenv

```
pip install pipenv
```

#### 使用
使用前请先创建一个account.json文件，用来存储登录的学号和密码，例如
```
{
	"username" : "198forest",
	"password" : "123456"
}
```

```bash
pipenv install
pipenv run main.py
```
#### 移除虚拟环境

```
pipenv --rm
```

### Notes

- 在使用教务系统前需要执行`session.get("http://jwts.hitwh.edu.cn/loginCAS")`以使用统一身份认证登录教务系统
- `hitwh.auth.logout`仅会退出统一身份认证，但不会退出教务系统
- 要退出教务系统，应该使用`session.get("http://172.26.64.16/logout")`

### 自定义配置

在调用之前可以修改全局变量来自定义配置

```python
import hitwh

# 是否选择一周内免登录
hitwh.config.rememberMe = "on"

# 自定义请求域名（最后不加'/'）
hitwh.config.auth_url = "http://authserver.hitwh.edu.cn"

# 自定义请求头
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
```

### TODO

- [ ] Session保存和加载
- [ ] 从浏览器获取登录后的Session

### See Also
[hitutil](https://github.com/billchenchina/hitutil)

