from django.core.management import BaseCommand

from users.models import User


class Command(BaseCommand):
    def handle(self, *args, **options):
        users_data = [
            {
                'email': 'user1@site.ru',
                'first_name': 'User',
                'last_name': 'One',
                'phone_number': '+7(999)000-11-11',
                'is_active': False,
                'password': '1248dkfdknwjrns'
            },
            {
                'email': 'user2@site.ru',
                'first_name': 'User',
                'last_name': 'Two',
                'phone_number': '+7(999)000-22-22',
                'is_active': True,
                'password': 'knsdkfns32421'
            },
            {
                'email': 'user3@site.ru',
                'first_name': 'User',
                'last_name': 'Three',
                'phone_number': '+7(999)000-33-33',
                'is_active': True,
                'password': '3421eksmnsncvsa'
            },
            {
                'email': 'user4@site.ru',
                'first_name': 'User',
                'last_name': 'Four',
                'phone_number': '+7(999)000-44-44',
                'is_active': True,
                'password': 'nqeofhj9qfnq25w'
            },
            {
                'email': 'user5@site.ru',
                'first_name': 'User',
                'last_name': 'Five',
                'phone_number': '+7(999)000-55-55',
                'is_active': False,
                'password': '93u1rh9fh2nq93'
            },
        ]

        user_list = []

        for item in users_data:
            user_list.append(User(**item))

        User.objects.bulk_create(user_list)