#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
------------------------------------------------------------------------------------------------------------------------

@Author: Bamboo
@Email: bamboo8493@126.com
@Datetime: 2019/12/4 15:54
@Description: 

------------------------------------------------------------------------------------------------------------------------

@Modifier: 
@Email: 
@Datetime: 2019/12/4 15:54
@Description: 

------------------------------------------------------------------------------------------------------------------------
"""

from lib import commons
from src import models


def login(tip):
    """
    登录
    :param tip: 提示信息
    :return: student_obj
    """
    print('======学生%s======' % tip)
    return models.Student.login()


def register(tip):
    """
    注册
    :param tip: 提示信息
    :return: student_obj
    """
    print('======学生%s======' % tip)
    return models.Student.register()

def choice_course(tip, student):
    """
    选择课程
    :param tip: 提示信息
    :return: True
    """
    print('======学生%s======' % tip)

    course_list = commons.get_all_list(models.Course.db_path)
    course_to_teacher_list = commons.get_all_list(models.CourseToTeacher.db_path)

    # 获取所有课程
    for index, course in enumerate(course_list, 1):
        teacher_name = ''
        # 获取所有课程对应的老师
        for courseToTeacher in commons.get_all_list(course_to_teacher_list):
            # 匹配当成课程对应的老师
            if course.nid.uuid ==  courseToTeacher.course_id.uuid:
                teacher_name = courseToTeacher.teacher_id.get_obj_by_uuid().name
                break

        print('%d. %s；老师名称：%s' % (index, course, teacher_name))

    return True


def score(tip, student):
    print('======%s======' % tip)

    score_dict = student.score.score_dict
    for course_to_teacher_nid in score_dict:
        course_name = course_to_teacher_nid.get_obj_by_uuid().course_id.get_obj_by_uuid().name
        print('%s : %s\n' % (course_name, score_dict[course_to_teacher_nid]))

    return True

def main():
    choices_init = [
        {
            'name': '登录',
            'method': login
        },
        {
            'name': '注册',
            'method': register
        }
    ]

    student = commons.to_choices(choices_init)

    choices_main = [
        {
            'name': '选课',
            'method': choice_course,
            'args': student
        },
        {
            'name': '查看成绩单',
            'method': score,
            'args': student
        }
    ]
    commons.to_choices_args(choices_main)
