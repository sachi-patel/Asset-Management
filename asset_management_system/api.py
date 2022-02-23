import frappe

@frappe.whitelist()
def get_asset_name(x):
    doc = frappe.get_all('Owner',{'owner_name':x},'asset')
    return doc