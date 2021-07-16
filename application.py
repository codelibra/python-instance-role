# from package.MovieTable import create_movie_table, put_item
import boto3
import flask
from botocore.exceptions import EndpointConnectionError

application = flask.Flask(__name__)

@application.route('/')
def home():
	client = boto3.client('sts')
	for i in range(10):
		try:
			identity = client.get_caller_identity()
			return identity['Arn']
		except EndpointConnectionError:
			time.sleep(1)
			continue
	identity = client.get_caller_identity()
	return identity['Arn']

if __name__ == '__main__':
	application.run(debug=True)