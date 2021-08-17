# from package.MovieTable import create_movie_table, put_item
import boto3
import flask
import logging
import time
import os

application = flask.Flask(__name__)
MESSAGE = "HELLO, WORLD!\n"

@application.route('/')
def sts():
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

@application.route('/ddb')
def ddb():
  start = time.time()
  dynamodb = boto3.resource('dynamodb')
  while (time.time() - start < 300):
    try:
      tables = list(dynamodb.tables.all())
      return str(tables)
    except Exception as e:
      print(e)
      time.sleep(5)
      continue
  return "call failed"

if __name__ == '__main__':
	application.run(debug=True)
