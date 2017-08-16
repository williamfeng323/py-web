import unittest
import json
import sys, os
from server.app import db, user_datastore
from server.models.user import User
import pdb
# from server.configuration.config import basedir


class UserModels(unittest.TestCase):
    def setUp(self):
        # pdb.set_trace()
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()

    # def test_init_user(self):
    #     user = user_datastore.create_user(email='test@test.com', password='a')
    #     db.session.commit()
    #     # expected = User.query.filter_by(email='test@test.com').first()
    #     # self.assertEqual(user, expected)

    # def test_invalid_email(self):
    #     pass
    #
    # def test_invalid_password(self):
    #     pass
    #
    # def test_no_role_exception(self):
    #     pass