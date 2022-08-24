import requests,random,string

sites=[
    {
        "name":"feiniao",
        "url":"https://feiniaoyun.tk/",
        "reg_url":"https://feiniaoyun.tk/api/v1/passport/auth/register",
        "sub":"https://feiniaoyun.tk/api/v1/client/subscribe?token={token}"
    },
    {
        "name":"waiqi",
        "url":"https://waiqi.xyz/",
        "reg_url":"https://waiqi.xyz/api/v1/passport/auth/register",
        "sub":"https://waiqi.xyz/api/v1/client/subscribe?token={token}"
    },
    {
        "name":"ckcloud",
        "url":"https://www.ckcloud.xyz/",
        "reg_url":"https://www.ckcloud.xyz/api/v1/passport/auth/register",
        "sub":"https://www.ckcloud.xyz/api/v1/client/subscribe?token={token}"
    },
    {
        "name":"rocket",
        "url":"https://58rocket.com/",
        "reg_url":"https://58rocket.com/api/v1/passport/auth/register",
        "sub":"https://8rkt.xyz/api/v1/client/subscribe?token={token}"
    },
    {
        "name":"giao",
        "url":"https://giaoyun.xyz/",
        "reg_url":"https://giaoyun.xyz/api/v1/passport/auth/register",
        "sub":"https://giaoyun.xyz/api/v1/client/subscribe?token={token}"
    },
    {
        "name":"blackhole",
        "url":"https://blackholeservices.com/",
        "reg_url":"https://blackholeservices.com/api/v1/passport/auth/register",
        "sub":"https://subs.hdapi.work/api/v1/client/subscribe?token={token}"
    },
        {
        "name":"kelecloud",
        "url":"https://my.kelecloud.xyz/",
        "reg_url":"https://my.kelecloud.xyz/api/v1/passport/auth/register",
        "sub":"https://sub5.kelecloud.xyz/api/v1/client/subscribe?token={token}"
    },
    {
        "name":"circlecloud123",
        "url":"https://circlecloud123.com/",
        "reg_url":"https://circlecloud123.com/api/v1/passport/auth/register",
        "sub":"https://circlecloud123.com/api/v1/client/subscribe?token={token}"
    }
]

class tempsite():
    def __init__(self,site):
        self.reg_url=site["reg_url"]
        self.ref=site["url"]
        self.name=site["name"]
        self.sub=site["sub"]

    def register(self,email,password,proxy=None):
        headers= {
            "User-Agent":'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.54 Safari/537.36',
            "Referer": self.ref
        }
        data={
            "email":email,
            "password":password,
            "invite_code":None,
            "email_code":None
        }
        req=requests.post(self.reg_url,headers=headers,data=data,timeout=5,proxies=proxy)
        return req
        
    def getSubscribe(self):
        password=''.join(random.sample(string.ascii_letters + string.digits + string.ascii_lowercase, 10))
        email=password+"@gmail.com"
        req=self.register(email,password)
        token=req.json()["data"]["token"]
        subscribe=self.sub.format(token=token)
        return subscribe

    def saveconf(self):
        url=self.getSubscribe()
        for k in range(3):
            try:
                req=requests.get(url,timeout=20)
                v2conf=req.text
                break
            except:
                v2conf=""
        with open("./cdd1/"+self.name,"w") as f:
                    f.write(v2conf)

def getconf():
    for v2site in sites:
        obj=tempsite(v2site)
        try:
            obj.saveconf()
        except:
            pass  
    
