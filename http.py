from flask import Flask, request,Response


app = Flask(__name__)



@app.route('/')
def test_1():
	return 'OK'



if __name__=='__main__':
	app.run(debug=False,host="188.166.80.84", port=8080)
