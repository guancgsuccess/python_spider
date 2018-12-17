from urllib import request
with request.urlopen('http://www.taobao.com') as f:
    # data = f.read()
    # print('Status:', f.status, f.reason)# Status: 200 OK
    # print(data)

    if f.status == 200:
        data = f.read()
        # print(data.decode())
        try:
            with open('first.html','w+',encoding="utf-8") as fp:
                fp.write(data.decode())
                fp.close()
        except Exception as ex:
            print(ex)


