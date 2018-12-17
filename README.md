# python_spider
python爬虫入门级案例,+扣849962874
# Urllib基础
1. urlopen()

    在python2.x版本中可以直接使用import urllib来进行操作，但是python3.x版本中使用的是import urllib.request来进行操作

    ```
    from urllib import request
    
    with request.urlopen('http://localhost:8080/spider-test.html') as f:
        data = f.read()
        #f.status 状态码，f.reason 
        print('Status:', f.status, f.reason) #Status: 200 OK
        for k, v in f.getheaders():
            print('%s: %s' % (k, v))
        print('Data:', data.decode('utf-8'))
    ```

       

2. get请求

    如果我们要想模拟浏览器发送GET请求，就需要使用Request对象，通过往Request对象添加HTTP头，我们就可以把请求伪装成浏览器。
     >浏览器 就是互联网世界上公认被允许的身份，如果我们希望我们的爬虫程序更像一个真实用户，那我们第一步，就是需要伪装成一个被公认的浏览器。用不同的浏览器在发送请求的时候，会有不同的User-Agent头。 urllib2默认的User-Agent头为：Python-urllib/x.y（x和y是Python主版本和次版本号,例如 Python-urllib/3.6）

    ```
    from urllib import request
    
    req = request.Request('http://localhost:8080/spider-test.html')
    req.add_header('User-Agent', 'Mozilla/6.0 (iPhone; CPU iPhone OS 8_0 like Mac OS X) AppleWebKit/536.26 (KHTML, like Gecko) Version/8.0 Mobile/10A5376e Safari/8536.25')
    with request.urlopen(req) as f:
        print('Status:', f.status, f.reason)
        for k, v in f.getheaders():
            print('%s: %s' % (k, v))
        print('Data:', f.read().decode('utf-8'))
    ```

3. 随机添加/修改User-Agent

   ​	from urllib import request
   ​	import random

   	#IE 9.0 的 User-Agent，包含在 ua_header里
   	
   	ua_list = [
   	    "Mozilla/5.0 (Windows NT 6.1; ) Apple.... ",
   	    "Mozilla/5.0 (X11; CrOS i686 2268.111.0)... ",
   	    "Mozilla/5.0 (Macintosh; U; PPC Mac OS X.... ",
   	    "Mozilla/5.0 (Macintosh; Intel Mac OS... "
   	]
   	
   	user_agent = random.choice(ua_list)
   			
   	ua_header = {"User-Agent" : user_agent}
   	
   	req=request.Request(url,headers=ua_header)
   	#获得请求方法 get
   	print(req.get_method())
   	#获取请求url
   	print(req.get_full_url())
   	
   	with request.urlopen(req) as f:
   	    data = f.read()
   	    print('Status:', f.status, f.reason)
   	    for k, v in f.getheaders():
   	        print('%s: %s' % (k, v))
   	    print('Data:', data.decode('utf-8'))

4. get提交数据-urlencode()

   ```
   from urllib import request,parse
   
   #当前urllib放在在parse模块中
   query={"q":"python","id":"001"}
   query=parse.urlencode(query)
   ...
   url='http://www.bootcss.com/'+'?'+query
   ```


5. 案例：批量爬取淘宝数据

  **解决https无法爬取的问题**

  	import ssl
  	ssl._create_default_https_context = ssl._create_unverified_context
  	
  	#解决url中有中文的问题
  	from urllib import parse
  	import string
  	url='https://s.taobao.com/search?q=手机&imgfile=&commend=all&ssid=s5-e&search_type=item&sourceId=tb.index&spm=a21bo.2017.201856-taobao-item.1&ie=utf8&initiative_id=' \
  	        'tbindexz_20170306&p4ppushleft=5%2C48&'
  	
  	url=parse.quote(url,safe=string.printable)


  ​	
  	print(url)

    	url = "https://s.taobao.com/list?spm=a217f.8051907.312344.2.7e383308OlmjDv&q=T%E6%81%A4&cat=16&seller_type=taobao&oetag=6745&source=qiangdiao&bcoffset=12&"

3. post请求

    如果要以POST发送一个请求，只需要把参数data以bytes形式传入。

    我们模拟一个微博登录，先读取登录的邮箱和口令，然后按照weibo.cn的登录页的格式以username=xxx&password=xxx的编码传入：
    
    ```
    from urllib import request, parse

    print('Login to weibo.cn...')
    email = input('Email: ')
    passwd = input('Password: ')
    login_data = parse.urlencode([
        ('username', email),
        ('password', passwd),
        ('entry', 'mweibo'),
        ('client_id', ''),
        ('savestate', '1'),
        ('ec', ''),
        ('pagerefer', 'https://passport.weibo.cn/signin/welcome?entry=mweibo&r=http%3A%2F%2Fm.weibo.cn%2F')
    ])
    
    req = request.Request('https://passport.weibo.cn/sso/login')
    req.add_header('Origin', 'https://passport.weibo.cn')
    req.add_header('User-Agent', 'Mozilla/6.0 (iPhone; CPU iPhone OS 8_0 like Mac OS X) AppleWebKit/536.26 (KHTML, like Gecko) Version/8.0 Mobile/10A5376e Safari/8536.25')
    req.add_header('Referer', 'https://passport.weibo.cn/signin/login?entry=mweibo&res=wel&wm=3349&r=http%3A%2F%2Fm.weibo.cn%2F')
    
    with request.urlopen(req, data=login_data.encode('utf-8')) as f:
        print('Status:', f.status, f.reason)
        for k, v in f.getheaders():
            print('%s: %s' % (k, v))
        print('Data:', f.read().decode('utf-8'))
    ```
    
    >关于user-agent
    >http://www.fynas.com/ua
    
7. AJAX请求json数据

  如果网站采用c/s模式，那么页面数据是返回json这个时候，我们要找到该页面后台接口地址，然后手动去爬取数据。

  具体查看数据方式为：chrome-->检查->network-->找到json文件（可以根据页面内容利用左面的搜索框搜索哦）-->点击右面的preview预览-->点击右面的headers查看地址然后给爬虫爬取。
  ajax请求数据都是XMLHttpRequest对象请求的，我们可以直接通过XHR筛选出文件（search_subjects?type.....）

  	from urllib import request,parse
  		import urllib
  		import ssl
  		ssl._create_default_https_context = ssl._create_unverified_context
  	# url = "https://movie.douban.com/j/chart/top_list?type=11&interval_id=100%3A90&action"
  	# https://movie.douban.com/j/search_subjects?type=tv&tag=%E7%83%AD%E9%97%A8&sort=recommend&page_limit=20&page_start=0
  	url='https://movie.douban.com/j/search_subjects?type=movie&tag=%E7%' \
  	    '83%AD%E9%97%A8&sort=recommend&'
  	headers={"User-Agent": "Mozilla...."}
  	
  	# 变动的是这两个参数，从start开始往后显示limit个
  	formdata = {
  	    'page_limit':20,
  	    'page_start':20*8
  	}
  	data = parse.urlencode(formdata).encode()
  	
  	url=url+data.decode()
  	
  	req = request.Request(url, headers = headers)
  	
  	response = request.urlopen(req)
  	
  	print(response.read().decode())

4. handler

    ```
    from urllib import request
    from urllib.error import URLError
    
    
    password_mgr = request.HTTPPasswordMgrWithDefaultRealm()
    top_level_url = 'http://localhost:8080/users/login'
    req = request.Request(top_level_url)
    try:
        # 创建一个密码管理者
        # 如果知道 realm, 我们可以使用他代替 ``None``.
        # password_mgr.add_password(None, top_level_url, username, password)
        password_mgr.add_password(None, top_level_url, '13812790421', '123456')
    
        # 创建了一个新的handler
        handler = request.HTTPBasicAuthHandler(password_mgr)
    
        # 创建 "opener" (OpenerDirector 实例)
        opener = request.build_opener(handler)
        a_url ='http://localhost:8080/users/getAllUsers'
    
        # 使用 opener 获取一个URL
        response =opener.open(a_url)
    
        # 安装 opener.
        # 现在所有调用 urllib2.urlopen 将用我们的 opener.
        urllib.install_opener(opener)
    except URLError as e:
        if hasattr(e, 'code'):
            print ('The server couldn\'t fulfill the request.')
            print ('Error code: ', e.code)
        elif hasattr(e, 'reason'):
            print ('We failed to reach a server.')
            print ('Reason: ', e.reason())
        else:
            print (response.read())

    ```


5. 异常处理

	URLError 产生的原因主要有：

	* 没有网络连接
	* 服务器连接失败
	* 找不到指定的服务器

	HTTPError
	
	HTTPError是URLError的子类，我们发出一个请求时，服务器上都会对应一个response应答对象，其中它包含一个数字"响应状态码"。

	如果urlopen或opener.open不能处理的，会产生一个HTTPError，对应相应的状态码，	HTTP状态码表示HTTP协议所返回的响应的状态。

	注意，urllib2可以为我们处理重定向的页面（也就是3开头的响应码），100-299范围的	号码表示成功，所以我们只能看到400-599的错误号码。
	
		try:
		    pass
		except error.HTTPError as err:
		    pass
		except error.URLError as err:
		    pass
		except Exception as err:
		    pass

6. HTTP响应状态码参考：

   1xx:信息
   ​	
   ​	100 Continue
   ​	服务器仅接收到部分请求，但是一旦服务器并没有拒绝该请求，客户端应该继续发送其余的请求。
   ​	101 Switching Protocols
   ​	服务器转换协议：服务器将遵从客户的请求转换到另外一种协议。


   ​	
   ​	
   	2xx:成功
   	
   	200 OK
   	请求成功（其后是对GET和POST请求的应答文档）
   	201 Created
   	请求被创建完成，同时新的资源被创建。
   	202 Accepted
   	供处理的请求已被接受，但是处理未完成。
   	203 Non-authoritative Information
   	文档已经正常地返回，但一些应答头可能不正确，因为使用的是文档的拷贝。
   	204 No Content
   	没有新文档。浏览器应该继续显示原来的文档。如果用户定期地刷新页面，而Servlet可以确定用户文档足够新，这个状态代码是很有用的。
   	205 Reset Content
   	没有新文档。但浏览器应该重置它所显示的内容。用来强制浏览器清除表单输入内容。
   	206 Partial Content
   	客户发送了一个带有Range头的GET请求，服务器完成了它。


   ​	
   ​	
   	3xx:重定向
   	
   	300 Multiple Choices
   	多重选择。链接列表。用户可以选择某链接到达目的地。最多允许五个地址。
   	301 Moved Permanently
   	所请求的页面已经转移至新的url。
   	302 Moved Temporarily
   	所请求的页面已经临时转移至新的url。
   	303 See Other
   	所请求的页面可在别的url下被找到。
   	304 Not Modified
   	未按预期修改文档。客户端有缓冲的文档并发出了一个条件性的请求（一般是提供If-Modified-Since头表示客户只想比指定日期更新的文档）。服务器告诉客户，原来缓冲的文档还可以继续使用。
   	305 Use Proxy
   	客户请求的文档应该通过Location头所指明的代理服务器提取。
   	306 Unused
   	此代码被用于前一版本。目前已不再使用，但是代码依然被保留。
   	307 Temporary Redirect
   	被请求的页面已经临时移至新的url。


   ​	
   ​	
   	4xx:客户端错误
   	
   	400 Bad Request
   	服务器未能理解请求。
   	401 Unauthorized
   	被请求的页面需要用户名和密码。
   	401.1
   	登录失败。
   	401.2
   	服务器配置导致登录失败。
   	401.3
   	由于 ACL 对资源的限制而未获得授权。
   	401.4
   	筛选器授权失败。
   	401.5
   	ISAPI/CGI 应用程序授权失败。
   	401.7
   	访问被 Web 服务器上的 URL 授权策略拒绝。这个错误代码为 IIS 6.0 所专用。
   	402 Payment Required
   	此代码尚无法使用。
   	403 Forbidden
   	对被请求页面的访问被禁止。
   	403.1
   	执行访问被禁止。
   	403.2
   	读访问被禁止。
   	403.3
   	写访问被禁止。
   	403.4
   	要求 SSL。
   	403.5
   	要求 SSL 128。
   	403.6
   	IP 地址被拒绝。
   	403.7
   	要求客户端证书。
   	403.8
   	站点访问被拒绝。
   	403.9
   	用户数过多。
   	403.10
   	配置无效。
   	403.11
   	密码更改。
   	403.12
   	拒绝访问映射表。
   	403.13
   	客户端证书被吊销。
   	403.14
   	拒绝目录列表。
   	403.15
   	超出客户端访问许可。
   	403.16
   	客户端证书不受信任或无效。
   	403.17
   	客户端证书已过期或尚未生效。
   	403.18
   	在当前的应用程序池中不能执行所请求的 URL。这个错误代码为 IIS 6.0 所专用。
   	403.19
   	不能为这个应用程序池中的客户端执行 CGI。这个错误代码为 IIS 6.0 所专用。
   	403.20
   	Passport 登录失败。这个错误代码为 IIS 6.0 所专用。
   	404 Not Found
   	服务器无法找到被请求的页面。
   	404.0
   	没有找到文件或目录。
   	404.1
   	无法在所请求的端口上访问 Web 站点。
   	404.2
   	Web 服务扩展锁定策略阻止本请求。
   	404.3
   	MIME 映射策略阻止本请求。
   	405 Method Not Allowed
   	请求中指定的方法不被允许。
   	406 Not Acceptable
   	服务器生成的响应无法被客户端所接受。
   	407 Proxy Authentication Required
   	用户必须首先使用代理服务器进行验证，这样请求才会被处理。
   	408 Request Timeout
   	请求超出了服务器的等待时间。
   	409 Conflict
   	由于冲突，请求无法被完成。
   	410 Gone
   	被请求的页面不可用。
   	411 Length Required
   	"Content-Length" 未被定义。如果无此内容，服务器不会接受请求。
   	412 Precondition Failed
   	请求中的前提条件被服务器评估为失败。
   	413 Request Entity Too Large
   	由于所请求的实体的太大，服务器不会接受请求。
   	414 Request-url Too Long
   	由于url太长，服务器不会接受请求。当post请求被转换为带有很长的查询信息的get请求时，就会发生这种情况。
   	415 Unsupported Media Type
   	由于媒介类型不被支持，服务器不会接受请求。
   	416 Requested Range Not Satisfiable
   	服务器不能满足客户在请求中指定的Range头。
   	417 Expectation Failed
   	执行失败。
   	423
   	锁定的错误。


   ​	
   ​	
   	5xx:服务器错误
   	
   	500 Internal Server Error
   	请求未完成。服务器遇到不可预知的情况。
   	500.12
   	应用程序正忙于在 Web 服务器上重新启动。
   	500.13
   	Web 服务器太忙。
   	500.15
   	不允许直接请求 Global.asa。
   	500.16
   	UNC 授权凭据不正确。这个错误代码为 IIS 6.0 所专用。
   	500.18
   	URL 授权存储不能打开。这个错误代码为 IIS 6.0 所专用。
   	500.100
   	内部 ASP 错误。
   	501 Not Implemented
   	请求未完成。服务器不支持所请求的功能。
   	502 Bad Gateway
   	请求未完成。服务器从上游服务器收到一个无效的响应。
   	502.1
   	CGI 应用程序超时。　·
   	502.2
   	CGI 应用程序出错。
   	503 Service Unavailable
   	请求未完成。服务器临时过载或当机。
   	504 Gateway Timeout
   	网关超时。
   	505 HTTP Version Not Supported
   	服务器不支持请求中指明的HTTP协议版本
    # Handler处理器 和 自定义Opener

1. 介绍

  opener是 urllib.OpenerDirector 的实例，我们之前一直都在使用的urlopen，它是一个特殊的opener（也就是模块帮我们构建好的）。

  但是基本的urlopen()方法不支持代理、cookie等其他的HTTP/HTTPS高级功能。所以要支持这些功能：

  使用相关的 Handler处理器 来创建特定功能的处理器对象；
  然后通过 urllib.build_opener()方法使用这些处理器对象，创建自定义opener对象；
  使用自定义的opener对象，调用open()方法发送请求。
  如果程序里所有的请求都使用自定义的opener，可以使用urllib.install_opener() 	将自定义的 opener 对象 定义为 全局opener，表示如果之后凡是调用urlopen，都将使用这个opener（根据自己的需求来选择）

2. 新建opener



   ​	

   	from urllib import request,parse
   	import urllib
   	import ssl
   	ssl._create_default_https_context = ssl._create_unverified_context
   	# 构建一个HTTPHandler 处理器对象，支持处理HTTP请求
   	# http_handler = request.HTTPHandler()
   	
   	# 构建一个HTTPHandler 处理器对象，支持处理HTTPS请求
   	http_handler = request.HTTPSHandler()
   	
   	# 调用request.build_opener()方法，创建支持处理HTTP请求的opener对象
   	opener = request.build_opener(http_handler)
   	
   	url='https://www.liepin.com/sh/zhaopin/pn1/?' \
   	    'd_pageSize=40&siTag=&d_headId=7523ef4c1e412df5e007f3cfd117447d&d_ckId=7523ef4c1e412df5e007f3cfd117447d&d_sfrom=' \
   	    'search_city&'
   	str={
   	    "key":"python",
   	    "d_curPage":0
   	
   	}
   	#
   	url=url+parse.urlencode(str)
   	
   	print(url)
   	# 构建 Request请求
   	request = request.Request(url)
   	
   	# 调用自定义opener对象的open()方法，发送request请求
   	f = opener.open(request)
   	
   	# 获取服务器响应内容
   	with open('liepin.html','w+') as fp:
   	    fp.write(f.read().decode())

   >如果在 HTTPHandler()增加 debuglevel=1参数，还会将 Debug Log 打开，这样程序在执行的时候，会把收包和发包的报头在屏幕上自动打印出来，方便调试，有时可以省去抓包的工作。

   	https_handler = urllib2.HTTPSHandler(debuglevel=1)

3. ProxyHandler处理器（代理设置）

  使用代理IP，这是爬虫/反爬虫的第二大招，通常也是最好用的。

  很多网站会检测某一段时间某个IP的访问次数(通过流量统计，系统日志等)，如果访问次数多的不像正常人，它会禁止这个IP的访问。

  所以我们可以设置一些代理服务器，每隔一段时间换一个代理，就算IP被禁止，依然可以换个IP继续爬取。

  免费的开放代理获取基本没有成本，我们可以在一些代理网站上收集这些免费代理，测试后如果可以用，就把它收集起来用在爬虫上面。

  免费短期代理网站举例：

  [西刺免费代理IP](http://www.xicidaili.com/)

  [快代理免费代理](http://www.kuaidaili.com/free/inha/)

  [Proxy360代理](http://www.proxy360.cn/default.aspx)

  [全网代理IP](http://www.goubanjia.com/free/index.shtml)


  **新建代理opener**

  	from urllib import request,parse
  	import urllib
  	import ssl
  	ssl._create_default_https_context = ssl._create_unverified_context
  	
  	# 构建了两个代理Handler，一个有代理IP，一个没有代理IP
  	httpproxy_handler = request.ProxyHandler({"http" : "110.73.1.105:8123"})
  	nullproxy_handler = request.ProxyHandler({})
  	
  	proxySwitch = True #定义一个代理开关
  	
  	# 通过 request.build_opener()方法使用这些代理Handler对象，创建自定义opener对象
  	# 根据代理开关是否打开，使用不同的代理模式
  	if proxySwitch:
  	    opener = request.build_opener(httpproxy_handler)
  	else:
  	    opener = request.build_opener(nullproxy_handler)
  	
  	request = request.Request("http://www.baidu.com/")
  	
  	# 1. 如果这么写，只有使用opener.open()方法发送请求才使用自定义的代理，而urlopen()则不使用自定义代理。
  	response = opener.open(request)
  	
  	# 2. 如果这么写，就是将opener应用到全局，之后所有的，不管是opener.open()还是urlopen() 发送请求，都将使用自定义代理。
  	# urllib2.install_opener(opener)
  	# response = urlopen(request)
  	print(response.read())

  如果代理IP足够多，就可以像随机获取User-Agent一样，随机选择一个代理去访问网站。

  	proxy_list = [
  	    {"http" : "110.73.1.105:8123"},
  	    {"http" : "110.73.40.20:8123"},
  	    {"http" : "124.88.67.81:80"},
  	    {"http" : "124.88.67.81:80"},
  	    {"http" : "124.88.67.81:80"}
  	]
  	
  	# 随机选择一个代理
  	proxy = random.choice(proxy_list)
  	httpproxy_handler = request.ProxyHandler(proxy)

4. handler

    ```
    from urllib import request
    from urllib.error import URLError
    
    
    password_mgr = request.HTTPPasswordMgrWithDefaultRealm()
    top_level_url = 'http://localhost:8080/users/login'
    req = request.Request(top_level_url)
    try:
        # 创建一个密码管理者
        # 如果知道 realm, 我们可以使用他代替 ``None``.
        # password_mgr.add_password(None, top_level_url, username, password)
        password_mgr.add_password(None, top_level_url, '13812790421', '123456')
    
        # 创建了一个新的handler
        handler = request.HTTPBasicAuthHandler(password_mgr)
    
        # 创建 "opener" (OpenerDirector 实例)
        opener = request.build_opener(handler)
        a_url ='http://localhost:8080/users/getAllUsers'
    
        # 使用 opener 获取一个URL
        response =opener.open(a_url)
    
        # 安装 opener.
        # 现在所有调用 urllib2.urlopen 将用我们的 opener.
        urllib.install_opener(opener)
    except URLError as e:
        if hasattr(e, 'code'):
            print ('The server couldn\'t fulfill the request.')
            print ('Error code: ', e.code)
        elif hasattr(e, 'reason'):
            print ('We failed to reach a server.')
            print ('Reason: ', e.reason())
        else:
            print (response.read())
    
    ```
# Requests

1. 介绍

	Requests 继承了urllib的所有特性。Requests支持HTTP连接保持和连接池，支持使用cookie保持会话，支持文件上传，支持自动确定响应内容的编码，支持国际化的 URL 和 POST 数据自动编码。

requests 的底层实现其实就是 urllib3

Requests的文档非常完备，中文文档也相当不错。Requests能完全满足当前网络的需求，支持Python 2.6—3.5，而且能在PyPy下完美运行。

[开源地址](https://github.com/kennethreitz/requests)

[中文文档 API](http://docs.python-requests.org/zh_CN/latest/index.html)

2. 安装

		pip install requests
	
3. get请求

		import requests

		url='https://www.liepin.com/sh/zhaopin/pn1/?' \
		    'd_pageSize=40&siTag=&d_headId=7523ef4c1e412df5e007f3cfd117447d&d_ckId=7523ef4c1e412df5e007f3cfd117447d&d_sfrom=' \
		    'search_city&'
		qs={
		    "key":"python",
		    "d_curPage":0
		
		}
		
		headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.99 Safari/537.36"}
		# params 接收一个字典或者字符串的查询参数，字典类型自动转换为url编码，不需要urlencode()
		response = requests.get(url, params = qs, headers = headers)
		
		# 查看响应内容，response.text 返回的是Unicode格式的数据
		print(response.text)
		# 查看响应内容，response.content返回的字节流数据
		print(response.content)
		
		# 查看完整url地址
		print(response.url)
		
		# 查看响应头部字符编码
		print(response.encoding)
		
		# 查看响应码
		print(response.status_code)
		#查看以一个 Python 字典形式展示的服务器响应头
		
		print(response.headers)
	
	>但是这个字典比较特殊：它是仅为 HTTP 头部而生的。根据 RFC 2616， HTTP 头部是大小写不敏感的。

	因此，我们可以使用任意大写形式来访问这些响应头字段：
	
		r.headers['Content-Type']
		r.headers.get('content-type')
	
3. post 请求

	response = requests.post（url, data = data)
	
	如果是json文件可以直接显示
	
		print(response.json())
	
	>如果 JSON 解码失败， r.json() 就会抛出一个异常。例如，响应内容是 401 (Unauthorized)，尝试访问 r.json() 将会抛出 ValueError: No JSON object could be decoded 异常。

	>需要注意的是，成功调用 r.json() 并**不**意味着响应的成功。有的服务器会在失败的响应中包含一个 JSON 对象（比如 HTTP 500 的错误细节）。这种 JSON 会被解码返回。要检查请求是否成功，请使用 r.raise_for_status() 或者检查 r.status_code 是否和你的期望相同。
	
4. 代理

	如果需要使用代理，你可以通过为任意请求方法提供 proxies 参数来配置单个请求
	
		import requests
	
		# 根据协议类型，选择不同的代理
		proxies = {
		  "http": "http://12.34.56.79:9527",
		  "https": "http://12.34.56.79:9527",
		}
		
		response = requests.get("http://www.baidu.com", proxies = proxies)
		print response.text
	
5. 处理HTTPS请求 SSL证书验证

	要想检查某个主机的SSL证书，你可以使用 verify 参数（也可以不写）
	
		import requests
		response = requests.get("https://www.baidu.com/", verify=True)
		
		# 也可以省略不写
		# response = requests.get("https://www.baidu.com/")
		print r.text
    
# 正则表达式
https://www.cnblogs.com/tina-python/p/5508402.html

1. 简介


     正则表达式本身是一种小型的、高度专业化的编程语言，而在python中，
     通过内嵌集成re模块，程序媛们可以直接调用来实现正则匹配。
     正则表达式模式被编译成一系列的字节码，然后由用C编写的匹配引擎执行。
2. 语法规则

    1. 普通字符和11个元字符：

        普通字符|匹配自身|abc|abc|
        ---|---|---|---|
        .|匹配任意除换行符"\n"外的字符(在DOTALL模式中也能匹配换行符|a.c|abc|
        \\|转义字符，使后一个字符改变原来的意思|a\.c;a\\c|a.c;a\c|
        \*|匹配前一个字符0或多次|abc*|ab;abccc|
        +|匹配前一个字符1次或无限次|abc+|abc;abccc|
        ?|匹配一个字符0次或1次|abc?|ab;abc|
        ^|匹配字符串开头。在多行模式中匹配每一行的开头|	^abc|abc|
        $|匹配字符串末尾，在多行模式中匹配每一行的末尾|	abc$|abc|
        \||	或。匹配|左右表达式任意一个，从左到右匹配，如果|没有包括在()中，则它的范围是整个正则表达式|abc|defabcdef|
        {}|	{m}匹配前一个字符m次，{m,n}匹配前一个字符m至n次，若省略n，则匹配m至无限次|ab{1,2}c|abc abbc|
        []|字符集。对应的位置可以是字符集中任意字符。字符集中的字符可以逐个列出，也可以给出范围，如[abc]或[a-c]。[^abc]表示取反，即非abc。所有特殊字符在字符集中都失去其原有的特殊含义。用\反斜杠转义恢复特殊字符的特殊含义。|a[bcd]e|abe ace ade|
        ()|被括起来的表达式将作为分组，从表达式左边开始没遇到一个分组的左括号“（”，编号+1.分组表达式作为一个整体，可以后接数量词。表达式中的|仅在该组中有效。|	(abc){2}a(123|456)c|abcabc a456c|

        这里需要强调一下反斜杠\的作用：

        * 反斜杠后边跟元字符去除特殊功能；（即将特殊字符转义成普通字符）
        * 反斜杠后边跟普通字符实现特殊功能；（即预定义字符）
        * 引用序号对应的字组所匹配的字符串。

        ```
            a=re.search(r'(tina)(fei)haha\2','tinafeihahafei tinafeihahatina').group()
            print(a)
            结果：
            tinafeihahafei
        ```

    2. 预定义字符集（可以写在字符集[...]中）

        * \d  数字:[0-9]

        * \D  非数字:[^\d]
        * \s  匹配任何空白字符:[<空格>\t\r\n\f\v]

        * \S	非空白字符:[^\s]
        * \w  匹配包括下划线在内的任何字字符:[A-Za-z0-9_]

        * \W  匹配非字母字符，即匹配特殊字符

        * \A  仅匹配字符串开头,同^	\Aabc
        * \Z  仅匹配字符串结尾，同$
        * \b  匹配\w和\W之间，即匹配单词边界匹配一个单词边界，也就是指单词和空格间的位置。例如， 'er\b' 可以匹配"never" 中的 'er'，但不能匹配 "verb" 中的 'er'。	\babc\b
            a\b!bc	空格abc空格
            a!bc
        * \B  [^\b]

        ```
            import re
            w = re.findall(r'\bzhan','zhan liang')
            print(w)
            s = re.findall(r'\btina','tiana tinaaaa')
            print(s)
            v = re.findall(r'\btina','tian#tinaaaa')
            print(v)
            a = re.findall(r'\btina\b','tian#tina@aaa')
            print(a)
        ```
    3. 特殊分组用法：

        (?P\<name>)|分组，除了原有的编号外再指定一个额外的别名|	(?P<id>abc){2}	|abcabc|
        ---|---|---|---|
        (?P=name)|引用别名为<name>的分组匹配到字符串|	(?P<id>\d)abc(?P=id)|1abc15abc5|
        \\\<number>|引用编号为<number>的分组匹配到字符串|	(\d)abc\1|1abc15abc5|

        1. (?P<tag>abc)就是把abc这个匹配项取个别名，这样后面用到abc的时候就用tag来代替了，比如

           ```
           import re
           
           str2='<li>aaa</li><li>bbb</li><li>ccc</li><a>eeee</a>'
           
           # 找出格式为<xxx>..</xxx>的元素，因为我们把\w+取名为dd，那么意味着后面的结束标签中的内容也必须和dd变量的内容一模一样
           reg2=re.compile(r'\<(?P<dd>\w+)\>(\w+)\</(?P=dd)\>')
           
           print(reg2.findall(str2))
           
           #找出单词格式为AABB 的词语
           
           str1='aabb is a word,and ccdd is a word too'
           
           # reg1=re.compile(r'(?P<tt>\w)(?P=tt)(?P<ee>\w)(?P=ee)')
           reg1=re.compile(r'((?P<tt>\w)(?P=tt)(?P<ee>\w)(?P=ee))')
           
           print(reg1.findall(str1))
           
           #\1 \2表示的是位置，类似于‘hello {0},i am {1}’.format(n,m)
           reg3=re.compile(r'(\w)\1(\w)\2')
           
           print(reg3.findall(str1))
           ```


4. re模块中常用功能函数

    1. compile()

        编译正则表达式模式，返回一个对象的模式。（可以把那些常用的正则表达式编译成正则表达式对象，
        这样可以提高一点效率。）

        ```
            regex01=re.compile(r'^李\w{1,2}$')
            # regex01=re.compile(r'李\w{1,2}')
            #如果不加上开始和结束标志，其实就是匹配部分数据，下面的字符串就会匹配'李小飞'

            str01='李小飞龙'

            res01=regex01.findall(str01)
            print(res01)
        ```
    2. match()

        决定re是否在字符串刚开始的位置匹配。//注：这个方法并不是完全匹配。
        当pattern结束时若string还有剩余字符，
        仍然视为成功。想要完全匹配，可以在表达式末尾加上边界匹配符'$'

        ```
            #匹配模式
            #如果单纯是测定字符串是否匹配正则表达式的规则，则不需要用到"()"
            #如果没有匹配结果为none
            m = re.match(r'^\d{3}-\d{3,8}$', '010-12345')
            #分组 一定要用到分组符号"()"

            m = re.match(r'^(\d{3})-(\d{3,8})$', '010-12345')
            print(m.group(0))
            print(m.group(1))
            print(m.group(2))
            print(m.groups())
            #提取时间

            t = '19:05:30'
            rt = re.match(r'^(0[0-9]|1[0-9]|2[0-3]|[0-9])\:(0[0-9]|1[0-9]|2[0-9]|3[0-9]|4[0-9]|5[0-9]|[0-9])\:(0[0-9]|1[0-9]|2[0-9]|3[0-9]|4[0-9]|5[0-9]|[0-9])$', t)
            print(rt.groups())
        ```

        **没有（）就是匹配模式，匹配模式就是从开始第一个字符进行匹配，如果匹配成功，那么后面的内容就不会匹配。有了（）就是分组查找模式,有了分组就是把匹配到的内容分组存放**

    3. search()

         格式：

        ```
        re.search(pattern, string, flags=0)
        
        re.search函数会在字符串内查找模式匹配,只要找到第一个匹配然后返回，如果字符串没有匹配，则返回None。
        
        print(re.search('\dcom','www.4comrunoob.5com').group())
        执行结果如下：
        4com
        
        ```
        
        **没有（）就是查找模式，查找模式就是在当前字符串中查找符合规则的子串，如果找到则停止找找。有了（）就是分组查找模式,有了分组就是把匹配到的内容分组存放**
    4. findall()

        re.findall遍历匹配，可以获取字符串中所有匹配的字符串，返回一个列表。

         格式：

        ```
             re.findall(pattern, string, flags=0)
        ```

        ```
            p = re.compile(r'\d+')
            print(p.findall('o1n2m3k4'))
            执行结果如下：
            ['1', '2', '3', '4']
            复制代码
            import re
            tt = "Tina is a good girl, she is cool, clever, and so on..."
            rr = re.compile(r'\w*oo\w*')
            print(rr.findall(tt))
            print(re.findall(r'(\w)*oo(\w)',tt))#()表示子表达式
            执行结果如下：
            ['good', 'cool']
            [('g', 'd'), ('c', 'l')]
        ```

        简单爬虫

        ```
            regex=re.compile(r'<li>(.+?)</li>')
            str01='
                    <html lang="en">
                    <head>
                        <meta charset="UTF-8">
                        <title>Title</title>
                    </head>
                    <body>
                        <li>001</li>
                        <li>002</li>
                        <li>003</li>
                        <li>004</li>
                    </body>
                    </html>
                '

                # str01=re.sub(r"\r|\n", "",str01)
                # print(str01)
                res01=regex.findall(str01)
                
                #不区分大小写
                regex=re.compile(r'<li id=(.+)>(\w+)</li>',flags=re.IGNORECASE)
                print(res01)
        ```

    5. split()

        按照能够匹配的子串将string分割后返回列表。

        可以使用re.split来分割字符串，如：re.split(r'\s+', text)；将字符串按空格分割成一个单词列表。

        格式：

        ```
        re.split(pattern, string[, maxsplit])

        maxsplit用于指定最大分割次数，不指定将全部分割。

        print(re.split('\d+','one1two2three3four4five5'))
        执行结果如下：
        ['one', 'two', 'three', 'four', 'five', '']

        ```

    6. sub()

        使用re替换string中每一个匹配的子串后返回替换后的字符串。

        格式：

            re.sub(pattern, repl, string, count)
            
            复制代码
            import re
            text = "JGood is a handsome boy, he is cool, clever, and so on..."
            print(re.sub(r'\s+', '-', text))
            执行结果如下：
            JGood-is-a-handsome-boy,-he-is-cool,-clever,-and-so-on...
            其中第二个函数是替换后的字符串；本例中为'-'
            
            第四个参数指替换个数。默认为0，表示每个匹配项都替换。


        re.sub还允许使用函数对匹配项的替换进行复杂的处理。
    
        如：re.sub(r'\s', lambda m: '[' + m.group(0) + ']', text, 0)；将字符串中的空格' '替换为'[ ]'。
    
            import re
            text = "JGood is a handsome boy, he is cool, clever, and so on..."
            print(re.sub(r'\s+', lambda m:'['+m.group(0)+']', text,0))
            执行结果如下：
            JGood[ ]is[ ]a[ ]handsome[ ]boy,[ ]he[ ]is[ ]cool,[ ]clever,[ ]and[ ]so[ ]on...


### 一些注意点

   1. re.match与re.search与re.findall的区别：

        re.match只匹配字符串的开始，如果字符串开始不符合正则表达式，
        则匹配失败，函数返回None；而re.search匹配整个字符串，直到找到一个匹配。


            a=re.search('[\d]',"abc33").group()
            print(a)
            p=re.match('[\d]',"abc33")
            print(p)
            b=re.findall('[\d]',"abc33")
            print(b)
            执行结果：
            3
            None
            ['3', '3']
   2. 贪婪匹配与非贪婪匹配
		
		 1. 贪婪模式：在整个表达式匹配成功的前提下，尽可能多的匹配 ( * )；

		 
		 2. 非贪婪模式：在整个表达式匹配成功的前提下，尽可能少的匹配 ( ? )；
    
	   *?  ,+?     ,??  ,{m,n}?
	   
	   前面的*,+,?等都是贪婪匹配，也就是尽可能匹配，后面加?号使其变成惰性匹配
			
	
	   
			
			```
			str4='ababbbbbab'
	
			#reg4=re.compile(r'ab+?')
			reg4=re.compile(r'ab+')
	
			print(reg4.findall(str4))
			```
			
			
			```
				aa<div>test1</div>bb<div>test2</div>cc
	
				使用贪婪的数量词的正则表达式：<div>.*</div>
	
				匹配结果：<div>test1</div>bb<div>test2</div>
				使用非贪婪的数量词的正则表达式：<div>.*?</div>
	
				匹配结果：<div>test1</div>
	
			```
	        demo1
	
	            a = re.findall(r"a(\d+?)",'a23b')
	            print(a)
	            b = re.findall(r"a(\d+)",'a23b')
	            print(b)
	            执行结果：
	            ['2']
	            ['23']
	            
	            a = re.match('<(.*)>','<H1>title<H1>').group()
	            print(a)
	            b = re.match('<(.*?)>','<H1>title<H1>').group()
	            print(b)
	            执行结果：
	            <H1>title<H1>
	            <H1>
	
	        demo2
	
	            a = re.findall(r"a(\d+)b",'a3333b')
	            print(a)
	            b = re.findall(r"a(\d+?)b",'a3333b')
	            print(b)
	            执行结果如下：
	            ['3333']
	            ['3333']
	            #######################
	            这里需要注意的是如果前后均有限定条件的时候，就不存在什么贪婪模式了，非匹配模式失效。
	            
# 爬虫页面解析
1. 正则表达式解析

	1. 实际上爬虫一共就四个主要步骤：

		1. 明确目标 (要知道你准备在哪个范围或者网站去搜索)
		1. 爬 (将所有的网站的内容全部爬下来)
		1. 取 (去掉对我们没用处的数据)
		1. 处理数据（按照我们想要的方式存储和使用）

	2. 匹配中文

		在某些情况下，我们想匹配文本中的汉字，有一点需要注意的是，中文的 unicode 编		码范围 主要在 [u4e00-u9fa5]，这里说主要是因为这个范围并不完整，比如没有包		括全角（中文）标点，不过，在大部分情况下，应该是够用的。

		假设现在想把字符串 title = u'你好，hello，世界' 中的中文提取出来，可以这		么做：
		
			import re
	
			title = u'你好，hello，世界'
			pattern = re.compile(ur'[\u4e00-\u9fa5]+')
			result = pattern.findall(title)
			
			print(result)
		注意到，我们在正则表达式前面加上了两个前缀 ur，其中 r 表示使用原始字符串，u 表示是 unicode 字符串。但是在python3中默认编码为unicode所以u必须省略。
		
		执行结果:

			['你好', '世界']
		
		**如果爬取的网页中有中文，可能会出现乱码。原因是网页的编码格式可能是GBK,我们可以这样**
		
			gbk_html = html.decode('gbk').encode('utf-8')	              
1. 案例一：解析淘宝数据

		import re
		li=[]
		with open('taopage0.html','r+') as fp:
		    data=fp.read()
		
		    plt = re.findall(r'\"view_price\"\: \"[\d\.]*\"', data)
		
		    # 在爬取下来的网页中查找物品
		    tlt = re.findall(r'\"raw_title\"\: \".*?\"', data)
		
		    loc=re.findall(r'\"item_loc\"\: \".*?\"', data)
		    
		    for i in range(len(plt)):
		        price = eval(plt[i].split(':')[1])
		        title = eval(tlt[i].split(':')[1])
		        location = eval(loc[i].split(':')[1])
		
		        li.append([price,title,location])
		
		
		print(li)
		
2. 案例二：解析猎聘网

# spider-页面解析-XML	
2. XML

	1. 什么是XML

		* XML 指可扩展标记语言（EXtensible Markup Language）
		* XML 是一种标记语言，很类似 HTML
		* XML 的设计宗旨是传输数据，而非显示数据
		* XML 的标签需要我们自行定义。
		* XML 被设计为具有自我描述性。
		* XML 是 W3C 的推荐标准

	2. 什么是XPath？

		XPath (XML Path Language) 是一门在 XML 文档中查找信息的语言，可用来在 XML 文档中对元素和属性进行遍历。
		
		XPath 开发工具

		- 开源的XPath表达式编辑工具:XMLQuire(XML格式文件可用)
		- Chrome插件 XPath Helper
		- Firefox插件 XPath Checker

	3. 示例文档

			<?xml version="1.0" encoding="utf-8"?>

			<bookstore> 
			
			  <book category="cooking"> 
			    <title lang="en">Everyday Italian</title>  
			    <author>Giada De Laurentiis</author>  
			    <year>2005</year>  
			    <price>30.00</price> 
			  </book>  
			
			  <book category="children"> 
			    <title lang="en">Harry Potter</title>  
			    <author>J K. Rowling</author>  
			    <year>2005</year>  
			    <price>29.99</price> 
			  </book>  
			
			  <book category="web"> 
			    <title lang="en">XQuery Kick Start</title>  
			    <author>James McGovern</author>  
			    <author>Per Bothner</author>  
			    <author>Kurt Cagle</author>  
			    <author>James Linn</author>  
			    <author>Vaidyanathan Nagarajan</author>  
			    <year>2003</year>  
			    <price>49.99</price> 
			  </book> 
			
			  <book category="web" cover="paperback"> 
			    <title lang="en">Learning XML</title>  
			    <author>Erik T. Ray</author>  
			    <year>2003</year>  
			    <price>39.95</price> 
			  </book> 
			
			</bookstore>
	4. 安装lxml

			pip install lxml
	4. 常用方法

		1. etree.parse()

			读取xml文件，结果为**xml对象**（不是字符串）
		2. etree.HTML(string_html)

			将字符串形势的html文件转换为xml对象
		3. etree.tostring(htmlelement, encoding="utf-8").decode("utf-8")

				etree.tostring(html,encoding="utf-8", pretty_print=True).decode()

			按字符串序列化HTML文档
	5. 选择器

		|表达式|	描述|
		|---|---|---|
		|nodename|	选取此节点的所有子节点。|
		|/	|从根节点选取。|
		|//	|从匹配选择的当前节点选择文档中的节点，而不考虑它们的位置。|
		|.	|选取当前节点。|
		|..	|选取当前节点的父节点。|
		|@	|选取属性。|
		
		范例
		
			bookstore	选取 bookstore 元素的所有子节点(如果只有一个的话)。
			/bookstore	选取根元素 bookstore。注释：假如路径起始于正斜杠( / )，则此路径始终代表到某元素的绝对路径！
			bookstore/book	选取属于 bookstore 的直接子元素的所有 book 元素。
			//book	选取所有 book 子元素，而不管它们在文档中的位置。
			bookstore//book	选择属于 bookstore 元素的后代的所有 book 元素，而不管它们位于 bookstore 之下的什么位置。
			bookstore//book/@lang	选取book元素的lang属性值。
			bookstore//book[@class="book-css"]/title	选取class属性值为“book-css”的book元素的title。
			//*[@class="bold"] 获取 class 值为 bold 的标签名
		
		**使用属性时，不要忘记@符号**
		> /表示直接子元素，//表示所有子孙元素
		
		
		读取案例-xml
		
			#from lxml import etree #这样写后面会出现红色波浪线
			
			import lxml.html
			etree = lxml.html.etree
			# 读取文件：这个时候只时候读取xml格式的文件，显然局限性太强！！！！！
			html = etree.parse('data.xml')
			# 转化为字节字符串
			# result = etree.tostring(html, pretty_print=True)
			# print(type(html))  # 显示etree.parse() 返回类型
			# print(result)
			titles = html.xpath('/bookstore/book/title')
			
			for tt in titles:
			    print(tt.text)
			
			# 如果不是直接子元素就要用//
	
			titles = html.xpath('/bookstore//title')
			
			for tt in titles:
			    print(tt.text)
	6. lxml读取html文件
		​	
		自己创建html解析器，增加parser参数
		
			import lxml.html
			etree = lxml.html.etree
			parser = etree.HTMLParser(encoding="utf-8")
			htmlelement = etree.parse("liepin.html", parser=parser)
			print(htmlelement)
			html_string=etree.tostring(htmlelement, encoding="utf-8").decode("utf-8")
			
			#读取innerText
			links=htmlelement.xpath('//div/div/span/a')
	
			for link in links:
			    print(link.text)
			    
			#读取属性的值
			
			with open('liepin.html','r+') as fp:
			    content=fp.read()
			    html=etree.HTML(content)
			    links = html.xpath('//div/div/span/@title')
			    for title in titles:
			        print(title)
# spider-页面解析-CSS
## BeautifulSoup4
3. CSS 选择器：BeautifulSoup4

	lxml 只会局部遍历，而Beautiful Soup 是基于HTML DOM的，会载入整个文档，解析整个DOM树，因此时间和内存开销都会大很多，所以性能要低于lxml。

	BeautifulSoup 用来解析 HTML 比较简单，API非常人性化，支持CSS选择器、Python标准库中的HTML解析器，也支持 lxml 的 XML解析器。

	Beautiful Soup 3 目前已经停止开发，推荐现在的项目使用Beautiful Soup 4。使用 pip 安装即可：pip install beautifulsoup4
	
	1. 安装

			pip install beautifulsoup4
	2. tag (可以使用文档对象直接.标签名获取)

			from bs4 import BeautifulSoup

			# html='....'
			#创建 Beautiful Soup 对象
			# soup = BeautifulSoup(html)
			
			#打开本地 HTML 文件的方式来创建对象
			soup = BeautifulSoup(open('data.xml'),"lxml")
			
			#格式化输出 soup 对象的内容
			# print(soup.prettify())
			print(soup.book) 
		
		>我们可以利用 soup 加标签名轻松地获取这些标签的内容，这些对象的类型是bs4.element.Tag。但是注意，它查找的是在所有内容中的第一个符合要求的标签。
print(soup.book)
	3. 对于 Tag，它有两个重要的属性，是 name 和 attrs

			from bs4 import BeautifulSoup
			
			# html='....'
			#创建 Beautiful Soup 对象
			# soup = BeautifulSoup(html)
			
			#打开本地 HTML 文件的方式来创建对象
			soup = BeautifulSoup(open('liepin.html'),"lxml")
			
			#格式化输出 soup 对象的内容
			# print(soup.prettify())
			
			nodes=soup.select('div.company-info p a')
			
			nodes=soup.select('div#div01 div.company-info > p[name="pr"] a')
			
			for node in nodes:
			    #获取节点名称
			    print(node.name)
			
			    #获取节点所有属性
			    print(node.attrs)
			
			    #获取节点href属性的值
			    print(node['href'])
			    # print(node.get('href'))

			    
			    #获取节点的值
			    print(node.string)		

# Selenium	
1. 介绍
	
	selenium 是一个用于Web应用程序测试的工具。Selenium测试直接运行在浏览器中，就像真正的用户在操作一样。支持的浏览器包括IE（7, 8, 9, 10, 11），Mozilla Firefox，Safari，Google Chrome，Opera等。这个工具的主要功能包括：测试与浏览器的兼容性——测试你的应用程序看是否能够很好得工作在不同浏览器和操作系统之上。测试系统功能——创建回归测试检验软件功能和用户需求。支持自动录制动作和自动生成 .Net、Java、Perl等不同语言的测试脚本。 
	selenium用于爬虫，主要是用来解决javascript渲染的问题 

	Selenium 可以根据我们的指令，让浏览器自动加载页面，获取需要的数据，甚至页面截屏，或者判断网站上某些动作是否发生。

	Selenium 自己不带浏览器，不支持浏览器的功能，它需要与第三方浏览器结合在一起才能使用。但是我们有时候需要让它内嵌在代码中运行，所以我们可以用一个叫 PhantomJS 的工具代替真实的浏览器。
	
2. 安装

		pip install selenium
		
		
	[官方文档](https://selenium-python.readthedocs.io/index.html)
	
3. headless brower

	无头模式是运行浏览器的一种非常有用的方式。就像听起来一样，浏览器正常运行，减去任何可见的UI组件。虽然对网上冲浪不是那么有用，但它通过自动化测试自成一体。
	
	chrome无头浏览器：
	
	[https://developers.google.com/web/updates/2017/04/headless-chrome](https://developers.google.com/web/updates/2017/04/headless-chrome)
	
	
	4. 无头Chrome入门
	
	
		无头Chrome 在Chrome 59中发布。这是在无头环境中运行Chrome浏览器的一种方式。基本上，运行Chrome没有铬！它将Chromium和Blink渲染引擎提供的所有现代Web平台功能引入命令行。
		
		为什么这有用？
		
		无头浏览器是自动测试和服务器环境的绝佳工具，您不需要可见的UI shell。例如，您可能希望针对真实网页运行某些测试，创建PDF，或者仅检查浏览器如何呈现URL。
		
	5. 命令行下启动无头浏览器
		
		[...](https://developers.google.com/web/updates/2017/04/headless-chrome#node)
		
		[...](https://blog.csdn.net/qq_30242609/article/details/79323963)
		
			 chrome --headless --disable-gpu --dump-dom https://www.baidu.com/
		
		**注意：现在，--disable-gpu如果您在Windows上运行，还需要包含该标志。**
		
		这里chrome是本地浏览器的别名，这个时候我们的目录应该定位到本机“/Applications/Google Chrome.app”的目录下
		
		修改别名的代码如下第一条
		
			alias chrome="/Applications/Google\ Chrome.app/Contents/MacOS/Google\ Chrome"
			
			alias chrome-canary="/Applications/Google\ Chrome\ Canary.app/Contents/MacOS/Google\ Chrome\ Canary"
			alias chromium="/Applications/Chromium.app/Contents/MacOS/Chromium"
			
		如果您使用的是Chrome的稳定渠道且无法获得测试版，我建议您使用chrome-canary：
		
		[在这里下载Chrome Canary](https://www.google.com/chrome/browser/canary.html)
		
	3. 有用的命令行标志 
		
		1. 打印DOM
		2. 
			该--dump-dom标志印document.body.innerHTML到stdout：
	
				chrome --headless --disable-gpu --dump-dom https://www.chromestatus.com/
				
		2. 创建PDF
	
		
			该--print-to-pdf标志创建页面的PDF：
	
				chrome --headless --disable-gpu --print-to-pdf https://www.chromestatus.com/
	
	
		3. 截图
	
			要捕获页面的屏幕截图，请使用以下--screenshot标志：
	
				chrome --headless --disable-gpu --screenshot https://www.chromestatus.com/
				
				# Size of a standard letterhead.
				chrome --headless --disable-gpu --screenshot --window-size=1280,1696 https://www.chromestatus.com/
				
				# Nexus 5x
				chrome --headless --disable-gpu --screenshot --window-size=412,732 https://www.chromestatus.com/



4. 安装webdriver（chromedriver）

	下载地址：http://chromedriver.storage.googleapis.com/index.html
	
	>最新chrome版本号69对应	chromedriver版本为2.42
	
	chromedriver解压后放到Python或者其他配置了环境变量的目录下。我们这里也可以放在隔离环境venv的bin目录下。
	
	测试代码：
	
		from selenium import webdriver
		browser=webdriver.Chrome()
		browser.get("https://www.baidu.com")
		print(browser.page_source)

		    
6. 语法
	
	**here**[参考](https://blog.csdn.net/qq_29186489/article/details/78661008)
	
	[重要参考](https://www.cnblogs.com/hanxiaobei/p/6108677.html)
	
	
	1. 查找单个元素

			#_*_coding: utf-8_*_
			
			from selenium import webdriver
			from selenium.webdriver.common.by import By
			browser=webdriver.Chrome()
			browser.get("http://www.taobao.com")
			input_first=browser.find_element_by_id("q")
			input_second=browser.find_element_by_css_selector("#q")
			input_third=browser.find_element(By.ID,"q")
			print(input_first,input_second,input_first)
			browser.close()
		
	1. 查找多个元素
	
			lis=browser.find_element_by_css_selector("li")
			lis_c=browser.find_element(By.CSS_SELECTOR,"li")
		
	3. 元素的交互操作 
	
			from selenium import webdriver
			import time
			browser=webdriver.Chrome()
			browser.get("https://www.taobao.com")
			input=browser.find_element_by_id("q")
			input.send_keys("iPhone")
			time.sleep(10)
			input.clear()
			input.send_keys("iPad")
			button=browser.find_element_by_class_name("btn-search")
			button.click()
			time.sleep(10)
			browser.close()
		
	4. 页面等待

		注意：这是非常重要的一部分！！
		
		现在的网页越来越多采用了 Ajax 技术，这样程序便不能确定何时某个元素完全加载出来了。如果实际页面等待时间过长导致某个dom元素还没出来，但是你的代码直接使用了这个WebElement，那么就会抛出NullPointer的异常。
		
		为了避免这种元素定位困难而且会提高产生 ElementNotVisibleException 的概率。所以 Selenium 提供了两种等待方式，一种是隐式等待，一种是显式等待。
		
		隐式等待是等待特定的时间，显式等待是指定某一条件直到这个条件成立时继续执行。
	
	
			from selenium import webdriver
			from selenium.webdriver.common.by import By
			# WebDriverWait 库，负责循环等待
			from selenium.webdriver.support.ui import WebDriverWait
			# expected_conditions 类，负责条件出发
			from selenium.webdriver.support import expected_conditions as EC
			
			driver = webdriver.Chrome()
			driver.get("http://www.xxxxx.com/loading")
			try:
			    # 页面一直循环，直到 id="myDynamicElement" 出现
			    element = WebDriverWait(driver, 10).until(
			        EC.presence_of_element_located((By.ID, "myDynamicElement"))
			    )
			finally:
			    driver.quit()
		>如果不写参数，程序默认会 0.5s 调用一次来查看元素是否已经生成，如果本来元素就是存在的，那么会立即返回。
		
		隐式等待

			隐式等待比较简单，就是简单地设置一个等待时间，单位为秒。
			
				from selenium import webdriver
				
				driver = webdriver.Chrome()
				driver.implicitly_wait(10) # seconds
				driver.get("http://www.xxxxx.com/loading")
				myDynamicElement = driver.find_element_by_id("myDynamicElement")
5. 案例：百度-有头

		from selenium import webdriver
		from selenium.webdriver.common.by import By
		from selenium.webdriver.common.keys import Keys
		from selenium.webdriver.support import expected_conditions as EC
		from selenium.webdriver.support.wait import WebDriverWait
		import time
		browser=webdriver.Chrome()
		try:
		    browser.get("https://www.baidu.com")
		    input=browser.find_element_by_id("kw")
		    input.send_keys("Python")
		    input.send_keys(Keys.ENTER)
		    wait=WebDriverWait(browser,10)
		    wait.until(EC.presence_of_element_located((By.ID,"content_left")))
		    print(browser.current_url)
		    print(browser.get_cookies())
		    print(browser.page_source)
		    time.sleep(10)
		finally:
		    browser.close()

5. 案例：百度-无头
		
		from selenium.webdriver.chrome.options import Options

		...
		try:
		    chrome_options = Options()
		    chrome_options.add_argument('--headless')
		    chrome_options.add_argument('--disable-gpu')
		    browser = webdriver.Chrome(chrome_options=chrome_options)
		    
6. 案例：搜索nike并爬取数据
		
		from selenium import webdriver
		from selenium.webdriver.common.by import By
		from selenium.webdriver.common.keys import Keys
		from selenium.webdriver.support import expected_conditions as EC
		from selenium.webdriver.support.wait import WebDriverWait
		
		import time
		
		from selenium.webdriver.chrome.options import Options
		try:
		    chrome_options = Options()
		    chrome_options.add_argument('--headless')
		    chrome_options.add_argument('--disable-gpu')
		    browser = webdriver.Chrome(chrome_options=chrome_options)
		    # 隐式等待
		    browser.implicitly_wait(10)  # seconds
		    url='https://s.taobao.com/search?q=&imgfile=&js=1&stats_click=search_radio_all%3A1&initiative_id=staobaoz_20180914&ie=utf8'
		    browser.get(url)
		    input=browser.find_element_by_id("q")
		    input.send_keys("nike")
		    input.send_keys(Keys.ENTER)
		    wait=WebDriverWait(browser,10)
		    # wait.until(EC.presence_of_element_located((By.ID,"content_left")))
		    print(browser.current_url)
		    print(browser.get_cookies())
		    # print(browser.page_source)
		    with open('taobao.html','w+') as fp:
		        fp.write(browser.page_source)
		        fp.close()
		    time.sleep(10)
		finally:
		    browser.close()

		
7. 案例：模拟豆瓣登录

		from selenium import webdriver
		from selenium.webdriver.common.by import By
		from selenium.webdriver.common.keys import Keys
		from selenium.webdriver.support import expected_conditions as EC
		from selenium.webdriver.support.wait import WebDriverWait
		
		import time
		
		from selenium.webdriver.chrome.options import Options
		
		try:
		    chrome_options = Options()
		    chrome_options.add_argument('--headless')
		    chrome_options.add_argument('--disable-gpu')
		    browser = webdriver.Chrome(chrome_options=chrome_options)
		    # 隐式等待
		    browser.get("http://www.douban.com")
		
		    # 输入账号密码
		    browser.find_element_by_name("form_email").send_keys("13812790420")
		    browser.find_element_by_name("form_password").send_keys("******")
		
		    # 模拟点击登录
		    browser.find_element_by_xpath("//input[@class='bn-submit']").click()
		
		    # 等待3秒
		    time.sleep(3)
		
		    # 生成登陆后快照
		    browser.save_screenshot("douban.png")
		finally:
		    browser.close()
	
	







	            

