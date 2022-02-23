# Copyright (c) 2022, Shweta and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document
from frappe import _

class Asset1(Document):
	def before_save(self):
		if self.asset_name:
			pass
	
		else:
			msg ="Please select the Asset"
			frappe.throw(_(msg))
