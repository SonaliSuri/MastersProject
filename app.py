from concurrent.futures import ThreadPoolExecutor
from multiprocessing.pool import ThreadPool
from flask import jsonify
from flask import Flask
import requests
import datetime
import random
import time

urls = []
total_number = 3
promise_number = 0
max_ts = datetime.datetime.now()

accepted_ts, accepted_val = None, None
current_ts, current_val = None, None
prev_ts, prev_val = None, None
port = "1050"

us_east_1 = "ec2-54-226-195-115.compute-1.amazonaws.com"
us_east_2 = "ec2-3-138-202-205.us-east-2.compute.amazonaws.com"
us_west_1 = "ec2-54-241-144-146.us-west-1.compute.amazonaws.com"

propose_urls = list([])
propose_urls.append("http://"+us_east_1+":1050/prepare/")
propose_urls.append("http://"+us_east_2+":1050/prepare/")
propose_urls.append("http://"+us_west_1+":1050/prepare/")


accept_urls = list([])
accept_urls.append("http://"+us_east_1+":1050/accept/")
accept_urls.append("http://"+us_east_2+":1050/accept/")
accept_urls.append("http://"+us_west_1+":1050/accept/")


app = Flask(__name__)


def send_prep(yr, mon, day, hr, minute, sec, micro_sec, value, num):
    global port
    yr, mon, day = str(yr), str(mon), str(day)
    hr, minute, sec, micro_sec, value = str(hr), str(minute), str(sec), str(micro_sec), str(value)

    global propose_urls
    sl, host = "/", propose_urls[num]
    url = host + yr + sl + mon + sl + day + sl + hr + sl + minute + sl + sec + sl + micro_sec + sl + value
    response = requests.post(url=url)
    return response


def send_accept(yr, mon, day, hr, minute, sec, micro_sec, value, num):
    yr, mon, day = str(yr), str(mon), str(day)
    hr, minute, sec, micro_sec, value = str(hr), str(minute), str(sec), str(micro_sec), str(value)

    global port
    sl, host = "/", "http://0.0.0.0:" + str(port) + "/accept/"
    host = accept_urls[num]
    url = host + yr + sl + mon + sl + day + sl + hr + sl + minute + sl + sec + sl + micro_sec + sl + value
    response = requests.post(url=url)
    print(response)
    return response


@app.route('/propose')
def propose():
    print("Propose Started =", time.time())
    ts = datetime.datetime.now()

    global max_ts
    max_ts = ts

    year, month, day = ts.year, ts.month, ts.day
    hr, minute, sec, micro_sec = ts.hour, ts.minute, ts.second, ts.microsecond
    value = random.randint(0, 100)

    args = (
        (year, month, day, hr, minute, sec, micro_sec, value, 0),
        (year, month, day, hr, minute, sec, micro_sec, value, 1),
        (year, month, day, hr, minute, sec, micro_sec, value, 2)
    )

    replies = []
    with ThreadPoolExecutor(max_workers=3) as executor:
        for reply in executor.map(lambda p: send_prep(*p), args):
            replies.append(reply)

    print("Propose Ended =", time.time())

    for reply in replies:
        if reply.status_code == 200:
            global promise_number
            promise_number += 1

    print("prepare =", replies)
    print("prepare promise_number =", promise_number)

    replies = []
    print("Accept Started =", time.time())
    if promise_number >= total_number // 2:
        with ThreadPoolExecutor(max_workers=3) as executor:
            for reply in executor.map(lambda p: send_accept(*p), args):
                replies.append(reply)

    print("accept =", replies)
    print("Accept Ended =", time.time())
    return 'Hello World !!!'


@app.route('/prepare/<yr>/<mon>/<day>/<hr>/<minute>/<sec>/<micro_sec>/<val>')
def prepare(yr, mon, day, hr, minute, sec, micro_sec, val):
    dash = "-"
    colon = ":"
    date_string = yr + dash + mon + dash + day + " " + hr + colon + minute + colon + sec + "." + micro_sec
    ts = datetime.datetime.strptime(date_string, "%Y-%m-%d %H:%M:%S.%f")

    global current_ts
    global current_val

    global prev_ts
    global prev_val

    # current_ts, current_val = ts, val  # ignore
    # prev_ts, prev_val = ts, val  # ignore
    if current_ts is None:
        current_ts, current_val = ts, val

    elif ts > current_ts:
        prev_ts, prev_val = current_ts, current_val
        current_ts, current_val = ts, val
        return "True"

    elif ts > prev_ts:
        prev_ts, prev_val = ts, val
        return "False"

    return "False"


@app.route('/accept/<yr>/<mon>/<day>/<hr>/<minute>/<sec>/<micro_sec>/<val>')
def accept(yr, mon, day, hr, minute, sec, micro_sec, val):
    global current_ts
    global current_val
    global accepted_ts
    global accepted_val

    dash = "-"
    colon = ":"
    date_string = yr + dash + mon + dash + day + " " + hr + colon + minute + colon + sec + "." + micro_sec
    ts = datetime.datetime.strptime(date_string, "%Y-%m-%d %H:%M:%S.%f")

    if current_ts == ts:
        accepted_ts = ts
        accepted_val = val
        return "True"
    return "False"


@app.route('/send_prep', methods=['POST'])
def get_tasks():

    return jsonify({'tasks': 'tasks'})

char_size = input()
port = "1050"
app.run(host='0.0.0.0', port=port)
