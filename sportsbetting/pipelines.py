# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html


class SportsbettingPipeline(object):
    def close_spider(self, spider):
        f = open('stat.txt', 'r')
        pos=int(f.read())
        f.close()
        print('Stat: ', pos)
        change=int(input('Change? '))
        changed=pos+change
        print('New:', changed)
        f = open('stat.txt', 'w')
        f.write(str(changed))
        f.close()


    def process_item(self, item, spider):
        return item
