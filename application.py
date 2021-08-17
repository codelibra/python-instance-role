# from package.MovieTable import create_movie_table, put_item
import boto3
import flask
import logging
import time
import os
import requests

application = flask.Flask(__name__)
MESSAGE = "HELLO, WORLD!\n"

@application.route("/")
def root1():
  hostname = "http://google.com"
  response = r = requests.get(hostname)

  msg = MESSAGE + hostname
  result = msg.encode("utf-8")
  return result

if __name__ == '__main__':
	application.run(debug=True)
