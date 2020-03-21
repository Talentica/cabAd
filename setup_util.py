from django.contrib.auth.models import Group, Permission
from django.db.utils import IntegrityError
import os
from main.models import User


def create_default_groups():
    groups = ['super_admin', 'admin', 'manager', 'member']
    print('\ncreate default groups')
    for i in groups:
        group = Group(name=i)
        try:
            group.save()
            print("group inserted %s" % group.name)
        except IntegrityError:
            print('group already exists %s' %i)


def create_super_user():
    print("\nenter super user details:")
    super_user_created = os.system("python manage.py createsuperuser")
    if super_user_created == 0:
        super_user = User.objects.all().last()
        super_admin = Group.objects.get(name='super_admin')
        super_admin.user_set.add(super_user)


def create_default_admin():
    password = User.objects.make_random_password()
    username = 'test15'
    try:
        user = User.objects.create_user(username, password=password, is_staff=True, office='iriz')
        admin = Group.objects.get(name='admin')
        user.groups.add(admin)
        print(f"\ndefault admin created with username={username}, password={password}")
    except IntegrityError:
        print(f'\nuser already exists {username}')