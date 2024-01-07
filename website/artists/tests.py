from django.test import TestCase

from .forms import SubscriberForm


# Create your tests here.
class SubscriberFormTest(TestCase):
    def test_form_with_correct_data(self):
        form_data = {
            "email": "testemail@email.com",
            "phone": "79998884433",
            "receive_adv": True,
        }

        form = SubscriberForm(data=form_data)

        self.assertTrue(form.is_valid())

    def test_form_with_incorrect_email(self):
        form_data = {
            "email": "testemail@.com",
            "phone": "79998884433",
            "receive_adv": True,
        }

        form = SubscriberForm(data=form_data)

        self.assertFalse(form.is_valid())

    def test_form_with_incorrect_phone(self):
        form_data = {
            "email": "testemail@email.com",
            "phone": "7999888443",
            "receive_adv": True,
        }

        form = SubscriberForm(data=form_data)

        self.assertFalse(form.is_valid())

    def test_form_with_incorrect_phone2(self):
        form_data = {
            "email": "testemail@email.com",
            "phone": "7999888443d",
            "receive_adv": True,
        }

        form = SubscriberForm(data=form_data)

        self.assertFalse(form.is_valid())
