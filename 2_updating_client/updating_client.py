import odoorpc

def update_client(id_partner, CPF):
    odoo = odoorpc.ODOO('chocotech.trustcode.com.br', port=80)
    db_list = odoo.db.list()
    odoo.login(db_list[5], 'demo', 'demo')	
    partner = odoo.env['res.partner']
    partner.write([id_partner], {'cnpj_cpf': CPF})

if __name__ == '__main__':
	insert_client()