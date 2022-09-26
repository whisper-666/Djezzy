import requests,os
os.system('clear')
print('''[+] GitHub   : whisper-666
[+] InstaGram : _whisper.io_
[+] TeleGram : whisper_io
=======================''')
head={
    "Accept": "*/*",
    "Content-Type": "application/x-www-form-urlencoded",
    "Content-Length": "71",
    "Host": "apim.djezzy.dz",
    "Connection": "Keep-Alive",
    "Accept-Encoding": "gzip",
    "User-Agent": "okhttp/3.14.9"}
nmb='  '+input('[+] Number : ')
nmb=nmb.split('  0')[1]
print('=======================')
data=f'msisdn=213{nmb}&client_id=6E6CwTkp8H1CyQxraPmcEJPQ7xka&scope=smsotp'
dj=requests.post('https://apim.djezzy.dz/oauth2/registration',data=data,headers=head).json()
otp=input('[+] Code : ')
tdata=f'otp={otp}&mobileNumber=213784349358&scope=openid&client_id=6E6CwTkp8H1CyQxraPmcEJPQ7xka&client_secret=MVpXHW_ImuMsxKIwrJpoVVMHjRsa&grant_type=mobile'
token=requests.post('https://apim.djezzy.dz/oauth2/token',data=tdata,headers=head).json()['access_token']
print('=======================')
g2=f'https://apim.djezzy.dz/djezzy-api/api/v1/subscribers/213{nmb}/subscription-product?include\u003d'
ghead={
    "Accept": "application/json",
    "Authorization": f"Bearer {token}",
    "Content-Type": "application/json; charset\u003dutf-8",
    "Content-Length": "125",
    "Host": "apim.djezzy.dz",
    "Connection": "Keep-Alive",
    "Accept-Encoding": "gzip",
    "User-Agent": "okhttp/3.14.9"}
json={"data":{"id":"GIFTWALKWIN","type":"products","meta":{"services":{"steps":33570816,"code":"GIFTWALKWIN2GO","id":"WALKWIN"}}}}
go2=requests.post(g2,headers=ghead,json=json).json()['message']
print(go2)