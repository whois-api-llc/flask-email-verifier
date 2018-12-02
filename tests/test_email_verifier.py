from os import environ
from unittest import TestCase

from flask import Flask
from flask_email_verifier import EmailVerifier

CONFIG_KEY = "EMAIL_VERIFIER_KEY"


class TestSimpleGeoIP(TestCase):
    def setUp(self):
        self.app = Flask(__name__)

    def test_init_fails_with_no_config(self):
        api_key = environ.get(CONFIG_KEY)
        if api_key:
            del environ[CONFIG_KEY]

        with self.assertRaises(Exception):
            EmailVerifier(self.app)

        if api_key:
            environ[CONFIG_KEY] = api_key

    def test_init_works_with_environment_variable_config(self):
        environ[CONFIG_KEY] = "test"
        EmailVerifier(self.app)
        del environ[CONFIG_KEY]

    def test_init_works_with_variable_config(self):
        self.app.config[CONFIG_KEY] = "test"
        EmailVerifier(self.app)

        del self.app.config[CONFIG_KEY]

    def test_get_geoip_data(self):
        with self.app.test_request_context():
            email_verifier = EmailVerifier(self.app)
            data = email_verifier.verify('test.email@gmail.com')
            self.assertIsInstance(data, object)
