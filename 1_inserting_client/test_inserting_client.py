import unittest
import odoorpc

class InsertingClientTestCase(unittest.TestCase):

    def test_insert_client(self):
        odoo = odoorpc.ODOO('chocotech.trustcode.com.br', port=80)
        db_list = odoo.db.list()
        odoo.login(db_list[5], 'demo', 'demo')
        user = odoo.env.user
        print(user.name)            # name of the user connected
        print(user.company_id.name) # the name of its company
        # Simple 'raw' query
        user_data = odoo.execute('res.users', 'read', [user.id])
        print(user_data)
        print("===========================================================")
	    # Update data through a record
        #user.name = "Brian Jones"
        #user = odoo.env.user
        #print(user.name)

if __name__ == '__main__':
	unittest.main()