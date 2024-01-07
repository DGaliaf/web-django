from django.contrib.auth.models import User
from django.test import TestCase

from .forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm


# Create your tests here.

class UserRegisterFormTest(TestCase):
    def test_form_with_correct_data(self):
        form_data = {
            "username": "Username",
            "email": "myemail@mail.com",
            "password1": "testPassword",
            "password2": "testPassword",
        }

        form = UserRegisterForm(data=form_data)

        self.assertTrue(form.is_valid())

    def test_form_with_incorrect_email(self):
        form_data = {
            "username": "Username",
            "email": "myemail@.com",
            "password1": "testPassword",
            "password2": "testPassword",
        }

        form = UserRegisterForm(data=form_data)

        self.assertFalse(form.is_valid())


    def test_form_with_incorrect_password(self):
        form_data = {
            "username": "Username",
            "email": "myemail@mail.com",
            "password1": "testPassword3",
            "password2": "testPassword",
        }

        form = UserRegisterForm(data=form_data)

        self.assertFalse(form.is_valid())

    def test_form_with_incorrect_password2(self):
        form_data = {
            "username": "Username",
            "email": "myemail@mail.com",
            "password1": "testPassword",
            "password2": "testPassword3",
        }

        form = UserRegisterForm(data=form_data)

        self.assertFalse(form.is_valid())

    def test_form_with_incorrect_data(self):
        form_data = {
            "username": "Username",
            "email": "myemail@mailcom",
            "password1": "testPassword",
            "password2": "testPassword3",
        }

        form = UserRegisterForm(data=form_data)

        self.assertFalse(form.is_valid())


class UserUpdateFormTest(TestCase):
    def test_form_with_correct_data(self):
        form_data = {
            "username": "Username",
            "email": "myemail@mail.com",
        }

        form = UserUpdateForm(data=form_data)

        self.assertTrue(form.is_valid())

    def test_form_with_incorrect_email(self):
        form_data = {
            "username": "Username",
            "email": "myemail@.com",
        }

        form = UserUpdateForm(data=form_data)

        self.assertFalse(form.is_valid())

class ProfileUpdateFormTest(TestCase):
    def test_form_with_correct_data(self):
        form_data = {
            "name": "Name",
            "surname": "Surname",
            "lastName": "LastName",
            "phone": "79998884433",
        }

        form = ProfileUpdateForm(data=form_data)

        self.assertTrue(form.is_valid())

    def test_form_with_incorrect_name(self):
        form_data = {
            "name": "Na",
            "surname": "Surname",
            "lastName": "LastName",
            "phone": "79998884433",
        }

        form = ProfileUpdateForm(data=form_data)

        self.assertFalse(form.is_valid())

    def test_form_with_incorrect_surname(self):
        form_data = {
            "name": "Name",
            "surname": "Su",
            "lastName": "LastName",
            "phone": "79998884433",
        }

        form = ProfileUpdateForm(data=form_data)

        self.assertFalse(form.is_valid())

    def test_form_with_incorrect_lastName(self):
        form_data = {
            "name": "Name",
            "surname": "Surname",
            "lastName": "La",
            "phone": "79998884433",
        }

        form = ProfileUpdateForm(data=form_data)

        self.assertFalse(form.is_valid())

    def test_form_with_incorrect_phone(self):
        form_data = {
            "name": "Name",
            "surname": "Surname",
            "lastName": "LastName",
            "phone": "7999888443",
        }

        form = ProfileUpdateForm(data=form_data)

        self.assertFalse(form.is_valid())

    def test_form_with_incorrect_phone2(self):
        form_data = {
            "name": "Name",
            "surname": "Surname",
            "lastName": "LastName",
            "phone": "7999888443d",
        }

        form = ProfileUpdateForm(data=form_data)

        self.assertFalse(form.is_valid())
