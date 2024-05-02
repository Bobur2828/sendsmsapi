import os 
import requests 

FAILED=400   
SUCCESS = 200
PROCESSING = 102

ESKIZ_EMAIL="islomjonabduganiyev18482@gmail.com"
ESKIZ_PASSWORD="FzZntPmZRXANDah7KGE8V1AS84P8RD6NZfGGqi49"


class SendSms:
    def __init__(self,message,phone,email=ESKIZ_EMAIL,password=ESKIZ_PASSWORD):
        self.message=message
        self.phone=phone
        self.spend=None
        self.email=email
        self.password=password

    def send(self):
        rsult=self.send_messege(self.message)
        return rsult
    

    def authorization(self):
        data={
            'email':self.email,
            'password':self.password

        }
        AUTHORIZATION_URL="http://notify.eskiz.uz/api/auth/login"
        r=requests.request('POST',AUTHORIZATION_URL,data=data)
        if r.json()['data']['token']:
            return r.json()['data']['token']
        return FAILED
    
    def send_messege(self,message):
        token=self.authorization()
        if token==FAILED:
            return FAILED
        
        SEND_SMS_URL="http://notify.eskiz.uz/api/message/sms/send"

        PAYLOAD={
            "mobile_phone":'998'+str(self.phone),
            "message":message,
            'from':'4546',
        }

        FILES=[

        ]
        HEADERS={
            'Authorization':f'Bearer {token}'
        }

        r=requests.request("POST",SEND_SMS_URL, headers=HEADERS,data=PAYLOAD,files=FILES)
        return r.status_code
    
# # message=" Bu Eskiz dan test"
# phone=916624222
# e_api=SendSms(message=message,phone=phone)
# r=e_api.send()
# print(r)




class SendSms_with:
    def __init__(self,message,phone,email,password):
        self.message=message
        self.phone=phone
        self.spend=None
        self.email=email
        self.password=password

    def send(self):
        rsult=self.send_messege(self.message)
        return rsult
    

    def authorization(self):
        data={
            'email':self.email,
            'password':self.password

        }
        AUTHORIZATION_URL="http://notify.eskiz.uz/api/auth/login"
        r=requests.request('POST',AUTHORIZATION_URL,data=data)
        if r.json()['data']['token']:
            return r.json()['data']['token']
        return FAILED
    
    def send_messege(self,message):
        token=self.authorization()
        if token==FAILED:
            return FAILED
        
        SEND_SMS_URL="http://notify.eskiz.uz/api/message/sms/send"

        PAYLOAD={
            "mobile_phone":'998'+str(self.phone),
            "message":message,
            'from':'4546',
        }

        FILES=[

        ]
        HEADERS={
            'Authorization':f'Bearer {token}'
        }

        r=requests.request("POST",SEND_SMS_URL, headers=HEADERS,data=PAYLOAD,files=FILES)
        return r.status_code
    