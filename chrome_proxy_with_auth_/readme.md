# python + Selenium 给 chrome 设置需认证的代理

## 不需要认证的代理
使用 Selenium 给 chrome 设置不需要认证的代理很简单，如下
``` python
chromeOptions = webdriver.ChromeOptions()
chromeOptions.add_argument('--proxy-server=http://ip:port')  
driver = webdriver.Chrome(chrome_options=chromeOptions)
```

## 需要认证的代理
需要认证的代理设置起来就有些麻烦了，经过一番搜索，找到了一份可行的方案，特此做个记录。
该方案的主要思路是 动态生成一个绑定代理及认证信息的 chrome 代理插件并在浏览器启动时启用，具体实现见 [chrome_proxy_with_auth.py](
chrome_proxy_with_auth_/chrome_proxy_with_auth.py)
