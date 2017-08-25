import xmlrpclib
import odoorpc

url = 'chocotech.trustcode.com.br'
uid = 'demo'
password = 'demo'
odoo = odoorpc.ODOO(url, port=80)
db_list = odoo.db.list()
db = db_list[5]
odoo.login(db, 'demo', 'demo')

def sales_percentage():
    list_ids_done = odoo.execute_kw('sale.order', 'search', [[['state', '=', 'done']]])
    list_ids_draft = odoo.execute_kw('sale.order', 'search', [[['state', '=', 'draft']]])
    list_ids_sent = odoo.execute_kw('sale.order', 'search', [[['state', '=', 'sent']]])
    list_ids_sale = odoo.execute_kw('sale.order', 'search', [[['state', '=', 'sale']]])
    total_orders_open = len(list_ids_draft) + len(list_ids_sent) + len(list_ids_sale)
    total_orders_closed = len(list_ids_done)
    total_orders = total_orders_open + total_orders_closed
    percentage_orders_closed = 0
    if total_orders != 0:
        percentage_orders_closed = (float(total_orders_closed)/float(total_orders))*100
    print("O percentual de fechamento de vendas eh de %s%%." % percentage_orders_closed)

if __name__ == '__main__':
	sales_percentage()