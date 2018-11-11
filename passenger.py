#!/usr/bin/env python3.6

from flask import Flask, jsonify, request
from flask_restful import Resource, Api
from flaskext.mysql import MySQL
from healthcheck import HealthCheck
import yaml
import os

mysql = MySQL()
app = Flask(__name__)

# MySQL configurations
app.config['MYSQL_DATABASE_USER'] = os.getenv('MYSQL_USER')
app.config['MYSQL_DATABASE_PASSWORD'] = os.getenv('MYSQL_ROOT_PASSWORD')
app.config['MYSQL_DATABASE_DB'] = 'titanic'
app.config['MYSQL_DATABASE_HOST'] = os.getenv('MYSQL_HOST')
app.config['MYSQL_DATABASE_PORT'] = 3306

mysql.init_app(app)
api = Api(app)

@app.route('/')
def get():
	minage = request.args.get('minage', None)
	pclass = request.args.get('pclass', None)
	sex = request.args.get('sex', None)
	survived = request.args.get('survived', None)

	cur = mysql.connect().cursor()
	if (sex is not None and pclass is None and survived is not None and minage is None):
		cur.execute('''select * from titanic.passengers where passengers.sex = "%s" AND passengers.survived = %s''' %(sex, survived))
	elif (sex is None and pclass is None and survived is not None and minage is not None):
		cur.execute('''select * from titanic.passengers where passengers.age >= %s AND passengers.survived = %s''' %(minage, survived))
	else:
		cur.execute('''select * from titanic.passengers''')	
	
	r = [dict((cur.description[i][0], value) for i, value in enumerate(row)) for row in cur.fetchall()]
	return jsonify({'myCollection' : r})
   
health = HealthCheck(app, "/healthcheck")

def app_health():
		return True, "Health OK"

health.add_check(app_health)

if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0')
