import datetime

import pytz
import requests
from bs4 import BeautifulSoup


def time_check():
    r = requests.get("http://127.0.0.1:5000")
    soup = BeautifulSoup(r.text, "html.parser")

    time_respose = soup.find("h1", id="time-holder").text
    time_respose = datetime.datetime.strptime(time_respose, "%H:%M:%S")

    timezone = pytz.timezone("Europe/Moscow")
    server_time = datetime.datetime.now(timezone)
    real_time = str(server_time.strftime("%H:%M:%S"))
    real_time = datetime.datetime.strptime(real_time, "%H:%M:%S")

    print((time_respose - real_time).seconds < 1)
    return True


def test_answer():
    assert time_check()
