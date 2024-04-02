import requests
def send_otp_code(phone_number, code):
    print(phone_number)
    headers = {"ACCEPT": "application/json","X-API-KEY": "zSoNE0KakXxIJ1Ch9XfFL8HrOqXxCjPhn50hp3uYjuh5h8tzYdT0KNsKm7XZWMtO"}

    data = {
        "Mobile": str(phone_number),
        "TemplateId": 100000,
        "Parameters": [
            {
                "Name": "Code",
                "Value": code,
            }
        ]
    }

    res = requests.post(url="https://api.sms.ir/v1/send/verify", headers=headers, json=data)

    print(res.reason)

