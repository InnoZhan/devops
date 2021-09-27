""" This application returns Moscow time

Flask application listens to port 5000
on request it returns HTML page with Moscow time
"""

import datetime

import pytz
from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def get_time():
    """Returns html page with Moscow time

    Returns:
        str: HTML page
    """
    timezone = pytz.timezone("Europe/Moscow")
    server_time = datetime.datetime.now(timezone)
    print(str(server_time))
    visits = []
    with open("visits.txt", "r", encoding="utf-8") as file:
        visits = file.readlines()
    visits = visits[:100]
    visits.insert(0, str(server_time)+'\n')
    with open("visits.txt", "w", encoding="utf-8") as file:
        file.writelines(visits)
    html_response = render_template(
        "index.html", time=str(server_time.strftime("%H:%M:%S"))
    )
    return html_response


@app.route("/visits")
def get_visits():
    """Returns number of times root path was accessed

    Returns:
        int: number of times was accessed
    """
    visits = []
    with open("visits.txt", "r", encoding="utf-8") as file:
        visits = file.readlines()
    html_response = render_template(
        "visits.html", visits=visits
    )
    return html_response

if __name__ == "__main__":
    app.run(host="0.0.0.0")
