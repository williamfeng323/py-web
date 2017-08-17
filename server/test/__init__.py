import os, sys
from functools import reduce
from unittest import TestSuite
from server.test.resources.users_resource_test import UserResources
from server.test.models.user_model_test import UserModels
os.environ['APP_SETTINGS'] = 'server.configuration.config.TestingConfig'
os.environ['DATABASE_URL'] = "@localhost/GTA-TEST"
os.environ['DATABASE_USER'] = "william"
os.environ['DATABASE_PASSWORD'] = "devil323"

test_cases = [UserResources, UserModels]


def load_tests(loader, tests, pattern):
    suite = TestSuite()
    for test_class in test_cases:
        tests = loader.loadTestsFromTestCase(test_class)
        suite.addTests(tests)
    return suite
