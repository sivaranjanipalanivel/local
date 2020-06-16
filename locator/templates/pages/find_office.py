from __future__ import unicode_literals
import frappe
from frappe import _
from urllib.parse import unquote

def get_context(context):
	print("----print")
	filters = {"type":"Office"}
	if frappe.form_dict.state:
		filters["state"] = frappe.form_dict.state
	if frappe.form_dict.city:
		filters["city"] = frappe.form_dict.city
	print(filters)
	location = frappe.db.get_all('Locations',filters= filters,fields=['*'],order_by='name desc')
	context.locations = location
	state = frappe.db.get_all('State',fields=['*'],order_by='name desc')
	context.states = state
	city = frappe.db.get_all('City',fields=['*'],order_by='name desc')
	context.citys = city