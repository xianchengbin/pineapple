# -*- coding:utf-8 -*-
import numpy as np

positionss = [[(129, 6), (236, 6), (343, 6)], [(22, 137), (129, 137), (236, 137), (343, 137), (450, 137)], [(22, 267), (129, 267), (236, 267), (343, 267), (450, 267)]]

def getPosition(position):
    for index, value in enumerate(positionss):
        index1 = index
        positions = value
        for index, value in enumerate(positions):
            if value[0] - 10 < position[0] and value[0] + 10 > position[0] and value[1] - 10 < position[1] and value[1] + 10 > position[1]:
                return index1, index


def remindAndSort(list):
    temp = []
    for item in list:
        remind = item
        while remind > 13:
            remind = remind - 13
        if remind == 0:
            remind = 13
        if remind == 1:
            remind = 14
        temp.append((remind, item))
    return sorted(temp, key=lambda student: student[0])


def isFlush(list):
    judge = -1
    for item in list:
        temp = 0
        if item % 13 == 0:
            temp = -1
        temp = temp + item / 13
        if judge == -1:
            judge = temp
            continue
        if judge != temp:
            return False
    return True

def isSame(list):
    temp = list[0]
    for item in list:
        if item != temp:
            return False
    return True


def isStraight(list):
    if len(list) >= 4 and list[-1] - list[0] < 5:
        for i in range(0, len(list)-1):
            if list[i] == list[i+1]:
                return False
        return True
    elif list[0] == 1:
        newTempList = list[1::1]
        newTempList.append(14)
        return isStraight(newTempList)
    return False


def isPineApple(num):
    return num == 1 or num == 12 or num == 13


def put(row, result, value):
    if row == 0 and len(result[0]) < 3:
        result[0].append(value)
        return True
    elif row == 1 and len(result[1]) < 5:
        result[1].append(value)
        return True
    elif row == 2 and len(result[2]) < 5:
        result[2].append(value)
        return True


def getResultFor5(list, all):
    result = [[], [], []]
    for i in range(0, 3):
        for j in range(0, 3):
            for k in range(0, 3):
                for m in range(0, 3):
                    for n in range(0, 3):
                        put(i, result, list[0])
                        put(j, result, list[1])
                        put(k, result, list[2])
                        put(m, result, list[3])
                        put(n, result, list[4])
                        if len(result[0]) + len(result[1]) + len(result[2]) == 5:
                            # print result
                            all.append(result)
                        result = [[], [], []]


def getResultFor2(list, all, init, judgeIsBoom):
    result = [[], [], []]
    result[0] = init[0][:]
    result[1] = init[1][:]
    result[2] = init[2][:]
    for i in range(0, 3):
        for j in range(0, 3):
            if put(i, result, list[0]) and put(j, result, list[1]):
                # print result
                temp = [[], [], []]
                temp[0] = result[0][:]
                temp[1] = result[1][:]
                temp[2] = result[2][:]
                if judgeIsBoom:
                    tempForIsBoom = []
                    global notBoomSet
                    if len(temp[0]) == 3:
                        tempForIsBoom.append(temp[0][::1])
                    if len(temp[1]) == 5:
                        tempForIsBoom.append(temp[1][::1])
                    if len(temp[2]) == 5:
                        tempForIsBoom.append(temp[2][::1])
                    if len(tempForIsBoom) == 2:
                        keyString = ""
                        for item in sorted(tempForIsBoom[0]):
                            keyString += str(item) + ","
                        keyString += "n"
                        for item in sorted(tempForIsBoom[1]):
                            keyString += str(item) + ","
                        if keyString not in notBoomSet:
                            if not isNotBoom(tempForIsBoom):
                                continue
                            else:
                                keyString = ""
                                for item in sorted(tempForIsBoom[0]):
                                    keyString += str(item) + ","
                                keyString += "n"
                                for item in sorted(tempForIsBoom[1]):
                                    keyString += str(item) + ","
                                notBoomSet.add(keyString)
                    elif len(tempForIsBoom) == 3 and not isNotBoom(tempForIsBoom):
                        continue
                all.append(temp)
            result[0] = init[0][:]
            result[1] = init[1][:]
            result[2] = init[2][:]


# 赖子
def isRogue(value):
    return value == 53 or value == 54


# 比大小
def compare(list1, list2):
    # if list1[0] == 1:
    #     newTempList = list1[1::1]
    #     newTempList.append(14)
    #     return compare(newTempList, list2)
    # if list2[0] == 1:
    #     newTempList = list2[1::1]
    #     newTempList.append(14)
    #     return compare(list1, newTempList)
    for i in range(len(list1) -1, -1, -1):
        if list1[i] > list2[i]:
            return True
        elif list1[i] == list2[i]:
            continue
        else:
            return False
    return True


def compareFive(downList, upList, point):
    # downList = []
    # upList = []
    # for down in downListIncludeA:
    #     if down == 1:
    #         downList.append(14)
    #     else:
    #         downList.append(down)
    # for up in upListIncludeA:
    #     if up == 1:
    #         upList.append(14)
    #     else:
    #         upList.append(up)
    # downList.sort()
    # upList.sort()
    # 四条
    if point == 10:
        return downList[1] >= upList[1]
    # 皇家同花顺
    elif point == 25:
        return True
    # 同花顺 or 顺子
    elif point == 15 or point == 2:
        return compare(downList[:5:1], upList[:5:1])
    # 同花
    elif point == 4:
        return compare(downList[:5:1], upList[:5:1])
    elif point == 1:
        downListTemp = []
        upListTemp = []
        if isSame(downList[:3:1]):
            downListTemp.append(downList[3])
            downListTemp.append(downList[4])
            downListTemp.append(downList[0])
        elif isSame(downList[1:4:1]):
            downListTemp.append(downList[0])
            downListTemp.append(downList[4])
            downListTemp.append(downList[1])
        elif isSame(downList[2:5:1]):
            downListTemp.append(downList[0])
            downListTemp.append(downList[1])
            downListTemp.append(downList[2])
        if isSame(upList[:3:1]):
            upListTemp.append(upList[3])
            upListTemp.append(upList[4])
            upListTemp.append(upList[0])
        elif isSame(upList[1:4:1]):
            upListTemp.append(upList[0])
            upListTemp.append(upList[4])
            upListTemp.append(upList[1])
        elif isSame(upList[2:5:1]):
            upListTemp.append(upList[0])
            upListTemp.append(upList[1])
            upListTemp.append(upList[2])
        return compare(downListTemp, upListTemp)
    elif point == 0:
        downListTemp = []
        upListTemp = []
        if isSame(downList[0:2:1]) and isSame(downList[2:4:1]):
            downListTemp.append(downList[4])
            downListTemp.append(downList[0])
            downListTemp.append(downList[2])
        elif isSame(downList[0:2:1]) and isSame(downList[3:5:1]):
            downListTemp.append(downList[2])
            downListTemp.append(downList[0])
            downListTemp.append(downList[3])
        elif isSame(downList[1:3:1]) and isSame(downList[3:5:1]):
            downListTemp.append(downList[0])
            downListTemp.append(downList[1])
            downListTemp.append(downList[3])
        if isSame(upList[0:2:1]) and isSame(upList[2:4:1]):
            upListTemp.append(upList[4])
            upListTemp.append(upList[0])
            upListTemp.append(upList[2])
        elif isSame(upList[0:2:1]) and isSame(upList[3:5:1]):
            upListTemp.append(upList[2])
            upListTemp.append(upList[0])
            upListTemp.append(upList[3])
        elif isSame(upList[1:3:1]) and isSame(upList[3:5:1]):
            upListTemp.append(upList[0])
            upListTemp.append(upList[1])
            upListTemp.append(upList[3])
        return compare(downListTemp, upListTemp)
    elif point == -1:
        downListTemp = []
        upListTemp = []
        if isSame(downList[0:2:1]):
            downListTemp.append(downList[2])
            downListTemp.append(downList[3])
            downListTemp.append(downList[4])
            downListTemp.append(downList[0])
        elif isSame(downList[1:3:1]):
            downListTemp.append(downList[0])
            downListTemp.append(downList[3])
            downListTemp.append(downList[4])
            downListTemp.append(downList[1])
        elif isSame(downList[2:4:1]):
            downListTemp.append(downList[0])
            downListTemp.append(downList[1])
            downListTemp.append(downList[4])
            downListTemp.append(downList[2])
        elif isSame(downList[3:4:1]):
            downListTemp.append(downList[0])
            downListTemp.append(downList[1])
            downListTemp.append(downList[2])
            downListTemp.append(downList[3])
        if isSame(upList[0:2:1]):
            upListTemp.append(upList[2])
            upListTemp.append(upList[3])
            upListTemp.append(upList[4])
            upListTemp.append(upList[0])
        elif isSame(upList[1:3:1]):
            upListTemp.append(upList[0])
            upListTemp.append(upList[3])
            upListTemp.append(upList[4])
            upListTemp.append(upList[1])
        elif isSame(upList[2:4:1]):
            upListTemp.append(upList[0])
            upListTemp.append(upList[1])
            upListTemp.append(upList[4])
            upListTemp.append(upList[2])
        elif isSame(upList[3:4:1]):
            upListTemp.append(upList[0])
            upListTemp.append(upList[1])
            upListTemp.append(upList[2])
            upListTemp.append(upList[3])
        return compare(downListTemp, upListTemp)
    elif point == -2:
        return compare(downList, upList)


def calFive(list, actual):
    # 四条
    if isSame(list[:4:1]):
        return 10
    elif isSame(list[1:5:1]):
        return 10
    # 同花顺
    elif isFlush(actual) and isStraight(list):
        if list[0] == 1 and list[4] == 13:
            return 25
        else:
            return 15
    # 顺子
    elif isStraight(list):
        return 2
    # 同花
    elif isFlush(actual):
        return 4
    # 三条
    if isSame(list[:3:1]):
        return 1
    elif isSame(list[1:4:1]):
        return 1
    elif isSame(list[2:5:1]):
        return 1
    # 两对
    elif isSame(list[0:2:1]) and (isSame(list[2:4:1]) or isSame(list[3:5:1])):
        return 0
    elif isSame(list[1:3:1]) and isSame(list[3:5:1]):
        return 0
    # 一对
    elif isSame(list[0:2:1]) or isSame(list[1:3:1]) or isSame(list[2:4:1]) or isSame(list[3:5:1]):
        return -1
    else:
        return -2


def calThree(list):
    # list = []
    # for includeA in listIncludeA:
    #     if includeA == 1:
    #         list.append(14)
    #     else:
    #         list.append(includeA)
    # list.sort()
    if isSame(list):
        return list[0] + 8
    if isSame(list[:2:1]) or isSame(list[1:3:1]):
        return list[1] - 5
    return -5


def isNotBoom(listTemp):
    listTuples = []
    for listTempSingle in listTemp:
        listTuples.append(remindAndSort(listTempSingle))
    list = []
    actual = []
    for listTuple in listTuples:
        listSingleTemp = []
        actualSingleTemp = []
        for listSingle in listTuple:
            listSingleTemp.append(listSingle[0])
            actualSingleTemp.append(listSingle[1])
        list.append(listSingleTemp)
        actual.append(actualSingleTemp)
    point1 = 0
    if len(listTemp) == 3:
        point1 = calFive(list[1], actual[1])
        point2 = calFive(list[2], actual[2])
        if point1 == point2:
            if compareFive(list[1], list[2], point1):
                return False
        elif point1 > point2:
            return False
    # 如果是只有中道和尾道
    elif len(list[0]) == 5:
        point1 = calFive(list[0], actual[0])
        point2 = calFive(list[1], actual[1])
        if point1 == point2:
            if compareFive(list[0], list[1], point1):
                return False
        elif point1 > point2:
            return False
        return True
    else:
        point1 = calFive(list[1], actual[1])
    if point1 >= 2:
        return True
    list1 = list[1]
    point0 = calThree(list[0])
    list1ForThree = []
    # 中道三条
    if point1 == 1:
        if point0 < 10:
            return True
        if isSame(list1[:3:1]):
            list1ForThree = list1[:3:1]
        elif isSame(list1[1:4:1]):
            list1ForThree = list1[1:4:1]
        elif isSame(list1[2:5:1]):
            list1ForThree = list1[2:5:1]
        return compare(list1ForThree, list[0])
    # 中道两对
    elif point1 == 0:
        if point0 >= 10:
            return False
        else:
            return True
    # 中道一对
    elif point1 == -1:
        if point0 >= 10:
            return False
        elif point0 <= -5:
            return True
        else:
            if isSame(list1[0:2:1]):
                list1ForThree.append(list1[4])
                list1ForThree.append(list1[0])
                list1ForThree.append(list1[1])
            elif isSame(list1[1:3:1]):
                list1ForThree.append(list1[4])
                list1ForThree.append(list1[1])
                list1ForThree.append(list1[2])
            elif isSame(list1[2:4:1]):
                list1ForThree.append(list1[4])
                list1ForThree.append(list1[2])
                list1ForThree.append(list1[3])
            elif isSame(list1[3:5:1]):
                list1ForThree.append(list1[2])
                list1ForThree.append(list1[3])
                list1ForThree.append(list1[4])
            return compare(list1ForThree, list[0])
    elif point1 == -2:
        if point0 > -5:
            return False
        else:
            return compare(list1[2:5:1], list[0])

global notBoomSet
notBoomSet = set()
all = []
all2 = []
all3 = []
all4 = []
all5 = []
a1 = [13, 12, 14, 24, 34]
a2 = [1, 2]
a3 = [3, 4]
a4 = [5, 6]
a5 = [7, 8]
getResultFor5(a1, all)
for a in all:
    getResultFor2(a2, all2, a, False)
for a in all2:
    getResultFor2(a3, all3, a, True)
for a in all3:
    getResultFor2(a4, all4, a, True)
for a in all4:
    getResultFor2(a5, all5, a, True)
# boomCount = 0
# for item in all5:
#     if not isNotBoom(item):
#         boomCount = boomCount + 1

for item in all5:
    listTuples = []
    for listTempSingle in item:
        listTuples.append(remindAndSort(listTempSingle))
    list = []
    actual = []
    for listTuple in listTuples:
        listSingleTemp = []
        actualSingleTemp = []
        for listSingle in listTuple:
            listSingleTemp.append(listSingle[0])
            actualSingleTemp.append(listSingle[1])
        list.append(listSingleTemp)
        actual.append(actualSingleTemp)
    point0 = calThree(list[0])
    if point0 < 0:
        point0 = 0
    point1 = calFive(list[1], actual[1])
    point1 = point1 * 2
    if point1 < 0:
        point1 = 0
    point2 = calFive(list[2], actual[2])
    if point2 < 2:
        point2 = 0
    if point0 + point1 + point2 > 15:
        print item
        print point0, point1, point2







# a = [13, 12, 14, 24, 36]
# result[0].append(a[0])
# print result
# print firstFive(a)
# print isSame(a[:])
# print isFlush(a)