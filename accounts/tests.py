from django.test import TestCase


# from accounts.models import User


class UserModelTests(TestCase):
    user_id = 'chanyou0311'
    user_name = 'ちゃんゆー'
    password = 'hogehoge'

    def test_user_save_ok(self):
        user = User(user_id=self.user_id, user_name=self.user_name, password=self.password)
        user.save()

        user_instance = User.objects.get(user_id=self.user_id)
        self.assertEqual(self.user_name, user_instance.user_name)

