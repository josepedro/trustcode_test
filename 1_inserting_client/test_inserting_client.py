import unittest
import odoorpc
import inserting_client

class InsertingClientTestCase(unittest.TestCase):

    def test_insert_client(self):
        inserting_client.insert_client()
        odoo = odoorpc.ODOO('chocotech.trustcode.com.br', port=80)
        db_list = odoo.db.list()
        odoo.login(db_list[5], 'demo', 'demo')
        partner = odoo.env['res.partner']
        assert partner.browse(1).name == 'Jose Pedro de Santana Neto', "Problem with name" 
        assert partner.browse(1).email == '1jpsneto@gmail.com', "Problem with email"
        assert partner.browse(1).phone == '61985909581', "Problem with phone"
        
if __name__ == '__main__':
	unittest.main()