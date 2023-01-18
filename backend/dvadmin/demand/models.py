from django.db import models


class Online(models.Model):
    id = models.BigAutoField(primary_key=True, help_text="Id", verbose_name="Id")
    equest_number = models.CharField(max_length=50, verbose_name="���������", help_text="���������", null=True,
                                     blank=True)
    demand_number = models.CharField(max_length=50, verbose_name="�������", help_text="�������", null=True,
                                     blank=True)
    systems = models.CharField(max_length=20, verbose_name="ϵͳ", help_text="ϵͳ", null=True, blank=True)
    requirements = models.CharField(max_length=255, verbose_name="ҵ������", help_text="ҵ������", null=True,
                                    blank=True)
    demand_type = models.CharField(max_length=20, verbose_name="��������", help_text="��������", null=True, blank=True)
    demand_source = models.CharField(max_length=20, verbose_name="������Դ", help_text="������Դ", null=True,
                                     blank=True)
    bureau_manager = models.CharField(max_length=10, verbose_name="�ַ�������", help_text="�ַ�������", null=True,
                                      blank=True)
    demand_complexity = models.CharField(max_length=5, verbose_name="�����Ӷ�", help_text="�����Ӷ�", null=True,
                                         blank=True)
    demand_manager = models.CharField(max_length=5, verbose_name="��������", help_text="��������", null=True,
                                      blank=True)
    development_manager = models.CharField(max_length=50, verbose_name="����������", help_text="����������", null=True,
                                           blank=True)
    development_group_leader = models.CharField(max_length=5, verbose_name="�����鳤", help_text="�����鳤", null=True,
                                                blank=True)
    tester = models.CharField(max_length=50, verbose_name="���Ը�����", help_text="���Ը�����", null=True, blank=True)
    ost_development = models.CharField(max_length=5, verbose_name="162�������", help_text="162�������", null=True,
                                       blank=True)
    ost_test_result = models.CharField(max_length=10, verbose_name="162���Խ��", help_text="162���Խ��", null=True,
                                       blank=True)
    oft_development = models.CharField(max_length=5, verbose_name="143�������", help_text="143�������", null=True,
                                       blank=True)
    oft_test_result = models.CharField(max_length=10, verbose_name="143���Խ��", help_text="143���Խ��", null=True,
                                       blank=True)
    notes = models.CharField(max_length=255, verbose_name="��ע", help_text="��ע", null=True, blank=True)
    version_number = models.CharField(max_length=30, verbose_name="���߰汾����", help_text="���߰汾����")

    class Meta:
        db_table = table_prefix + "online"
        verbose_name = "���߱�"
        verbose_name_plural = verbose_name
        ordering = "-id",