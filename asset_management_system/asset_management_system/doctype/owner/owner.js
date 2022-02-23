// Copyright (c) 2022, Shweta and contributors
// For license information, please see license.txt

frappe.ui.form.on('Owner', {
	 refresh: function(frm) {
		frm.set_query('asset', () => {
            return {
                filters: {
                    available: ['in',['1']]
                }
            }
    })
	 }
});
