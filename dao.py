#!/usr/bin/env python
# -*- coding:utf-8 -*-
import redis
import json

pool = redis.ConnectionPool(host='192.168.2.11', port=6380, password='56458368e0f55aebaa003a55')
r = redis.Redis(connection_pool=pool)
#构造字典
python2json = {}
#构造list
listData = [1,2,3]
python2json["listData"] = listData
python2json["strData"] = "test python obj 2 json"
#转换成json字符串
json_str = json.dumps(python2json)
r.set('1_2_3', json_str)
print r.keys('1_*_3')
# print json.loads(r.get('1_*_3'))['listData']

