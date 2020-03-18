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


def class_info(tip, teacher):
    """
    查看班级信息
    :param tip: 提示信息
    :param teacher: 老师对象
    :return:
    """
    print('======%s======' % tip)
    for classes in commons.get_all_list(models.Classes.db_path):
        for item in classes.course_to_teacher_list:
            if teacher.nid.uuid == item.teacher_id.uuid:
                print(classes)

    return True


def student_info(tip, teacher):
    """
    查看学生信息
    :param tip: 提示信息
    :param teacher: 老师对象
    :return:
    """
    print('======%s======' % tip)

    # 获取所有班级
    classes_list = commons.get_all_list(models.Classes.db_path)
    # 获取所有学生
    student_list = commons.get_all_list(models.Student.db_path)

    # 遍历所有班级
    for classes in classes_list:
        # 遍历班级对应的老师
        for course_to_teacher in classes.course_to_teacher_list:
            # 判断老师是否在该班级授课
            if course_to_teacher.teacher_id.uuid == teacher.nid.uuid:
                # 遍历所有学生
                for student in student_list:
                    # 判断学生是否在该班级
                    if classes.nid.uuid == student.classes_id.uuid:
                        print(student)

    return True


def set_student_score(tip, teacher):
    """
    设置学生分数
    :param tip: 提示信息
    :param teacher: 老师对象
    :return:
    """
    print('======%s======' % tip)

    # 获取所有班级
    classes_list = commons.get_all_list(models.Classes.db_path)
    # 获取所有学生
    student_list = commons.get_all_list(models.Student.db_path)
    teach_classes_list = []
    teach_student_list = []
    classes_index = ''
    student_index = ''
    select_classes = ''
    select_student = ''

    # 遍历所有班级
    for classes in classes_list:
        # 遍历班级对应的老师
        for course_to_teacher in classes.course_to_teacher_list:
            # 判断老师是否在该班级授课
            if course_to_teacher.teacher_id.uuid == teacher.nid.uuid:
                teach_classes_list.append(classes)

    # 遍历老师教学的班级列表
    for index, teach_classes in enumerate(teach_classes_list, 1):
        print('%d. %s' % (index, teach_classes.name))

    # 选择要设置学生分数的班级
    while classes_index == '':
        classes_index = input('请输入您要设置学生分数的班级序号：')

    classes_index = int(classes_index) - 1
    select_classes = teach_classes_list[classes_index]

    # 遍历所有学生
    for student in student_list:
        # 判断学生是否在该班级
        if classes_list[classes_index].nid.uuid == student.classes_id.uuid:
            teach_student_list.append(student)

    # 遍历老师教学的所有学生
    for index, teach_student in enumerate(teach_student_list, 1):
        print('%d. %s' % (index, teach_student.name))

    # 选择要设置学生分数的学生序号
    while student_index == '':
        student_index = input('请输入学生序号：')

    student_index = int(student_index) - 1
    select_student = teach_student_list[student_index]

    student_score = input('请输入分数：')

    course_to_teacher_nid = ''
    # 遍历班级对应的老师，找到该老师在 课程对应的老师 nid
    for course_to_teacher in select_classes.course_to_teacher_list:
        # 判断老师是否在该班级授课
        if course_to_teacher.teacher_id.uuid == teacher.nid.uuid:
            course_to_teacher_nid = course_to_teacher.nid
            break

    select_student.score.set(course_to_teacher_nid, student_score)
    select_student.save()

    # 遍历班级内的所欲学生

    return True


def main():
    print('======老师登录======')
    teacher = commons.login(models.Teacher.db_path)

    choices = [
        {
            'name': '查看班级信息',
            'method': class_info,
            'args': teacher
        },
        {
            'name': '查看学生信息',
            'method': student_info,
            'args': teacher
        },
        {
            'name': '设置学生分数',
            'method': set_student_score,
            'args': teacher
        }
    ]

    commons.to_choices_args(choices, True)
