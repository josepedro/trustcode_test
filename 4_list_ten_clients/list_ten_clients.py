import xmlrpclib
import odoorpc
import string
import random

url = 'chocotech.trustcode.com.br'
uid = 'demo'
password = 'demo'
odoo = odoorpc.ODOO(url, port=80)
db_list = odoo.db.list()
db = db_list[5]
odoo.login(db, 'demo', 'demo')

def list_ten_clients():
    list_ids = odoo.execute_kw('res.partner', 'search', [[['customer', '=', True]]])
    clients_names = []
    i = 1
    for client_id in list_ids:
        [client] = odoo.execute_kw('res.partner', 'read', [client_id]) 
        clients_names.append(client['name'])
        i += 1
        if i == 10:
            break
    sorted_clients = sorted(clients_names)
    print sorted_clients

if __name__ == '__main__':
	list_ten_clients()