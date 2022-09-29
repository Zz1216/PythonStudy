# !/usr/bin/python
# -*- coding: utf8 -*-
"""
 Package：
 User：loyal
 Date：2022/9/29
 Dscription：
"""
import random

student_names = ['A', 'B', 'C', 'D', 'E']
suject_names = ['1', '2', '3', '4', '5']

class_score = {}
for std in student_names:
    std_score = {}
    for suj in suject_names:
        std_score[suj] = random.randint(0,100)
    class_score[std] = std_score


def get_student_score(std_name, suj_name):
    """
    获取某个学生某个科目的成绩
    :param std_name: 学生名字
    :param suj_name: 科目名字
    :return: 得分
    """
    score = class_score[std_name][suj_name]
    return score


print(get_student_score('A', '2'))


