from odoo import models, fields, api

class Document(models.Model):
    _name = 'document_module.document'
    _description = 'Document Model'

    name = fields.Char(string='Title', required=True)
    description = fields.Text(string='Description')
    company = fields.Char(string='Company')
    creator_user_id = fields.Many2one('res.users', string='Created By', default=lambda self: self.env.user)
    responsible_employee_ids = fields.Many2many('res.users', string='Responsible Employees')
    created_date = fields.Date(string='Created Date', default=fields.Date.today)