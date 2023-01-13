// import util from '@/libs/util'

export const crudOptions = (vm) => {
  // util.filterParams(vm, ['dept_name', 'role_info{name}', 'dept_name_all'])
  return {
    pageOptions: {
      compact: true
    },
    options: {
      height: '100%',
      highlightCurrentRow: true,
      tableType: 'vxe-table',
      rowKey: true,
      rowId: 'id'
    },
    selectionRow: {
      align: 'center',
      width: 46
    },
    rowHandle: {
      width: 240,
      fixed: 'right',
      view: {
        thin: true,
        text: '',
        disabled () {
          return !vm.hasPermissions('Retrieve')
        }
      },
      edit: {
        thin: true,
        text: '',
        disabled () {
          return !vm.hasPermissions('Update')
        }
      },
      remove: {
        thin: true,
        text: '',
        disabled () {
          return !vm.hasPermissions('Delete')
        }
      }
    },
    viewOptions: {
      componentType: 'form'
    },
    formOptions: {
      defaultSpan: 12 // 默认的表单 span
    },
    indexRow: { // 或者直接传true,不显示title，不居中
      title: '序号',
      align: 'center',
      width: 60
    },
    columns: [
      {
        title: 'ID',
        key: 'id',
        disabled: true,
        form: {
          disabled: true
        }
      },
      {
        title: '姓名',
        key: 'name',
        minWidth: 60,
        search: {
          disabled: false
        },
        type: 'input',
        form: {
          rules: [ // 表单校验规则
            {
              required: true,
              message: '姓名必填项'
            }
          ],
          component: {
            span: 12,
            placeholder: '请输入姓名'
          },
          itemProps: {
            class: { yxtInput: true }
          }
        }
      },
      {
        title: '员工编号',
        key: 'employee_number',
        minWidth: 90,
        search: {
          disabled: false
        },
        type: 'input',
        form: {
          component: {
            span: 12,
            placeholder: '请输入员工编号'
          },
          itemProps: {
            class: { yxtInput: true }
          }
        }
      },
      {
        title: '性别',
        key: 'gender',
        show: false,
        minWidth: 50,
        type: 'input',
        form: {
          component: {
            span: 12,
            placeholder: '请输入性别'
          },
          itemProps: {
            class: { yxtInput: true }
          }
        }
      },
      {
        title: '身份证号',
        key: 'card_number',
        minWidth: 100,
        type: 'input',
        form: {
          component: {
            span: 12,
            placeholder: '请输入身份证号'
          },
          itemProps: {
            class: { yxtInput: true }
          }
        }
      },
      {
        title: '到期时间',
        key: 'card_expire',
        show: false,
        minWidth: 100,
        type: 'input',
        form: {
          component: {
            span: 12,
            placeholder: '请输入身份证号到期时间'
          },
          itemProps: {
            class: { yxtInput: true }
          }
        }
      },
      {
        title: '学历',
        key: 'degree',
        minWidth: 50,
        search: {
          disabled: false
        },
        type: 'input',
        form: {
          rules: [ // 表单校验规则
            {
              required: true,
              message: '学历必填项'
            }
          ],
          component: {
            span: 12,
            placeholder: '请输入学历'
          },
          itemProps: {
            class: { yxtInput: true }
          }
        }
      },
      {
        title: '电话',
        key: 'phone',
        show: false,
        minWidth: 90,
        type: 'input',
        form: {
          component: {
            span: 12,
            placeholder: '请输入电话'
          },
          itemProps: {
            class: { yxtInput: true }
          }
        }
      },
      {
        title: '正编',
        key: 'formal_preparation',
        show: false,
        minWidth: 50,
        search: {
          disabled: false
        },
        type: 'input',
        form: {
          component: {
            span: 12,
            placeholder: '请输入是否正编'
          },
          itemProps: {
            class: { yxtInput: true }
          }
        }
      },
      {
        title: '专业',
        key: 'specialized',
        minWidth: 140,
        type: 'input',
        form: {
          rules: [ // 表单校验规则
            {
              required: true,
              message: '专业必填项'
            }
          ],
          component: {
            span: 12,
            placeholder: '请输入专业'
          },
          itemProps: {
            class: { yxtInput: true }
          }
        }
      },
      {
        title: '毕业时间',
        key: 'graduation_date',
        show: false,
        minWidth: 100,
        type: 'input',
        form: {
          rules: [ // 表单校验规则
            {
              required: true,
              message: '毕业时间必填项'
            }
          ],
          component: {
            span: 12,
            placeholder: '请输入毕业时间'
          },
          itemProps: {
            class: { yxtInput: true }
          }
        }
      },
      {
        title: '合同到期时间',
        key: 'contract_expire',
        minWidth: 110,
        type: 'input',
        form: {
          component: {
            span: 12,
            placeholder: '请输入合同到期时间'
          },
          itemProps: {
            class: { yxtInput: true }
          }
        }
      },
      {
        title: '社保缴纳地',
        key: 'social_security',
        show: false,
        minWidth: 110,
        type: 'input',
        form: {
          component: {
            span: 12,
            placeholder: '请输入社保缴纳地'
          },
          itemProps: {
            class: { yxtInput: true }
          }
        }
      },
      {
        title: '证书名称',
        key: 'certificate_name',
        minWidth: 150,
        type: 'input',
        form: {
          component: {
            span: 12,
            placeholder: '请输入证书名称(到期时间)'
          },
          itemProps: {
            class: { yxtInput: true }
          }
        }
      },
      {
        title: '证书生效日期',
        key: 'certificate_valid_date',
        show: false,
        minWidth: 60,
        type: 'input',
        form: {
          component: {
            span: 12,
            placeholder: '请输入证书生效日期'
          },
          itemProps: {
            class: { yxtInput: true }
          }
        }
      },
      {
        title: '证书失效日期',
        key: 'certificate_expire_date',
        show: false,
        minWidth: 60,
        type: 'input',
        form: {
          component: {
            span: 12,
            placeholder: '请输入证书失效日期'
          },
          itemProps: {
            class: { yxtInput: true }
          }
        }
      },
      {
        title: '验真网址',
        key: 'verify_url',
        show: false,
        minWidth: 60,
        type: 'input',
        form: {
          component: {
            span: 12,
            placeholder: '请输入验真网址'
          },
          itemProps: {
            class: { yxtInput: true }
          }
        }
      },
      {
        title: '认证机构',
        key: 'certification_body',
        show: false,
        minWidth: 60,
        search: {
          disabled: false
        },
        type: 'input',
        form: {
          rules: [ // 表单校验规则
            {
              required: true,
              message: '认证机构必填项'
            }
          ],
          component: {
            span: 12,
            placeholder: '请输入认证机构'
          },
          itemProps: {
            class: { yxtInput: true }
          }
        }
      },
      {
        title: '等级',
        key: 'grade',
        minWidth: 60,
        search: {
          disabled: false
        },
        type: 'input',
        form: {
          rules: [ // 表单校验规则
            {
              required: true,
              message: '等级必填项'
            }
          ],
          component: {
            span: 12,
            placeholder: '请输入等级'
          },
          itemProps: {
            class: { yxtInput: true }
          }
        }
      }
    ]
  }
}
