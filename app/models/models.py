from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Report(db.Model):
	__tablename__ = 'reports'
	report_id = db.Column('id', db.Integer, primary_key=True)
	data = db.Column('data', db.String, nullable=False)