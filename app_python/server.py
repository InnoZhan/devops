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
    html_response = render_template(
        "index.html", time=str(server_time.strftime("%H:%M:%S"))
    )
    return html_response


if __name__ == "__main__":
    app.run()
