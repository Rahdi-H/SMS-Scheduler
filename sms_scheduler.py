import requests
import schedule
import time

def send_sms():
    resp = requests.post('https://textbelt.com/text', {
        'phone' : '+8801778124049',
        'message' : 'hello mithun',
        'key' : 'texbelt',
    })
    print(resp.json)

schedule.every().day.at('06:00').do(send_sms)

while True:
    schedule.run_pending()
    time.sleep(1)