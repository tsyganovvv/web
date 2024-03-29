from flask import Flask, render_template, url_for, request, redirect, flash
from db_sneacers import db_sneacers


app = Flask(__name__)
app.config['SECRET_KEY'] = 'wudbuwSSle*5#@$LLLkdsdf$#1s'


db = []
list_sneacers = db_sneacers("sneacers.txt")


@app.route('/', methods=['POST', 'GET'])
def index():
	if request.method == 'POST':
		address = request.form['address']
		password = request.form['password']
		user = {'address' : address,
				'password': password}
		if user in db:
			return redirect('/home')
		if user not in db:
			for userDB in db:
				if userDB['address'] == address:
					flash("password is not correct")
					return redirect('/')
			db.append(user)
			return redirect('/home')

	return render_template('index.html')


@app.route('/home', methods=['POST', 'GET'])
def home():
	return render_template('home.html')


@app.route('/shop', methods=['GET', 'POST'])
def shop():
	return render_template('shop.html', list_sneacers = list_sneacers, len = len(list_sneacers))


@app.route('/neural_network', methods=['POST', 'GET'])
def neural_network():
	return render_template('neural_network.html')


@app.route('/about', methods=['GET'])
def about():
	return render_template('about.html')


if __name__ == "__main__":
	app.run(debug=True)
