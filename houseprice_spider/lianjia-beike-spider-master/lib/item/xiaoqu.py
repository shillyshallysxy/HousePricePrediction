#!/usr/bin/env python
# coding=utf-8
# author: zengyuetian
# 此代码仅供学习与交流，请勿用于商业用途。
# 小区信息的数据结构
from lib.item.fangzi import FangZi

class XiaoQu(object):
    def __init__(self, district, area, name, price, on_sale, developer, fangzi):
        self.district = district
        self.area = area
        self.price = price
        self.name = name
        self.on_sale = on_sale
        self.developer = developer
        self.fangzi = fangzi

    def text(self):
        return self.district + "," + \
                self.area + "," + \
                self.name + "," + \
                self.developer + "," + \
                self.price + "," + \
                self.on_sale + "," + \
                self.fangzi.text()
