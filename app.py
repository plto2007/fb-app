from flask import *
from requests import get
import wget


app = Flask(__name__)


@app.route("/")
def main():
 return "{url: 'https://www.privacypolicies.com/live/3c7506eb-0d85-42e2-a1bf-808e58ac90bd', confirmation_code: '1'}"


if __name__ == '__main__':
  app.run()
