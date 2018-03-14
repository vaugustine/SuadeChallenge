from flask import jsonify, request, render_template, make_response
from weasyprint import HTML
from dicttoxml import dicttoxml
import json

from app.apis import api
from app.models.models import db, Report


@api.route('/reports/<int:report_id>', methods=['GET'])
def generate_report(report_id):
	style = request.args.get('format','')
	report = db.session.query(Report).get_or_404(report_id)
	data = json.loads(report.data)

	if style=='pdf':

		rendered = render_template('report_template.html', **data)
		pdf = HTML(string=rendered).write_pdf()

		response = make_response(pdf)
		response.headers['Content-Type'] = 'application/pdf'
		response.headers['Content-Disposition'] = 'inline'

		return response

	elif style=='xml':

		xml = dicttoxml(data, custom_root='report', attr_type=False)

		response = make_response(xml)
		response.headers['Content-Type'] = 'application/xml'

		return response

	else:
		return jsonify(data)