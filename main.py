from flask import Flask, request, jsonify
from datetime import datetime
import sys
app = Flask(__name__)

def main():
	try:
		if len(sys.argv) - 1 != 2:
			raise Exception("Incorrect input parameters")
		if sys.argv[1] != "--port":
			raise Exception("Port not specified")
		if not sys.argv[2].isdigit():
			raise Exception("Port isn't a number")
		if int(sys.argv[2]) not in range(1,65536):
			raise Exception("Incorrect port")
		app.run(host='0.0.0.0', port = int(sys.argv[2]))
	except Exception as e:
		print(e)
		sys.exit()

@app.route('/now')
def hello_world():
	prefix = request.args.get('prefix', type=str)
	return jsonify({prefix : str(datetime.now().strftime("%m/%d/%Y, %H:%M:%S"))})

if __name__ == "__main__":
	main()