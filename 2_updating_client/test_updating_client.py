import unittest
import odoorpc
import updating_client 

class UpdatingClientTestCase(unittest.TestCase):

    def test_update_client(self):
        odoo = odoorpc.ODOO('chocotech.trustcode.com.br', port=80)
        db_list = odoo.db.list()
        odoo.login(db_list[5], 'demo', 'demo')  
        partner = odoo.env['res.partner']
        id_partner = 1
        partner.write([id_partner], {'name': "Jose Pedro de Santana Neto", 
        'email': "1jpsneto@gmail.com", 'phone': "61985909581"})
        CPF = '19.145.271/0001-63'
        updating_client.update_client(id_partner, CPF)
        assert partner.browse(id_partner).cnpj_cpf == CPF, "Problem with CPF" 
        
if __name__ == '__main__':
	unittest.main()