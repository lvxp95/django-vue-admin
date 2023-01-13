#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
@Project ：backend
@File    ：employee.py
@Author  ：吕星澎
@Date    ：2022/12/12 16:31
"""
import datetime
import os
import zipfile
from urllib.parse import quote
from django.http import HttpResponse
from docxtpl import DocxTemplate
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from dvadmin.system.models import Employee
from dvadmin.utils.serializers import CustomModelSerializer
from dvadmin.utils.viewset import CustomModelViewSet
from dvadmin.utils.json_response import DetailResponse


class EmployeeSerializer(CustomModelSerializer):
    """
    员工序列化器
    """

    class Meta:
        model = Employee
        fields = "__all__"
        read_only_fields = ["id"]
        # fields = ["online_version"]


class EmployeeCreateUpdateSerializer(CustomModelSerializer):
    """
    员工创建/更新时的列化器
    """

    class Meta:
        model = Employee
        fields = '__all__'


class ExportEmployeeProfileSerializer(CustomModelSerializer):
    """
    员工导出 序列化器
    """

    def get_is_active(self, instance):
        return "启用" if instance.is_active else "停用"

    class Meta:
        model = Employee
        fields = ("name", "gender", "employee_number", "card_number", "card_expire", "degree", "phone",
                  "formal_preparation", "specialized", "graduation_date", "social_security", "contract_expire",
                  "certificate_name", "certificate_valid_date", "certificate_expire_date", "verify_url", "grade",
                  "certification_body")


class EmployeeProfileImportSerializer(CustomModelSerializer):
    def save(self, **kwargs):
        data = super().save(**kwargs)
        data.save()
        return data

    class Meta:
        model = Employee
        fields = '__all__'


class EmployeeViewSet(CustomModelViewSet):
    """
    list:查询
    create:新增
    update:修改
    retrieve:单例
    destroy:删除
    """
    queryset = Employee.objects.all()  # 指明该视图集在查询数据时使用的查询集
    serializer_class = EmployeeSerializer  # 指明该视图在进行序列化或者反序列化时使用的序列化器
    create_serializer_class = EmployeeCreateUpdateSerializer
    update_serializer_class = EmployeeCreateUpdateSerializer
    # 导出
    field_label = {
        "name": "姓名",
        "employee_number": "员工编号",
        "gender": "性别",
        "card_number": "身份证号",
        "card_expire": "身份证到期",
        "degree": "学历",
        "phone": "电话",
        "formal_preparation": "是否正编",
        "specialized": "专业",
        "graduation_date": "毕业时间",
        "contract_expire": "合同到期",
        "social_security": "社保缴纳地",
        "certificate_name": "证书名称",
        "certificate_valid_date": "证书生效日期",
        "certificate_expire_date": "证书失效日期",
        "verify_url": "验真网址",
        "grade": "等级",
        "certification_body": "认证机构"
    }
    export_field_label = field_label
    export_serializer_class = ExportEmployeeProfileSerializer

    import_serializer_class = EmployeeProfileImportSerializer
    import_field_dict = field_label

    # filter_fields = ["name", "employee_number", "degree", "specialized", "formal_preparation", "have_certificate"]

    @action(methods=["POST"], detail=False, permission_classes=[IsAuthenticated])
    def export_employee_info(self, request):
        """导出员工信息到Word文档"""
        file_path = str(datetime.datetime.now().strftime('%Y-%m-%d')+'.zip')
        zipf = zipfile.ZipFile(file_path, 'w', zipfile.ZIP_DEFLATED)

        response = HttpResponse(content_type="application/msexcel")
        response["Access-Control-Expose-Headers"] = f"Content-Disposition"
        response["content-disposition"] = f'attachment;filename={quote(file_path)}'

        # 遍历人员信息
        for index, info in enumerate(request.data):
            doc = DocxTemplate(r"static\file_template\employee_info_template.docx")  # 模板文档
            context = {}
            for key, value in self.field_label.items():
                context[value] = '' if info[key] is None else info[key]
            doc.render(context)  # 将数据渲染到模板中
            doc.save(response)
            zipf.writestr(info['name']+'.docx', response.content)   # 将docx文档放入压缩包中
            response.content = {}

        zipf.close()
        f = open(file_path, "rb")
        response.content = f.read()
        f.close()
        os.remove(file_path)
        return response
