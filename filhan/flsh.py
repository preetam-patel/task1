from flask import Flask 
app = Flask(__name__)

@app.route('/')
def app():
	return "doneeee"

if __name__ == "__main__":
	app.run( host = 'localhost', port = 5001)
