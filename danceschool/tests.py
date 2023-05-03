from http import HTTPStatus
from tp.wsgi import *
from PIL import Image
from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
from django.http import HttpRequest
from django.test import TestCase
from django.urls import reverse

from danceschool.forms import UserRegisterForm
from danceschool.models import Profile
from danceschool.views import edit


class CreateUserTest(TestCase):
    @classmethod
    def setUp(self):
        self.user1 = User.objects.create_user(username= 'alina' , password= 'alinapassword')
        self.client1 = Profile.objects.create(user = self.user1, photo = 'css/img/price1.png',phone = '899966365437',email = 'kns8@tpu.tu',visits = '0')
        self.user1.save()
        self.client1.save()

    def tearDown(self):
        self.client1.delete()
        self.user1.delete()

    def test_photo(self):
        print("\nPhoto test")
        self.assertEqual('css/img/price1.png', self.client1.photo)

    def test_phone(self):
        print("\nPhone test")
        self.assertEqual('899966365437', self.client1.phone)

    def test_email(self):
        print("\nEmail test")
        self.assertEqual('kns8@tpu.tu', self.client1.email)

    def test_username(self):
        print("\nUsername test")
        self.assertEqual('alina', self.client1.user.username)


class SignUpTest(TestCase):

    def test_correct_data(self):
        print("\nMethod: test_correct_data")
        form_data = {'username': 'Arkadii', 'password1': 'ThisIsStrongPassword',
                     'password2': 'ThisIsStrongPassword', 'phone': '899966365431', 'photo': "tp/static/css/img/jk.png", 'email':'kns8@iot.ru'}
        form = UserRegisterForm(data=form_data)
        self.assertTrue(form.is_valid())

    def test_non_unique_username(self):
        print("\nMethod: test_non_unique_username")
        form_data = {'username': 'non_unique', 'password1': 'ThisIsStrongPassword',
                     'password2': 'ThisIsStrongPassword', 'phone': '899966365431',
                     'photo': "tp/static/css/img/jk.png", 'email': 'kns8@iot.ru'}
        form = UserRegisterForm(data=form_data)
        self.assertTrue(form.is_valid())

    def test_non_unique_email(self):
        print("\nMethod: test_non_unique_email")
        form_data = {'username': 'unique', 'password1': 'ThisIsStrongPassword',
                     'password2': 'ThisIsStrongPassword', 'phone': '899966365431',
                     'photo': "tp/static/css/img/jk.png", 'email': 'nonunique@example.com'}
        form = UserRegisterForm(data=form_data)
        self.assertTrue(form.is_valid())

    def test_weak_password(self):
        print("\nMethod: test_weak_password")
        form_data = {'username': 'non_unique', 'password1': '1234',
                     'password2': '1234', 'phone': '899966365431',
                     'photo': "tp/static/css/img/jk.png", 'email': 'unique@example.com'}
        form = UserRegisterForm(data=form_data)
        self.assertFalse(form.is_valid())


class LogoutTestCase(TestCase):
    def test_logout(self):
        response = self.client.get(reverse("logout"))
        self.assertRedirects(response, reverse("home"))


# class EditProfileTestCase(TestCase):
#     @classmethod
#     def setUp(self):
#         self.user = get_user_model().objects.create_user(username='alina', password='alinapassword')
#         self.client1 = Profile.objects.create(user=self.user, photo='css/img/price1.png', phone='899966365437',
#                                         email='kns8@tpu.tu',
#                                         visits='0')
#         self.user.save()
#     @classmethod
#
#     def tearDown(self):
#         self.user.delete()
#         self.client1.delete()
#
#     def test_edit_profile(self):
#
#         self.client.post(
#             reverse("edit"),
#             {
#                 'photo': Image.open("tp/static/css/img/jk.png"),
#                 'username': 'alinka',
#                 'phone': '899966365438',
#                 'email': 'kns9@tpu.tu',
#             }
#         )
#         self.assertEqual('899966365438', self.client1.phone)
#         self.assertEqual('alinka', self.client1.user.username)
#         self.assertEqual('kns9@tpu.tu', self.client1.email)