import unittest
import json
from server.app import app, db
# from server.configuration.config import basedir


class UserResources(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()

    def test_put(self):
        response = self.app.put('/api/users')
        print(response)
        self.assertEqual(json.loads(response.get_data()), {'msg': 'function on the road!'})
