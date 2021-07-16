# from package.MovieTable import create_movie_table, put_item
import boto3
import flask
import logging
import time

application = flask.Flask(__name__)

@application.route('/')
def home():
	logging.basicConfig(level=logging.DEBUG)
	client = boto3.client('sts')
	for i in range(10):
		try:
			identity = client.get_caller_identity()
			return identity['Arn']
		except Exception as e:
			logging.error("Failed to get caller identity: " + str(e))
			time.sleep(1)
			continue

if __name__ == '__main__':
	application.run(debug=True)