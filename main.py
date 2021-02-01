from flask import Flask, request, jsonify
from datetime import datetime
import sys
app = Flask(__name__)

def main():
	try:
		assert sys.argv[1] == "--port" and int(sys.argv[2]) in range(1,65536)
		app.run(host='0.0.0.0', port = int(sys.argv[2]))
	except:
		print("Incorrect input values")
		sys.exit()

@app.route('/now')
def hello_world():
	prefix = request.args.get('prefix', type=str)
	return jsonify({prefix : str(datetime.now().strftime("%m/%d/%Y, %H:%M:%S"))})

if __name__ == "__main__":
	main()