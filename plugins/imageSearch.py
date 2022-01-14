# -*- coding: utf-8 -*-

# 作者：Sosai
# 时间：2022/1/14  16:58 
# 名称：imageSearch.PY
# 工具：PyCharm

# SauceNao识图基本处理
import requests
from typing import Optional, BinaryIO, Union


# 返回识图的结果
class SearchResults:
    def __init__(self, json):
        self.similarity = json["results"][0]["header"]["similarity"]  # 相似度
        self.thumbnail = json["results"][0]["header"]["thumbnail"]  # 识图的预览图
        self.title = json["results"][0]["data"]["title"]  # 标题
        self.ext_urls = json["results"][0]["data"]["ext_urls"][0]  # 图片原url
        self.member_name = json["results"][0]["data"]["member_name"]  # 画师名字
        self.pixiv_id = json["results"][0]["data"]["pixiv_id"]

    def __str__(self):
        string = f"相似度：{self.similarity}\n标题：{self.title}\nurl：{self.ext_urls}\n画师：{self.member_name}"
        return string


# 图片识别
class SauceNaoSearch:
    def __init__(
            self,
            api_key: Optional[str] = None,
            output_type: int = 2,
            minsim: str = '80!',
            numres: int = 1,
            dbmask: int = 999,
    ):
        self.sauceUrl = 'https://saucenao.com/search.php'  # 起始url
        params = dict()

        if api_key is not None:
            params['api_key'] = api_key

        params['output_type'] = output_type  # 输出格式，默认2是json
        params['minsim'] = minsim  # 识别精度，默认80即可
        params['numres'] = numres  # 返回识图结果的个数
        params['dbmask'] = dbmask  # 搜索的数据库范围
        self.params = params

    # 根据url搜索图片
    def searchFromUrl(self, url: str) -> Union[SearchResults, int]:
        params = self.params.copy()
        params['url'] = url
        results = self._search(params)
        return results

    # 根据本地文件搜索图片
    def searchFromFile(self, file: BinaryIO) -> Union[SearchResults, int]:
        files = {'file': file}
        results = self._search(self.params, files)
        return results

    def _search(self, params, files=None):
        response = requests.post(self.sauceUrl, params=params, files=files)
        status_code = response.status_code
        # 请求成功返回json结果
        if status_code == 200:
            results = SearchResults(response.json())
            return results
        # 请求失败返回状态码
        else:
            return status_code

        # 请求失败的情况
        # elif status_code == 403:
        #     raise "请求失败，apikey无效"
        #
        # elif status_code == 413:
        #     raise "请求失败，文件太大了"
        #
        # elif status_code == 429:
        #     if 'Daily' in response.json()['header']['message']:
        #         raise '24小时内图片搜索数目达到上限'
        #     raise '30秒内图片搜索数目达到上限'
        #
        # raise f'发生了错误，服务器返回了错误代码 {status_code}'
