from flask import Flask, request, jsonify
from datetime import datetime
app = Flask(__name__)

@app.route('/now')
def hello_world():
	prefix = request.args.get('prefix', type=str)
	return jsonify({prefix : str(datetime.now().strftime("%m/%d/%Y, %H:%M:%S"))})

def getPort():
	port = -1
	while port < 0 or port > 65535: 
		print("Input port in [0:65535]")
		port = int(input())
	return str(port)


if __name__ == "__main__":
	app.run(host='0.0.0.0', port = getPort())