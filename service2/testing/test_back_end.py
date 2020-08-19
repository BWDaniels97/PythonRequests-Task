import requests
import unittest

from flask import url_for

from flask_testing import TestCase

from application import app

class TestBase(TestCase):

    def create_app(self):
        return app


class TestViews(TestBase):

    def test_get_page(self):

        response = self.client.get(url_for('get_animal'))
        self.assertEqual(response.status_code, 200)

    def test_post_page(self):
        
        response = self.client.get(url_for('post_animal'))
        self.assertEqual(response.status_code, 200)
        
    
