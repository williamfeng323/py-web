import unittest
import json, pdb
from server.app import app, db, user_datastore, security
from bs4 import BeautifulSoup
# from server.configuration.config import basedir


class UserResources(unittest.TestCase):
    def setUp(self):
        db.drop_all()
        self.app = app.test_client()
        db.create_all()
        # pdb.set_trace()
        user_datastore.create_user(email='test@example.com', password='tesT123')
        db.session.commit()

    def tearDown(self):
        db.session.remove()
        db.drop_all()

    def get_csrf(self):
        login = self.app.get('/login')
        soup = BeautifulSoup(login.data, 'html.parser')
        return soup.find(id='csrf_token').get('value')

    def login(self, username, password):
        headers = {
            'GTA_CSRF_TOKEN': self.get_csrf(),
            'Content-Type': 'application/json'
        }
        return self.app.post('/login', data=json.dumps(dict(
            email=username,
            password=password,
        )), headers=headers, follow_redirects=True)

    def logout(self):
        return self.app.get('/logout', follow_redirects=True)

    def test_authorized_put(self):
        self.login('test@example.com', 'tesT123')
        response = self.app.put('/api/users')
        self.assertEqual(json.loads(response.get_data()), {'msg': 'function on the road!'})

    def test_unauthorized_put(self):
        response = self.app.put('/api/users')
        # self.assertEqual(json.loads(response.get_data()), {'msg': 'function on the road!'})
        self.assertEqual(response.status_code, 401)

    def test_authorized_get(self):
        user = user_datastore.find_user(email='test@example.com')
        self.login('test@example.com', 'tesT123')
        response = self.app.get('/api/users?email=test@example.com')
        self.assertEqual(response.status_code, 201)
        self.assertEqual(json.loads(response.data)['id'], user.id)

    def test_get_failed(self):
        self.login('test@example.com', 'tesT123')
        response = self.app.get('/api/users?email=notexist@example.com')
        self.assertEqual(json.loads(response.get_data()), {'msg': 'user not found'})

    def test_unauthorized_get(self):
        response = self.app.get('/api/users')
        self.assertEqual(response.status_code, 401)