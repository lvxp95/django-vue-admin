from django.db import models

from dvadmin.utils.models import CoreModel, table_prefix


class OnlineVersion(CoreModel):
    equest_number = models.CharField(max_length=25, verbose_name="需求申请号", help_text="需求申请号", null=True, blank=True)
    demand_number = models.CharField(max_length=50, verbose_name="需求编号", help_text="需求编号", null=True, blank=True)
    SYSTEMS_CHOICES = (
        (0, "请选择"),
        (1, "CRM"),
        (2, "ESOP"),
        (3, "电渠"),
        (4, "账管"),
        (5, "终端"),
        (7, "知识库"),
        (8, "渠道APP"),
        (9, "酬金"),
        (10, "项目"),
        (11, "收入宝"),
    )
    systemes = models.IntegerField(
        choices=SYSTEMS_CHOICES, default=0, verbose_name="系统", help_text="系统"
    )

    requirements = models.CharField(max_length=50, verbose_name="业务需求", help_text="业务需求")
    DEMAND_TYPE = (
        (0, "请选择"),
        (1, "故障"),
        (2, "项目"),
        (3, "优化"),
        (4, "需求"),
    )
    demand_type = models.IntegerField(
        choices=DEMAND_TYPE, default=0, verbose_name="需求类型", help_text="需求类型"
    )

    DEMAND_SOURCE = (
        (0, "请选择"),
        (1, "互联网运营中心"),
        (2, "信息技术中心"),
        (3, "市场经营部"),
    )
    demand_source = models.IntegerField(
        choices=DEMAND_SOURCE, default=0, verbose_name="需求来源", help_text="需求来源"
    )

    online_version = models.CharField(max_length=50, verbose_name="上线版本批次", help_text="上线版本批次")

    class Meta:
        db_table = table_prefix + "online"
        verbose_name = "上线表"
        verbose_name_plural = verbose_name
        ordering = "-online_version",


class OnlineVersionStatistics(models.Model):
    id = models.BigAutoField(primary_key=True, help_text="Id", verbose_name="Id")
    online_version = models.CharField(max_length=50, verbose_name="上线版本批次", help_text="上线版本批次")
    environment = models.CharField(max_length=20, verbose_name="环境", help_text="环境")
    systems = models.CharField(max_length=50, verbose_name="系统", help_text="系统")
    count = models.IntegerField(default=0, verbose_name="数量", help_text="数量")
    undeveloped = models.IntegerField(default=0, verbose_name="未开发完成", help_text="未开发完成")
    unpublished = models.IntegerField(default=0, verbose_name="未发布", help_text="未发布")
    not_configured = models.IntegerField(default=0, verbose_name="未配置", help_text="未配置")
    demand_not_confirmed = models.IntegerField(default=0, verbose_name="需求未确认", help_text="需求未确认")
    block = models.IntegerField(default=0, verbose_name="阻塞", help_text="阻塞")
    joint_commissioning = models.IntegerField(default=0, verbose_name="联调中", help_text="联调中")
    not_tested = models.IntegerField(default=0, verbose_name="未测试", help_text="未测试")
    under_test = models.IntegerField(default=0, verbose_name="测试中", help_text="测试中")
    test_pass = models.IntegerField(default=0, verbose_name="通过", help_text="通过")
    test_fail = models.IntegerField(default=0, verbose_name="未通过", help_text="未通过")
    fixed = models.IntegerField(default=0, verbose_name="已修复", help_text="已修复")
    unable_to_test = models.IntegerField(default=0, verbose_name="通过（无法测试）", help_text="通过（无法测试）")
    not_online_temporarily = models.IntegerField(default=0, verbose_name="暂不上线", help_text="暂不上线")
    already_online = models.IntegerField(default=0, verbose_name="已经上线", help_text="已经上线")

    class Meta:
        db_table = table_prefix + "online_version_statistics"
        verbose_name = "上线需求统计表"
        verbose_name_plural = verbose_name
        ordering = "-online_version",


class BPMOnline(models.Model):
    id = models.BigAutoField(primary_key=True, help_text="Id", verbose_name="Id")
    equest_number = models.CharField(max_length=50, verbose_name="需求申请号", help_text="需求申请号")
    demand_number = models.CharField(max_length=50, verbose_name="需求编码", help_text="需求编码")
    systems = models.CharField(max_length=20, verbose_name="系统", help_text="系统")
    requirements = models.CharField(max_length=255, verbose_name="业务需求", help_text="业务需求")
    requirements = models.CharField(max_length=255, verbose_name="业务需求", help_text="业务需求")
    demand_type = models.CharField(max_length=20, verbose_name="需求类型", help_text="需求类型")
    demand_source = models.CharField(max_length=20, verbose_name="需求来源", help_text="需求来源")
    bureau_manager = models.CharField(max_length=5, verbose_name="局方负责人", help_text="局方负责人")
    demand_complexity = models.CharField(max_length=5, verbose_name="需求复杂度", help_text="需求复杂度")
    demand_manager = models.CharField(max_length=5, verbose_name="需求负责人", help_text="需求负责人")
    demand_manager = models.CharField(max_length=5, verbose_name="需求负责人", help_text="需求负责人")
    development_manager = models.CharField(max_length=5, verbose_name="开发负责人", help_text="开发负责人")
    development_group_leader = models.CharField(max_length=5, verbose_name="开发组长", help_text="开发组长")
    tester = models.CharField(max_length=5, verbose_name="测试负责人", help_text="测试负责人")
    ost_development = models.CharField(max_length=5, verbose_name="162部署情况", help_text="162部署情况")
    ost_test_result = models.CharField(max_length=5, verbose_name="162测试结果", help_text="162测试结果")
    oft_development = models.CharField(max_length=5, verbose_name="143部署情况", help_text="143部署情况")
    oft_test_result = models.CharField(max_length=5, verbose_name="143测试结果", help_text="143测试结果")
    notes = models.CharField(max_length=255, verbose_name="备注", help_text="备注")
    version_number = models.CharField(max_length=10, verbose_name="上线版本批次", help_text="上线版本批次")

    class Meta:
        db_table = table_prefix + "bpm_online"
        verbose_name = "上线清单表"
        verbose_name_plural = verbose_name
        ordering = "-id",
