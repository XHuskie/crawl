# -*- coding: utf-8 -*-
import scrapy
import json
from Lagou.items import LagouItem


class LagouSpider(scrapy.Spider):
    name = 'lagou'
    allowed_domains = ['lagou.com']
    kd = input('请输入要搜索的职位：')
    ct = input('请输入要搜索的城市：')
    page = 1
    start_urls = ['https://www.lagou.com/jobs/list_"+str(kd)+"&city="+str(ct)']
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36",
        "Referer": "https://www.lagou.com/jobs/list_python",
        "Cookie": "_ga=GA1.2.94415486.1531289341; user_trace_token=20180711140901-e7dd0bc1-84d0-11e8-883f-525400f775ce; LGUID=20180711140901-e7dd127e-84d0-11e8-883f-525400f775ce; index_location_city=%E5%8C%97%E4%BA%AC; WEBTJ-ID=20180731183320-164efe63e4294-0958087626bef-5701f32-1049088-164efe63e442f7; _gid=GA1.2.1628244110.1533033202; Hm_lvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1532400996,1532401022,1533033203,1533033209; LGSID=20180731183329-2a3760c3-94ad-11e8-a085-5254005c3644; JSESSIONID=ABAAABAABEEAAJA0DF896472E3DE6F75068BC3924A33574; TG-TRACK-CODE=search_code; LGRID=20180731184554-e689e3f2-94ae-11e8-a085-5254005c3644; Hm_lpvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1533033955; SEARCH_ID=7d347d423ea4474aae105e84c2d756e5"
    }

    def parse(self, response):
        formdata = {'first': 'true', 'kd': str(self.kd), 'pn': '1', 'city': str(self.ct)}
        url = "https://www.lagou.com/jobs/positionAjax.json?needAddtionalResult=false"
        yield scrapy.FormRequest(url, callback=self.parse_lagou, formdata=formdata)

    def parse_lagou(self, response):
        text = json.loads(response.text)
        print(text)
        res = []
        try:
            res = text["content"]["positionResult"]["result"]
        except:
            pass
        if len(res) > 0:
            item = LagouItem()
            for position in res:
                try:
                    item['title'] = position['positionName']
                    item['education'] = position['education']
                    item['company'] = position['companyFullName']
                    item['experience'] = position['workYear']
                    item['location'] = position['city']
                    item['salary'] = position['salary']
                    print(item)
                except:
                    pass
                yield item
            self.page += 1
            url = 'https://www.lagou.com/jobs/positionAjax.json?needAddtionalResult=false'
            formdata = {'first': 'false', 'kd': str(self.kd), 'pn': str(self.page), 'city': str(self.ct)}
            print('===========================', formdata)
            yield scrapy.FormRequest(url, callback=self.parse_lagou, formdata=formdata, headers=self.headers)
        else:
            print('爬虫结束了！')
