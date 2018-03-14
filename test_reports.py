import unittest
import json

from app import create_app
from app.models.models import db, Report

class ReportsTestCase(unittest.TestCase):

	report_id = 1
	data = {
	    "created_at": "2015-04-22",
	    "inventory": [
	        {
	            "name": "paper",
	            "price": "2.00"
	        },
	        {
	            "name": "stapler",
	            "price": "5.00"
	        },
	        {
	            "name": "printer",
	            "price": "125.00"
	        },
	        {
	            "name": "ink",
	            "price": "3000.00"
	        }
	    ],
	    "organization": "Dunder Mifflin",
	    "reported_at": "2015-04-21"
	}
	
	def setUp(self):
		self.app = create_app('test_config')

		self.ctx = self.app.app_context()
		self.ctx.push()

		db.create_all()
		r = Report(report_id=self.report_id, data=json.dumps(self.data))
		db.session.add(r)
		db.session.commit()

		self.client = self.app.test_client()

	def tearDown(self):
		db.session.remove()
		db.drop_all()
		self.ctx.pop()

	def test_home_page(self):

		rv = self.client.get('/')
		self.assertEqual(rv.status_code, 200)
		self.assertEqual(rv.headers['Content-Type'], 'text/plain')
		self.assertEqual(rv.data, b'Suade Challenge by vaugustine !!!')

	def test_report_json(self):
		rv = self.client.get('/reports/1')
		self.assertEqual(rv.status_code, 200)
		self.assertEqual(rv.headers['Content-Type'], 'application/json')

		data = json.loads(rv.data)
		self.assertTrue('organization' in data)
		self.assertTrue('reported_at' in data)
		self.assertTrue('created_at' in data)
		self.assertTrue('inventory' in data)


	def test_report_xml(self):
		rv = self.client.get('/reports/1?format=xml')
		self.assertEqual(rv.status_code, 200)
		self.assertEqual(rv.headers['Content-Type'], 'application/xml')

	def test_report_pdf(self):
		rv = self.client.get('/reports/1?format=pdf')
		self.assertEqual(rv.status_code, 200)
		self.assertEqual(rv.headers['Content-Type'], 'application/pdf')

	def test_report_not_found(self):
		rv = self.client.get('/reports/2')
		self.assertEqual(rv.status_code, 404)


if __name__ == '__main__':
	unittest.main()
