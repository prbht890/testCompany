# Generated by Django 3.1.1 on 2020-09-23 10:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('testapp', '0003_auto_20200923_1518'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='resume',
            field=models.ImageField(null=True, upload_to='documents/'),
        ),
    ]
