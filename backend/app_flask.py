from flask import Flask

app = Flask(__name__)

@app.route("/")
def root():
	return {
		"response": 200,
		"message": "API is working !"
	}

if __name__ == '__main__':
	app.run(debug=True, host='127.0.0.1', port=2250)
