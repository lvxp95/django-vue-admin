# Generated by Django 3.2.3 on 2023-01-17 23:01

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='OnlineCurrentTime',
            fields=[
                ('id', models.BigAutoField(help_text='Id', primary_key=True, serialize=False, verbose_name='Id')),
                ('description', models.CharField(blank=True, help_text='描述', max_length=255, null=True, verbose_name='描述')),
                ('modifier', models.CharField(blank=True, help_text='修改人', max_length=255, null=True, verbose_name='修改人')),
                ('dept_belong_id', models.CharField(blank=True, help_text='数据归属部门', max_length=255, null=True, verbose_name='数据归属部门')),
                ('update_datetime', models.DateTimeField(auto_now=True, help_text='修改时间', null=True, verbose_name='修改时间')),
                ('create_datetime', models.DateTimeField(auto_now_add=True, help_text='创建时间', null=True, verbose_name='创建时间')),
                ('requirements', models.CharField(blank=True, help_text='业务需求名称', max_length=255, null=True, verbose_name='业务需求名称')),
                ('equest_number', models.CharField(blank=True, help_text='需求申请号', max_length=50, null=True, verbose_name='需求申请号')),
                ('demand_number', models.CharField(blank=True, help_text='需求编码', max_length=50, null=True, verbose_name='需求编码')),
                ('systems', models.IntegerField(blank=True, choices=[(0, '请选择'), (1, 'CRM'), (2, 'ESOP'), (3, '电渠'), (4, '账管'), (5, '终端'), (6, '知识库'), (7, '渠道APP'), (8, '酬金'), (9, '项目'), (10, '收入宝')], default=0, help_text='系统', null=True, verbose_name='系统')),
                ('demand_type', models.IntegerField(blank=True, choices=[(0, '请选择'), (1, '故障'), (2, '项目'), (3, '优化'), (4, '需求')], default=0, help_text='需求类型', null=True, verbose_name='需求类型')),
                ('demand_source', models.IntegerField(blank=True, choices=[(0, '请选择'), (1, '信息技术中心'), (2, '互联网需求中心'), (3, '市场经营部')], default=0, help_text='需求来源', null=True, verbose_name='需求来源')),
                ('demand_complexity', models.CharField(blank=True, help_text='需求复杂度', max_length=5, null=True, verbose_name='需求复杂度')),
                ('version_number', models.CharField(help_text='上线版本批次', max_length=30, verbose_name='上线版本批次')),
                ('development_manager', models.CharField(blank=True, help_text='开发负责人', max_length=50, null=True, verbose_name='开发负责人')),
                ('bureau_manager', models.CharField(blank=True, help_text='局方负责人', max_length=10, null=True, verbose_name='局方负责人')),
                ('demand_manager', models.CharField(blank=True, help_text='需求负责人', max_length=5, null=True, verbose_name='需求负责人')),
                ('development_group_leader', models.CharField(blank=True, help_text='开发组长', max_length=5, null=True, verbose_name='开发组长')),
                ('tester', models.CharField(blank=True, help_text='测试负责人', max_length=50, null=True, verbose_name='测试负责人')),
                ('development_162', models.IntegerField(blank=True, choices=[(0, '请选择'), (1, '已发布'), (2, '无需发布'), (3, '未发布')], default=0, help_text='162部署情况', null=True, verbose_name='162部署情况')),
                ('test_result_162', models.IntegerField(blank=True, choices=[(0, '请选择'), (1, '未开发完成'), (2, '未发布'), (3, '未配置'), (4, '需求未确认'), (5, '阻塞'), (6, '联调中'), (7, '已经上线'), (8, '测试中'), (9, '通过'), (10, '未通过'), (11, '已修复'), (12, '通过（无法测试）'), (13, '暂不上线'), (14, '未测试')], default=0, help_text='162测试结果', null=True, verbose_name='162测试结果')),
                ('development_143', models.IntegerField(blank=True, choices=[(0, '请选择'), (1, '已发布'), (2, '无需发布'), (3, '未发布')], default=0, help_text='143部署情况', null=True, verbose_name='143部署情况')),
                ('test_result_143', models.IntegerField(blank=True, choices=[(0, '请选择'), (1, '未开发完成'), (2, '未发布'), (3, '未配置'), (4, '需求未确认'), (5, '阻塞'), (6, '联调中'), (7, '已经上线'), (8, '测试中'), (9, '通过'), (10, '未通过'), (11, '已修复'), (12, '通过（无法测试）'), (13, '暂不上线'), (14, '未测试')], default=0, help_text='143测试结果', null=True, verbose_name='143测试结果')),
                ('notes', models.TextField(blank=True, help_text='备注', null=True, verbose_name='备注')),
                ('creator', models.ForeignKey(db_constraint=False, help_text='创建人', null=True, on_delete=django.db.models.deletion.SET_NULL, related_query_name='creator_query', to=settings.AUTH_USER_MODEL, verbose_name='创建人')),
            ],
            options={
                'verbose_name': '需求表',
                'verbose_name_plural': '需求表',
                'db_table': 'dvadmin_online_current_time_online',
                'ordering': ('-id',),
            },
        ),
    ]
