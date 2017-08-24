import unittest
import odoorpc
import count_clients_db

class CountClientsTestCase(unittest.TestCase):

    def test_count_clients(self):
        number_total_clients = 12
        assert count_clients_db.count_clients() == number_total_clients, "Problem with total clients" 
        
if __name__ == '__main__':
	unittest.main()