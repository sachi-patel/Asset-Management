// Copyright (c) 2022, Shweta and contributors
// For license information, please see license.txt

frappe.ui.form.on('Report1',{
	 
	 before_save:function(frm){
         frappe.call({
             method:'asset_management_system.api.get_asset_name',
            args:{
                x: frm.doc.owner
            },
            callback: function(x){
                console.log("r is: ",x)
                console.log(x.message)
                console.log(x.message[0])
                console.log(x.message[0].asset)
                for(let i=0;i<x.message.length;i++){
                    frm.add_child('assets',{'asset_name':x.message[i].asset})
                }
            }
        })
    }



});
		

