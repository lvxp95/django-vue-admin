# Generated by Django 3.2.3 on 2022-12-14 15:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('system', '0002_auto_20221214_1205'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='certificate_expire_date',
            field=models.CharField(blank=True, help_text='证书失效日期', max_length=10, null=True, verbose_name='证书失效日期'),
        ),
    ]
