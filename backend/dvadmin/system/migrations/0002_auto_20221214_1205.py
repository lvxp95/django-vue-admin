# Generated by Django 3.2.3 on 2022-12-14 12:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('system', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='grade',
            field=models.CharField(help_text='等级', max_length=5, verbose_name='等级'),
        ),
        migrations.AlterField(
            model_name='employee',
            name='graduation_date',
            field=models.CharField(help_text='毕业时间', max_length=10, verbose_name='毕业时间'),
        ),
    ]
