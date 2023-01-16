from django.db import models

from dvadmin.utils.models import CoreModel, table_prefix


class Online(models.Model):
    id = models.BigAutoField(primary_key=True, help_text="Id", verbose_name="Id")
    equest_number = models.CharField(max_length=50, verbose_name="需求申请号", help_text="需求申请号", null=True,
                                     blank=True)
    demand_number = models.CharField(max_length=50, verbose_name="需求编码", help_text="需求编码", null=True,
                                     blank=True)
    systems = models.CharField(max_length=20, verbose_name="系统", help_text="系统", null=True, blank=True)
    requirements = models.CharField(max_length=255, verbose_name="业务需求", help_text="业务需求", null=True,
                                    blank=True)
    demand_type = models.CharField(max_length=20, verbose_name="需求类型", help_text="需求类型", null=True, blank=True)
    demand_source = models.CharField(max_length=20, verbose_name="需求来源", help_text="需求来源", null=True,
                                     blank=True)
    bureau_manager = models.CharField(max_length=10, verbose_name="局方负责人", help_text="局方负责人", null=True,
                                      blank=True)
    demand_complexity = models.CharField(max_length=5, verbose_name="需求复杂度", help_text="需求复杂度", null=True,
                                         blank=True)
    demand_manager = models.CharField(max_length=5, verbose_name="需求负责人", help_text="需求负责人", null=True,
                                      blank=True)
    development_manager = models.CharField(max_length=20, verbose_name="开发负责人", help_text="开发负责人", null=True,
                                           blank=True)
    development_group_leader = models.CharField(max_length=5, verbose_name="开发组长", help_text="开发组长", null=True,
                                                blank=True)
    tester = models.CharField(max_length=5, verbose_name="测试负责人", help_text="测试负责人", null=True, blank=True)
    ost_development = models.CharField(max_length=5, verbose_name="162部署情况", help_text="162部署情况", null=True,
                                       blank=True)
    ost_test_result = models.CharField(max_length=10, verbose_name="162测试结果", help_text="162测试结果", null=True,
                                       blank=True)
    oft_development = models.CharField(max_length=5, verbose_name="143部署情况", help_text="143部署情况", null=True,
                                       blank=True)
    oft_test_result = models.CharField(max_length=10, verbose_name="143测试结果", help_text="143测试结果", null=True,
                                       blank=True)
    notes = models.CharField(max_length=255, verbose_name="备注", help_text="备注", null=True, blank=True)
    version_number = models.CharField(max_length=10, verbose_name="上线版本批次", help_text="上线版本批次")

    class Meta:
        db_table = table_prefix + "online"
        verbose_name = "上线表"
        verbose_name_plural = verbose_name
        ordering = "-id",
