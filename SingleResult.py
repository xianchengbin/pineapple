#!/usr/bin/env python
# -*- coding:utf-8 -*-


class SingleResult:
    def __init__(self, list, point, fantasy):
        self.list = list
        self.point = point
        self.fantasy = fantasy

    def getList(self):
        return self.list

    def getPoint(self):
        return self.point

    def getFantasy(self):
        return self.fantasy

    def isSub(self, subList):
        includes = [False, False, False]
        for i in range(0, 3):
            for sub in subList[i]:
                for item in list[i]:
                    if sub == item:
                        includes[i] = True
                        break
        for include in includes:
            if not include:
                return False
        return True


