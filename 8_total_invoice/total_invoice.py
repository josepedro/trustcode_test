import odoorpc

url = 'chocotech.trustcode.com.br'
uid = 'demo'
password = 'demo'
odoo = odoorpc.ODOO(url, port=80)
db_list = odoo.db.list()
db = db_list[5]
odoo.login(db, 'demo', 'demo')

def total_invoice():
    list_ids_invoice_paid = odoo.execute_kw('account.invoice', 'search', [[['state', '=', 'paid']]])
    total_value_invoice_jun_2017 = 0
    for invoice_paid_id in list_ids_invoice_paid:
        [invoice_paid] = odoo.execute_kw('account.invoice', 'read', [invoice_paid_id])
        value_invoice = invoice_paid['amount_total']
        date_invoice = invoice_paid['date_invoice']
        month_invoice = date_invoice.split('-')[1]
        year_invoice =  date_invoice.split('-')[0]
        if month_invoice == '06' and year_invoice == '2017':
            total_value_invoice_jun_2017 += float(value_invoice)
    print("O valor em R$ total de faturas para o mes de Junho de 2017: %s" % (total_value_invoice_jun_2017))

if __name__ == '__main__':
	total_invoice()