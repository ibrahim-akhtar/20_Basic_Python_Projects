# Project 17
# Python Automation

# install schedule through terminal, command being 'pip install schedule'
# install requests library, command 'pip install requests'

# enter your phone number
ph_no = '<phone number>'

import requests
import schedule
import time

def send_message():
    resp = requests.post('https://textbelt.com/text', {
        'phone' : ph_no,
        'message' : 'Good Morning!!!',
        'key' : 'textbelt'
    })
    print(resp.json())

#schedule.every().day.at('09:00').do(send_message)    #follows 24 hour format: 1pm-13:00

#for testing phase: <to send messages right now at 3 sec interval>
schedule.every(3).seconds.do(send_message)
while True:
    schedule.run_pending()
    time.sleep(1)

# this might not send messages to your phone
# main purpose is to understand the schedule library and how to schedule tasks
