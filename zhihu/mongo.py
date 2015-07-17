# coding:utf-8
import pymongo
import sys
import jieba
import jieba.analyse
import copy

reload(sys)
sys.setdefaultencoding('utf-8')

db = pymongo.MongoClient('localhost', 27017).scrapy

questions = db.zhihu.find()

for question in questions:
    tags = jieba.analyse.extract_tags(question['question'], 10, True)
    for tag, num in tags:
        #如果已存在，更新原来的记录
        if db.index.find({tag: {'$exists': True}}).count():
            old = db.index.find_one({tag: {'$exists': True}})

            old_cache = copy.deepcopy(old[tag])  # 必须用深拷贝

            #更新原来的记录，并插入数据库
            old[tag].update({str(question['_id']): num})
            db.index.update({tag: old_cache}, {tag: old[tag]})
        #不存在则插入数据。（关键字不能包含'.'等...）
        else:
            if '.' not in tag:
                db.index.insert({tag: {str(question['_id']): num}})

