# from package.MovieTable import create_movie_table, put_item
import boto3
import flask
import logging
import time
import os

application = flask.Flask(__name__)
MESSAGE = "HELLO, WORLD!\n"

@application.route('/')
def home():
  start = time.time()
  client = boto3.client('sts')
  while (time.time() - start < 300):
    try:
      identity = client.get_caller_identity()
      return identity['Arn']
    except Exception as e:
      print(e)
      time.sleep(5)
      continue

@application.route("/public")
def root1():
  hostname = "google.com"
  response = os.system("ping -c 1 " + hostname)
  print(response)
  if response == 0:
    print (hostname, 'is up!')
  else:
    print (hostname, 'is down!')

  msg = MESSAGE + hostname
  result = msg.encode("utf-8")
  return result

@application.route("/ip")
def root2():
  hostname = "192.30.255.112"
  response = os.system("ping -c 1 " + hostname)
  print(response)
  if response == 0:
    print (hostname, 'is up!')
  else:
    print (hostname, 'is down!')
  msg = MESSAGE + hostname
  result = msg.encode("utf-8")
  return result

@application.route("/aws")
def root3():
  client = boto3.client('sts')
  for i in range(10):
    try:
      identity = client.get_caller_identity()
      return identity['Arn']
    except Exception as e:
      print(e)
      time.sleep(1)
      continue

if __name__ == '__main__':
	application.run(debug=True)
