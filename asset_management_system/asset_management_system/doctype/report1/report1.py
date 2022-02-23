# Copyright (c) 2022, Shweta and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document
from frappe import _

class Report1(Document):
	def before_save(self):
		'''if self.owner == 'Shweta':
			doc = frappe.get_all('Owner',{'owner_name':self.owner},'asset')
			for row in doc:
				price = frappe.get_all('Asset1',{'asset_name':row.get('asset')},'price')
				self.append('assets',{'asset_name':row.get('asset'),'price':price[0].get('price')})
			total=[]
			for i in self.assets:
				total.append(i.get('price'))
		self.total_asset_value = sum(total)'''
		pass
	def validate(self):
		pass


	#def sum(self):
		#for add in self.Asset_():
		#	doc=frappe.get_value('')