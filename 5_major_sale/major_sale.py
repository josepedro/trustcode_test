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

def major_sale():
    list_ids = odoo.execute_kw('res.partner', 'search', [[['customer', '=', True]]])
    clients_total_bruto = {}
    for client_id in list_ids:
        [client] = odoo.execute_kw('res.partner', 'read', [client_id])
        sale_order_ids = client['sale_order_ids']
        totais_brutos = []
        for sale_order_id in sale_order_ids:
            [sale_order] = odoo.execute_kw('sale.order', 'read', [sale_order_id])
            totais_brutos.append(sale_order['total_bruto'])
        if totais_brutos != []:
            clients_total_bruto[client_id] = max(totais_brutos)
    clients_id_sorted_by_sale = sorted(clients_total_bruto, key=clients_total_bruto.get, reverse=True)
    client_id_major_sale = clients_id_sorted_by_sale[0]
    major_sale = clients_total_bruto[client_id_major_sale]
    partner = odoo.env['res.partner']
    name = partner.browse(int(client_id_major_sale)).name
    email = partner.browse(int(client_id_major_sale)).email
    phone = partner.browse(int(client_id_major_sale)).phone
    print("O cliente %s, com email %s e telefone %s obteve a maior venda feita no valor total de %s reais." % (name, email, phone, major_sale))

if __name__ == '__main__':
	major_sale()