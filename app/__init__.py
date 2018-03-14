import os
from flask import Flask, make_response

from app.models.models import db
from app.apis.report import api

def create_app(config_module=None):

	app = Flask(__name__)
	app.config.from_object(config_module or os.environ.get('FLASK_CONFIG') or 'config')
	db.init_app(app)

	app.register_blueprint(api)

	@app.route('/')
	def index():
		response = make_response('Suade Challenge by vaugustine !!!')
		response.headers['Content-Type'] = 'text/plain'

		return response

	return app