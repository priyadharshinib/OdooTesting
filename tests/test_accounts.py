# -*-coding: utf-8 -*-

from odoo.tests import common


class TestAccounts(common.TransactionCase):

 def test_create_data(self):
 #creating a test invoice 
   test_invoice = self.env['account.move'].create({
         "name":"Testing_invoice"})

 #checking if invoice is created
   self.assertEqual(test_invoice.name,"Testing_invoice")
   print("TEST PASSED")
