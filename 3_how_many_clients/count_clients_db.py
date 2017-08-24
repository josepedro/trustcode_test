import xmlrpclib
import odoorpc

def count_clients():
    url = 'chocotech.trustcode.com.br'
    uid = 'demo'
    password = 'demo'
    odoo = odoorpc.ODOO(url, port=80)
    db_list = odoo.db.list()
    db = db_list[5]
    odoo.login(db, 'demo', 'demo')
    list_records = odoo.execute_kw('res.partner', 'search_count',[[['is_company', '=', True], ['customer', '=', True]]])
    return list_records

if __name__ == '__main__':
	count_clients()