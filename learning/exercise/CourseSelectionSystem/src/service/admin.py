#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
------------------------------------------------------------------------------------------------------------------------

@Author: Bamboo
@Email: bamboo8493@126.com
@Datetime: 2019/12/4 15:56
@Description: 

------------------------------------------------------------------------------------------------------------------------

@Modifier: 
@Email: 
@Datetime: 2019/12/4 15:56
@Description: 

------------------------------------------------------------------------------------------------------------------------
"""

from lib import commons
from src import models


def create_school(tip):
    """
    创建学校
    :param tip: 提示信息
    :return: obj
    """
    print('======%s======' % tip)
    name = input('请输入学校名字：')

    obj = models.School(name)
    obj.save()

    return obj


def show_school(tip):
    """
    查看学校
    :param tip: 提示信息
    :return: True
    """
    return commons.show_model(models.School.db_path, tip)


def create_teacher(tip):
    """
    创建老师
    :param tip: 提示信息
    :return: obj
    """
    print('======%s======' % tip)

    mobile = ''
    password = ''
    name = ''
    level = ''

    while mobile == '':
        mobile = input('请输入老师手机号码：')

    while password == '':
        password = input('请输入老师手机密码：')

    while name == '':
        name = input('请输入老师名字：')

    while level == '':
        level = input('请输入老师级别：')

    obj = models.Teacher(mobile, password, name, level)
    obj.save()

    return obj


def show_teacher(tip):
    """
    查看老师
    :param tip: 提示信息
    :return: True
    """
    return commons.show_model(models.Teacher.db_path, tip)


def create_course(tip):
    """
    创建课程
    :param tip: 提示信息
    :return: school_obj
    """
    print('======%s======' % tip)
    school_obj = commons.choice_model(models.School.db_path, '学校')

    name = input('请输入课程名称：')
    price = input('请输入课程价格：')
    period = input('请输入课程周期：')

    obj = models.Course(name, price, period, school_obj.nid)
    obj.save()

    return obj


def show_course(tip):
    """
    显示课程
    :param tip: 提示信息
    :return: True
    """
    # return
    return commons.show_model(models.Course.db_path, tip)


def create_course_teacher(tip):
    """
    创建课程对应老师
    :param tip: 提示信息
    :return: obj
    """
    print('======%s======' % tip)

    course_obj = commons.choice_model(models.Course.db_path, '课程')
    teacher_obj = commons.choice_model(models.Teacher.db_path, '老师')

    obj = models.CourseToTeacher(course_obj.nid, teacher_obj.nid)
    obj.save()

    return obj


def show_course_teacher(tip):
    """
    查看课程对应老师
    :param tip: 提示信息
    :return: True
    """
    return commons.show_model(models.CourseToTeacher.db_path, tip)


def create_classes(tip):
    """
    创建班级
    :param tip: 提示信息
    :return: obj
    """
    print('======%s======' % tip)

    school_obj = commons.choice_model(models.School.db_path, '学校')
    course_to_teacher_list = commons.choice_model(models.CourseToTeacher.db_path, '班级对应老师', True)

    name = input('请输入班级名字：')
    tuition = input('请输入学费：')

    obj = models.Classes(name, tuition, school_obj.nid, course_to_teacher_list)
    obj.save()

    return obj


def show_classes(tip):
    """
    查看班级
    :param tip: 提示信息
    :return: True
    """
    return commons.show_model(models.Classes.db_path, tip)


def main():
    print('======管理员登录======')
    admin = models.Admin.login()

    choices = [
        {
            'name': '创建学校',
            'method': create_school
        },
        {
            'name': '查看学校',
            'method': show_school
        },
        {
            'name': '创建老师',
            'method': create_teacher
        },
        {
            'name': '查看老师',
            'method': show_teacher
        },
        {
            'name': '创建课程',
            'method': create_course
        },
        {
            'name': '查看课程',
            'method': show_course
        },
        {
            'name': '创建课程对应的老师',
            'method': create_course_teacher
        },
        {
            'name': '查看课程对应的老师',
            'method': show_course_teacher
        },
        {
            'name': '创建班级',
            'method': create_classes
        },
        {
            'name': '查看班级',
            'method': show_classes
        }
    ]

    commons.to_choices(choices, True)
