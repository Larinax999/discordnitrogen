from requests import post
from secrets import choice, token_hex
from concurrent.futures import ThreadPoolExecutor

executor = ThreadPoolExecutor(max_workers=1000)
f = open("nitro.txt", "a+")

def get():
    global f
    while 1:
        try:
            d=post("https://steelseries.com/api/v2/users",headers={"Host": "steelseries.com","User-Agent": "Go-http-client/1.1","Authorization": "Basic OThlNTQ1NWE5ZjY4MGM5YTVmZDcwNjo=","Content-Type": "application/json","Accept-Encoding": "gzip, deflate"},json={"accepted_privacy_policy" : True,"email" : f'{token_hex(3)}G@gmail.com',"password1" : "123456@aaaaAAAA","password2" : "123456@aaaaAAAA","subscribe_to_newsletter" : False}).json()
            dd=post("https://steelseries.com/api/v1/promos/discord-nitro",headers={"Host": "steelseries.com","User-Agent": "Go-http-client/1.1","Authorization":f"Bearer {d['access_token']}","Content-Type": "application/json","Accept-Encoding": "gzip, deflate"},json={"uuid":f"8029cf03-{token_hex(2)}-{token_hex(2)}-{token_hex(2)}-0cdcc0e8a6d6"}).json()
            print(dd['promo_code_url'][:33])
            f.write(f"{dd['promo_code_url']}\n")
            f.flush()
        except: pass
            #print(f"[!] error | {e}")


for _ in range(100): # 100 nitro per ip
    executor.submit(get)
executor.shutdown(wait=True)
f.close()
