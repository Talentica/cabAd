from django.contrib.auth.models import Group, Permission
from django.db.utils import IntegrityError
import os
from main.models.user import User


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
    user = User.objects.create_user(username='test', password='test123', is_staff=True, office='iriz', team=1)
    admin = Group.objects.get(name='admin')
    user.groups.add(admin)
    print("\ndefault admin created with username=test, password=test123")