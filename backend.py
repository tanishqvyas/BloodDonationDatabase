from flask import Flask, render_template, request
from flask_mysqldb import MySQL


app = Flask(__name__)

app.config['MYSQL_USER'] = 'user'
app.config['MYSQL_PASSWORD'] = 'PASSWORD'
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_DB'] = 'dbms_project'
app.config['MYSQL_CURSORCLASS'] = 'DictCursor'

mysql = MySQL(app)

@app.route('/', methods=['post', 'get'])


def index():

	cur = mysql.connection.cursor()

	if request.method == 'POST':

		query = request.form['inputquery']
		try:
		
			cur.execute(query)
			results = cur.fetchall()
			mysql.connection.commit()
		
			if len(results) > 0:
				return render_template('index.html', results = results, show = 1, error = 0, msg='')
			else:

				return render_template("index.html", results = results, show = 0, error = 0, msg = 'No Rows Returned', myquery = query)

		except Exception as e:
			print("----------------------------------")
			print(e)
			print("----------------------------------")

			return render_template('index.html', results= (), show = 0, error = 1 ,msg= e, myquery = query)	

	else:
		return render_template('index.html', results = (), show = 0, error = 0, myquery = '')


if __name__ == '__main__':
	app.run(debug=True)