# -*- coding: utf-8 -*-

# 作者：Sosai
# 时间：2022/1/14  16:58 
# 名称：saucenao.PY
# 工具：PyCharm

# SauceNao识图基本处理
import requests
from typing import Optional, BinaryIO, Union
from assistclass.SauceNaoResult import SearchResults


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

        self.header = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) \
            AppleWebKit/537.36 (KHTML, like Gecko) \
            Chrome/88.0.4324.146 Safari/537.36',
        }
        self.proxy = {'http': 'http://127.0.0.1:10809',
                      'https': 'https://127.0.0.1:10809'}

    # 根据url搜索图片
    def searchFromUrl(self, url: str) -> Union[SearchResults, str]:
        params = self.params.copy()
        params['url'] = url
        results = self._search(params)
        return results

    # 根据本地文件搜索图片
    def searchFromFile(self, file: BinaryIO) -> Union[SearchResults, str]:
        files = {'file': file}
        results = self._search(self.params, files)
        return results

    def _search(self, params, files=None):
        response = requests.post(self.sauceUrl, params=params, files=files, headers=self.header, proxies=self.proxy)
        status_code = response.status_code
        # 请求成功返回json结果
        if status_code == 200:
            # print(response.json())
            results = SearchResults(response.json())
            return results

        # 请求失败的情况
        elif status_code == 403:
            return "请求失败，apikey无效"

        elif status_code == 413:
            return "请求失败，文件太大了"

        elif status_code == 429:
            if 'Daily' in response.json()['header']['message']:
                return '24小时内图片搜索数目达到上限'
            return '30秒内图片搜索数目达到上限'

        return f'发生了错误，服务器返回了错误代码 {status_code}'
