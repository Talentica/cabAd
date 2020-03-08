#!/usr/bin/env python3
import os
import django
import sys


def main():
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'cabAd.settings')
    django.setup()
    print('---------start------------\n')

    import setup_util

    execute_migrations()
    setup_util.create_default_groups()
    setup_util.create_super_user()
    setup_util.create_default_admin()


def execute_migrations():
    make_migration = os.system("python manage.py migrate")
    print("\nmigrations ran with exit code %d" % make_migration)
    if make_migration != 0:
        sys.exit("migrations not successful")


if __name__ == '__main__':
    main()
