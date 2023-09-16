from odoo import fields, models


class SearchRecord(models.AbstractModel):
    _name = "bookstore.search"
    _description = "book search"

    def search_methods(self):
        print("hello")
        domain = []
        domain += [('user_id','!=',self.env.user.id)]
        result = self.env['sale.order'].search_read(domain)
        for x in result:
            print(x['user_id'][1]+" =>",x)

