# -*- coding: utf-8 -*-


import scrapy


class ClubActivityFriendScrapyItem(scrapy.Item):
    """论坛统计活跃车友数量"""
    bbs_id = scrapy.Field()  # 论坛ID
    activity_friend_count = scrapy.Field()  # 总共活跃车友数
    time = scrapy.Field()  # 采集时间

    def get_insert_sql(self):
        insert_sql = """insert into auto_home_club_activity_friend (bbs_id, activity_friend_count,update_time) VALUES (%s, %s,str_to_date(%s,'%%Y-%%m-%%d')) """
        params = (self["bbs_id"], self["activity_friend_count"], self["time"])
        return insert_sql, params

    def distinct_data(self):
        query = """select id from auto_home_club_activity_friend where id =%s"""
        params = (0)
        return query, params
