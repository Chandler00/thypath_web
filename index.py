"""
****************************************
 * @author: Chandler Qian
 * Date: 2021-July
 * Project:
 * Purpose:
 * Python version: 3.8.1
 * Project root:
 * Environment package:
****************************************
"""
from flask import Flask

app = Flask(__name__)


@app.route("/")
def hello():
    return "init"


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
