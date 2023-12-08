# -*- coding: utf-8 -*-
# from odoo import http


# class DocumentModule(http.Controller):
#     @http.route('/document_module/document_module', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/document_module/document_module/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('document_module.listing', {
#             'root': '/document_module/document_module',
#             'objects': http.request.env['document_module.document_module'].search([]),
#         })

#     @http.route('/document_module/document_module/objects/<model("document_module.document_module"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('document_module.object', {
#             'object': obj
#         })

