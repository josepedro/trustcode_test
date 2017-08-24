import odoorpc

def insert_client():
    odoo = odoorpc.ODOO('chocotech.trustcode.com.br', port=80)
    db_list = odoo.db.list()
    odoo.login(db_list[5], 'demo', 'demo')	
    partner = odoo.env['res.partner']
    partner.write([1], {'name': "Jose Pedro de Santana Neto", 
    	'email': "1jpsneto@gmail.com", 'phone': "61985909581"})

if __name__ == '__main__':
	insert_client()