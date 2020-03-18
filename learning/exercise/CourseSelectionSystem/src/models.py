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

import pickle, os, time

from config import settings
from src import identifier
from lib import commons


class Base:
    """
    基类
    """

    def save(self):
        """
        使用 pickle 将用户对象保存到文件中
        :return:
        """
        pickle.dump(self, open(os.path.join(self.db_path, str(self.nid)), 'wb'))


class Admin(Base):
    """
    管理员
    """
    role = 'admin'
    db_path = settings.DB_DIR_DICT[role]

    def __init__(self, mobile, password, name):
        """
        创建管理员对象
        :param mobile: 管理员手机号码
        :param password: 管理员密码
        :param name: 管理员名称
        """
        self.nid = identifier.Nid(Admin.role)
        self.mobile = mobile
        self.password = password
        self.name = name
        self.create_time = time.strftime('%Y-%m-%d')

    def __str__(self):
        return "管理员名称：%s" % (self.name)

    @staticmethod
    def login():
        return commons.login(Admin.db_path)

    @staticmethod
    def register():
        obj = commons.register(Admin.db_path)
        name = ''

        while name == '':
            name = input('请输入管理员名称：').strip()

        user = Admin(obj['mobile'], obj['password'], name)
        user.save()

        return user


class School(Base):
    """
    学校
    """
    role = 'school'
    db_path = settings.DB_DIR_DICT[role]

    def __init__(self, name):
        """
        初始化
        :param name: 学校名称
        """
        self.nid = identifier.Nid(School.role)
        self.name = name
        self.income = 0

    def __str__(self):
        return "学校名称：%s" % (self.name)


class Teacher(Base):
    """
    老师
    """
    role = 'teacher'
    db_path = settings.DB_DIR_DICT[role]

    def __init__(self, mobile, password, name, level):
        """
        初始化
        :param name: 老师名称
        :param level: 老师级别
        """
        self.nid = identifier.Nid(Teacher.role)
        self.mobile = mobile
        self.password = password
        self.name = name
        self.level = level
        self.__account = 0

    def __str__(self):
        return "老师名称：%s；老师级别：%s" % (self.name, self.level)

    @staticmethod
    def login():
        return commons.login(Teacher.db_path)


class Course(Base):
    """
    课程
    """
    role = 'course'
    db_path = settings.DB_DIR_DICT[role]

    def __init__(self, name, price, period, school_id):
        """
        初始化
        :param name: 课程名称
        :param price: 课程价格
        :param period: 课程周期
        :param school_id: 学校ID，学校ID是一个对象，具有get_obj_by_uuid方法，以此获取学校对象（其中包含学校信息）
        """
        self.nid = identifier.Nid(Course.role)
        self.name = name
        self.price = price
        self.period = period
        self.school_id = school_id

    def __str__(self):
        return "课程名称：%s；课程价格：%s；课程周期：%s；所属学校：%s" % (
            self.name, self.price, self.period, self.school_id.get_obj_by_uuid().name
        )


class CourseToTeacher(Base):
    """
    课程对应的老师
    """
    role = 'course_to_teacher'
    db_path = settings.DB_DIR_DICT[role]

    def __init__(self, course_id, teacher_id):
        """
        初始化
        :param course_id: 课程ID
        :param teacher_id: 老师ID
        """
        self.nid = identifier.Nid(CourseToTeacher.role)
        self.course_id = course_id
        self.teacher_id = teacher_id

    def __str__(self):
        course = self.course_id.get_obj_by_uuid()
        teacher = self.teacher_id.get_obj_by_uuid()

        return "课程名称：%s；老师名称：%s" % (course.name, teacher.name)


class Classes(Base):
    """
    班级
    """
    role = 'classes'
    db_path = settings.DB_DIR_DICT[role]

    def __init__(self, name, tuition, school_id, course_to_teacher_list):
        """
        初始化
        :param name: 班级名称
        :param tuition: 学费
        :param school_id: 学校ID
        :param course_to_teacher_list: 课程对应的老师列表 [ CourseToTeacher, CourseToTeacher ]
        """
        self.nid = identifier.Nid(Classes.role)
        self.name = name
        self.tuition = tuition
        self.school_id = school_id
        self.course_to_teacher_list = course_to_teacher_list

    def __str__(self):
        school = self.school_id.get_obj_by_uuid()
        course_to_teacher_list = []

        for item in self.course_to_teacher_list:
            obj = item.nid.get_obj_by_uuid()
            course = obj.course_id.get_obj_by_uuid()
            teacher = obj.teacher_id.get_obj_by_uuid()
            course_to_teacher_list.append("课程名称：%s；老师名称：%s" % (course.name, teacher.name))

        return "班级名称：%s；学费：%s；所属学校：%s；\n 任课老师：\n  %s" % (
            self.name, self.tuition, school.name, '；\n  '.join(course_to_teacher_list)
        )


class Score(Base):
    """
    成绩单
    """

    def __init__(self, student_id):
        """
        初始化
        :param student_id: 学生ID
        """
        self.student_id = student_id
        self.score_dict = {}

    def set(self, course_to_teacher_nid, score):
        """
        设置课程对应老师ID的成绩分
        :param course_to_teacher_nid: 课程对应老师ID
        :param score:
        :return:
        """
        self.score_dict[course_to_teacher_nid] = score

    def get(self, course_to_teacher_nid):
        """
        获取课程对应老师ID的成绩分
        :param course_to_teacher_nid: 课程对应老师ID
        :return:
        """
        return self.score_dict.get(course_to_teacher_nid, None)


class Student(Base):
    """
    学生
    """
    role = 'student'
    db_path = settings.DB_DIR_DICT[role]

    def __init__(self, mobile, password, name, age, classes_id):
        """
        初始化
        :param mobile: 学生手机号码
        :param password: 学生手机密码
        :param name: 学生名称
        :param age: 学生年龄
        :param classes_id: 班级ID
        """
        self.nid = identifier.Nid(Student.role)
        self.mobile = mobile
        self.password = password
        self.name = name
        self.age = age
        self.classes_id = classes_id
        self.score = Score(self.nid)

    def __str__(self):
        score_dict = self.score.score_dict
        scores = ''

        for key, course_to_teacher_nid in score_dict:
            course_name = course_to_teacher_nid.get_obj_by_uuid().course_id.get_obj_by_uuid().name
            score = score_dict[course_to_teacher_nid]
            scores += '课程名称：%s；分数：%s\n' % (course_name, score)

        return "学生名称：%s；学生手机号码：%s；学生年龄：%s；\n 学生成绩：\n  %s" % (
            self.name, self.mobile, self.age, scores
        )

    @staticmethod
    def register():
        obj = commons.register(Admin.db_path)

        name = ''
        age = ''

        while name == '':
            name = input('请输入学生名称：').strip()

        while age == '':
            age = input('请输入学生年龄：').strip()

        classes_obj = commons.choice_model(Classes.db_path, '班级')

        student = Student(obj['mobile'], obj['password'], name, age, classes_obj.nid)
        student.save()

        return student

    @staticmethod
    def login():
        return commons.login(Student.db_path)

