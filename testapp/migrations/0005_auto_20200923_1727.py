# Generated by Django 3.1.1 on 2020-09-23 11:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('testapp', '0004_auto_20200923_1537'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='dob',
            field=models.DateField(null=True),
        ),
        migrations.AlterField(
            model_name='employeeeducationdetail',
            name='college_end_month',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='employeeeducationdetail',
            name='college_end_year',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='employeeeducationdetail',
            name='college_start_month',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='employeeeducationdetail',
            name='college_start_year',
            field=models.IntegerField(null=True),
        ),
    ]