# Generated by Django 3.2.3 on 2022-12-14 17:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('system', '0003_alter_employee_certificate_expire_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='certification_body',
            field=models.CharField(blank=True, help_text='认证机构', max_length=100, null=True, verbose_name='认证机构'),
        ),
    ]
