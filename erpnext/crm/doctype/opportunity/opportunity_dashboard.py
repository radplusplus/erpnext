from frappe import _

def get_data():
	# 2017-01-19 - RM - Ajout de resquest for quotation dans les related documents de opportunity. Doit egalement ajouter custom field dans RFQ.
	return {
		'fieldname': 'prevdoc_docname',
		'non_standard_fieldnames': {
			'Supplier Quotation': 'opportunity',
			'Quotation': 'opportunity'
		},
		'transactions': [
			{
				'items': ['Quotation', 'Supplier Quotation', 'Request for Quotation']
			},
		]
	}