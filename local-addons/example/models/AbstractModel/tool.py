# -*- coding: utf-8 -*-

from odoo import models, fields, api
from locallib import qymp
import logging

_logger = logging.getLogger(__name__)


class Tool(models.AbstractModel):
    _name = 'example.tool'
    _description = '自定义工具'

    def _init_sync_tool(self):
        _logger.info("--------同步企业组织初始化 --------")
        corpid = self.env['ir.config_parameter'].sudo().get_param('corpid')
        corpsecret = self.env['ir.config_parameter'].sudo().get_param('corpsecret')
        if corpid and corpsecret:
            qymp.corpid = corpid
            qymp.corpsecret = corpsecret
            _logger.info("--------同步企业组织初始化成功 --------")
            return True
        else:
            _logger.info("--------同步企业组织初始化失败 --------")
            return False

    def _sync_new_dep(self, department_list):
        _logger.info("--------创建新部门开始--------")
        for department in department_list:
            qywx_id = str(department['id'])
            old_dep = self.env['hr.diy.department'].sudo().search([('qywx_id', '=', qywx_id)])
            if not old_dep:
                vals = {
                    'name': department.get('name'),
                    'qywx_id': qywx_id,
                }
                if qywx_id == 1:
                    vals['active'] = False
                new_dep = self.env['hr.diy.department'].sudo().create(vals)
        _logger.info("--------创建新部门成功--------")
        return True

    def _sync_new_emp(self, department_list):
        _logger.info("--------创建新员工开始--------")
        for department in department_list:
            userid_set = set()
            dep_id = department['id']
            dep_user_info_list = qymp.get_department_user_info_list(dep_id)
            for user_info in dep_user_info_list:
                userid = user_info['userid']
                if userid not in userid_set:
                    userid_set.add(userid)
                    old_user = self.env['hr.diy.employee'].sudo().search([('qywx_code', '=', userid)], limit=1)
                    if not old_user:
                        new_emp = self.env['hr.diy.employee'].sudo().create({
                            'name': user_info['name'],
                            'qywx_code': user_info['userid'],
                        })
        _logger.info("--------创建新员工成功--------")
        return True

    def _sync_dep_info(self, department_list):
        _logger.info("--------同步部门详情开始--------")
        for department in department_list:
            qywx_id = str(department['id'])
            vals = {
                'is_sync': True
            }
            dep = self.env['hr.diy.department'].sudo().search([('qywx_id', '=', qywx_id)], limit=1)
            parentid = department.get('parentid')
            if parentid:
                parent_dep = self.env['hr.diy.department'].sudo().search([('qywx_id', '=', parentid)], limit=1)
                vals['parent_id'] = parent_dep.id
            department_leader_list = department.get('department_leader')
            if department_leader_list:
                leader_userid = department_leader_list[0]
                leader = self.env['hr.diy.employee'].sudo().search([('qywx_code', '=', leader_userid)], limit=1)
                vals['manager_id'] = leader.id
            dep.sudo().write(vals)
        _logger.info("--------同步部门详情成功--------")
        return True

    def _sync_emp_info(self, department_list):
        _logger.info("--------同步员工详情开始--------")
        all_user_info_list = []
        for department in department_list:
            dep_id = department['id']
            dep_user_info_list = qymp.get_department_user_info_list(dep_id)
            all_user_info_list.extend(dep_user_info_list)
        for user_info in all_user_info_list:
            old_user = self.env['hr.diy.employee'].sudo().search([('qywx_code', '=', user_info['userid'])], limit=1)
            vals = {
                'position': user_info.get('position'),
                'status': str(user_info.get('status')),
                'telephone': user_info.get('telephone'),
                # 'department_id': dep.id,
                'is_sync': True
            }
            dep_id = str(user_info.get('main_department'))
            if dep_id:
                dep = self.env['hr.diy.department'].sudo().search([('qywx_id', '=', dep_id)], limit=1)
                vals['dep_id'] = dep.id
            old_user.sudo().write(vals)
        _logger.info("--------同步员工详情成功--------")
        return True

    def syns_qywx_department_employee(self):
        assert self._init_sync_tool()
        department_list = qymp.get_department_list()
        assert self._sync_new_dep(department_list), "--------创建新部门失败--------"
        assert self._sync_new_emp(department_list), "--------创建新员工失败--------"
        assert self._sync_dep_info(department_list), "--------同步部门详情失败--------"
        assert self._sync_emp_info(department_list), "--------同步员工详情失败--------"
