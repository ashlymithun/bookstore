from odoo import fields, models


class SaleReport(models.TransientModel):
    _name = "bookstore.sale.report"
    _description = "sales report"

    student_id = fields.Many2one('res.partner', string="Student")
    from_date = fields.Date(string="Start date")
    to_date = fields.Date(string="End date")

    def get_report(self):
        print('clicked',self.student_id)
        domain = []
        if self.student_id.id:
            domain += [('name','=',self.student_id.id)]
        if self.from_date:
            domain += [('date_of_issue','>=',self.from_date)]
        if self.to_date:
            domain += [('date_of_issue','<=',self.to_date)]
        print("from date",self.from_date)
        print("to date",self.to_date)
        result = self.env['bookstore.store'].search_read(domain)
        if result:
            print('true')
        else:
            print('false')
        data = {
            'rec': result
        }
        return self.env.ref('bookstore.action_report_bookstore_sale').report_action(self, data=data)
