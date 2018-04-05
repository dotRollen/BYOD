employee_dict = {
    'employee':{
        'first_name':'John', 'last_name':'Doe', 'email':'john_doe@fake.com', 'phone':'123456789'
    }, 
    'devices': [
        {'model':'HP Laptop', 'serial':'123', 'asset_tag':'456'}, 
        {'model':'Surface Tablet', 'serial':'789', 'asset_tag':'000'}
    ]
}

# employee_dict = {
#     'employee':{
#         'first_name':'', 'last_name':'', 'email':'', 'phone':''
#     }, 
#     'devices': []
# }

# employee_dict['employee']['first_name'] = employee[0]
# employee_dict['employee']['last_name'] = employee[1]
# employee_dict['devices'].append({'model': employee[2], 'serial': employee[3], 'asset_tag': employee[4]})

# employee_entry(cursor, employee_dict)
# employee_lookup(cursor, employee_dict)
# device_entry(cursor, employee_dict)
# device_lookup(cursor, employee_dict)
# device_checkin(cursor, employee_dict)