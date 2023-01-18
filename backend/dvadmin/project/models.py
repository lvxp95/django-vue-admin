from django.db import models

from dvadmin.utils.models import CoreModel, table_prefix


class OnlineCurrentTime(CoreModel):
    requirements = models.CharField(
        max_length=255, verbose_name="业务需求名称", help_text="业务需求名称", null=True, blank=True
    )
    equest_number = models.CharField(
        max_length=50, verbose_name="需求申请号", help_text="需求申请号", null=True, blank=True
    )
    demand_number = models.CharField(
        max_length=50, verbose_name="需求编码", help_text="需求编码", null=True, blank=True
    )
    SYSTEMS_CHOICES = (
        (0, "请选择"),
        (1, "CRM"),
        (2, "ESOP"),
        (3, "电渠"),
        (4, "账管"),
        (5, "终端"),
        (6, "知识库"),
        (7, "渠道APP"),
        (8, "酬金"),
        (9, "项目"),
        (10, "收入宝"),
    )
    systems = models.IntegerField(
        choices=SYSTEMS_CHOICES, default=0, verbose_name="系统", help_text="系统", null=True, blank=True
    )
    DEMAND_TYPE_CHOICES = (
        (0, "请选择"),
        (1, "故障"),
        (2, "项目"),
        (3, "优化"),
        (4, "需求"),
    )
    demand_type = models.IntegerField(
        choices=DEMAND_TYPE_CHOICES, default=0, verbose_name="需求类型", help_text="需求类型", null=True, blank=True
    )
    DEMAND_SOURCE_CHOICES = (
        (0, "请选择"),
        (1, "信息技术中心"),
        (2, "互联网需求中心"),
        (3, "市场经营部"),
    )
    demand_source = models.IntegerField(
        choices=DEMAND_SOURCE_CHOICES, default=0, verbose_name="需求来源", help_text="需求来源", null=True, blank=True
    )
    demand_complexity = models.CharField(
        max_length=5, verbose_name="需求复杂度", help_text="需求复杂度", null=True, blank=True
    )
    version_number = models.CharField(max_length=30, verbose_name="上线版本批次", help_text="上线版本批次")
    development_manager = models.CharField(
        max_length=50, verbose_name="开发负责人", help_text="开发负责人", null=True, blank=True
    )
    bureau_manager = models.CharField(
        max_length=10, verbose_name="局方负责人", help_text="局方负责人", null=True, blank=True
    )
    demand_manager = models.CharField(
        max_length=5, verbose_name="需求负责人", help_text="需求负责人", null=True, blank=True
    )
    development_group_leader = models.CharField(
        max_length=5, verbose_name="开发组长", help_text="开发组长", null=True, blank=True
    )
    tester = models.CharField(max_length=50, verbose_name="测试负责人", help_text="测试负责人", null=True, blank=True)
    DEVELOPMENT_CHOICES = (
        (0, "请选择"),
        (1, "已发布"),
        (2, "无需发布"),
        (3, "未发布"),
    )
    TEST_RESULT_CHOICES = (
        (0, "请选择"),
        (1, "未开发完成"),
        (2, "未发布"),
        (3, "未配置"),
        (4, "需求未确认"),
        (5, "阻塞"),
        (6, "联调中"),
        (7, "已经上线"),
        (8, "测试中"),
        (9, "通过"),
        (10, "未通过"),
        (11, "已修复"),
        (12, "通过（无法测试）"),
        (13, "暂不上线"),
        (14, "未测试"),
    )
    development_162 = models.IntegerField(
        choices=DEVELOPMENT_CHOICES, default=0, verbose_name="162部署情况", help_text="162部署情况", null=True, blank=True
    )
    test_result_162 = models.IntegerField(
        choices=TEST_RESULT_CHOICES, default=0, verbose_name="162测试结果", help_text="162测试结果", null=True, blank=True
    )
    development_143 = models.IntegerField(
        choices=DEVELOPMENT_CHOICES, default=0, verbose_name="143部署情况", help_text="143部署情况", null=True, blank=True
    )
    test_result_143 = models.IntegerField(
        choices=TEST_RESULT_CHOICES, default=0, verbose_name="143测试结果", help_text="143测试结果", null=True, blank=True
    )
    notes = models.TextField(verbose_name="备注", help_text="备注", null=True, blank=True)

    class Meta:
        db_table = table_prefix + "online_current_time_online"
        verbose_name = "需求表"
        verbose_name_plural = verbose_name
        ordering = "-id",

#
#
# class Online(models.Model):
#     id = models.BigAutoField(primary_key=True, help_text="Id", verbose_name="Id")
#     requirements = models.CharField(max_length=255, verbose_name="业务需求", help_text="业务需求", null=True,
#                                     blank=True)
#     demand_number = models.CharField(max_length=50, verbose_name="需求编码", help_text="需求编码", null=True,
#                                      blank=True)
#     equest_number = models.CharField(max_length=50, verbose_name="需求申请号", help_text="需求申请号", null=True,
#                                      blank=True)
#     split_demand = models.CharField(max_length=50, verbose_name="拆分需求编码", help_text="拆分需求编码", null=True,
#                                     blank=True)
#     systems = models.CharField(max_length=20, verbose_name="系统", help_text="系统", null=True, blank=True)
#     demand_type = models.CharField(max_length=20, verbose_name="需求类型", help_text="需求类型", null=True, blank=True)
#     demand_source = models.CharField(max_length=20, verbose_name="需求来源", help_text="需求来源", null=True,
#                                      blank=True)
#     bureau_manager = models.CharField(max_length=10, verbose_name="局方负责人", help_text="局方负责人", null=True,
#                                       blank=True)
#     demand_complexity = models.CharField(max_length=5, verbose_name="需求复杂度", help_text="需求复杂度", null=True,
#                                          blank=True)
#     demand_manager = models.CharField(max_length=5, verbose_name="需求负责人", help_text="需求负责人", null=True,
#                                       blank=True)
#     development_manager = models.CharField(max_length=50, verbose_name="开发负责人", help_text="开发负责人", null=True,
#                                            blank=True)
#     development_group_leader = models.CharField(max_length=5, verbose_name="开发组长", help_text="开发组长", null=True,
#                                                 blank=True)
#     tester = models.CharField(max_length=50, verbose_name="测试负责人", help_text="测试负责人", null=True, blank=True)
#     ost_development = models.CharField(max_length=5, verbose_name="162部署情况", help_text="162部署情况", null=True,
#                                        blank=True)
#     ost_test_result = models.CharField(max_length=10, verbose_name="162测试结果", help_text="162测试结果", null=True,
#                                        blank=True)
#     oft_development = models.CharField(max_length=5, verbose_name="143部署情况", help_text="143部署情况", null=True,
#                                        blank=True)
#     oft_test_result = models.CharField(max_length=10, verbose_name="143测试结果", help_text="143测试结果", null=True,
#                                        blank=True)
#     notes = models.CharField(max_length=255, verbose_name="备注", help_text="备注", null=True, blank=True)
#     version_number = models.CharField(max_length=30, verbose_name="上线版本批次", help_text="上线版本批次")
#
#     class Meta:
#         db_table = table_prefix + "online"
#         verbose_name = "上线表"
#         verbose_name_plural = verbose_name
#         ordering = "-id",
