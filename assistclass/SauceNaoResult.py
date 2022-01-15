# -*- coding: utf-8 -*-

# 作者：Sosai
# 时间：2022/1/15  17:20 
# 名称：SauceNaoResult.PY
# 工具：PyCharm

# 返回识图的结果
class SearchResults:
    def __init__(self, json):
        # pixiv识图结果
        if 'Pixiv Images' in json["results"][0]["header"]["index_name"]:
            self.website = 'pixiv'
            self.similarity = json["results"][0]["header"]["similarity"]  # 相似度
            self.thumbnail = json["results"][0]["header"]["thumbnail"]  # 识图的预览图
            self.title = json["results"][0]["data"]["title"]  # 标题
            self.ext_urls = json["results"][0]["data"]["ext_urls"][0]  # 图片原url
            self.member_name = json["results"][0]["data"]["member_name"]  # 画师名字
            self.pixiv_id = json["results"][0]["data"]["pixiv_id"]  # pixivID
        # danbooru识图结果
        elif 'Danbooru' in json["results"][0]["header"]["index_name"]:
            self.website = 'danbooru'
            self.similarity = json["results"][0]["header"]["similarity"]  # 相似度
            self.thumbnail = json["results"][0]["header"]["thumbnail"]  # 识图的预览图
            self.danbooru_id = json["results"][0]["data"]["danbooru_id"]  # danbooruID
            self.creator = json["results"][0]["data"]["creator"]  # 画师名字
            self.characters = json["results"][0]["data"]["characters"]  # 图片人物
            self.source = json["results"][0]["data"]["source"]  # 图片原url
            self.ext_urls = json["results"][0]["data"]["ext_urls"][0]  # danbooru图片url
        else:
            self.website = None

    def __str__(self):
        if self.website == 'pixiv':
            string = f"相似度：{self.similarity}\n标题：{self.title}\nurl：{self.ext_urls}\n画师：{self.member_name}\npixivID：{self.pixiv_id}"
        elif self.website == 'danbooru':
            string = f"相似度：{self.similarity}\n原url：{self.source}\ndanbooruUrl：{self.ext_urls}\n人物：{self.characters}\n上传者：{self.creator}\ndanbooruID：{self.danbooru_id}"
        else:
            string = '识图失败，未找到图片'
        return string
