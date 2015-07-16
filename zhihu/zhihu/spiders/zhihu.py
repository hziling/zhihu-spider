# -*- coding: utf-8 -*-
import scrapy
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from scrapy import Request, FormRequest
from ..items import ZhihuItem
from ..settings import COOKIES


class ZhihuSpider(CrawlSpider):
    name = "zhihu"
    allowed_domains = ["zhihu.com"]
    login_page = 'http://www.zhihu.com/#signin'

    start_urls = (
        'http://www.zhihu.com/topics',
        # 'http://www.zhihu.com/question/20091578',
    )
    rules = (
        # Rule(LinkExtractor(allow=[r'/question/\d{8}/log$']), callback='logined_parse'),
        # Rule(LinkExtractor(allow=['www.zhihu.com/people/followees'], deny=['followees', 'followers', 'followed', 'topics']), follow=False),
        # Rule(LinkExtractor(allow=['www.zhihu.com/people/']), follow=True),
        Rule(LinkExtractor(allow=[r'/question/\d{8}$']), callback='question_parse'),
        Rule(LinkExtractor(allow=['/topic/\d{8}$'], deny=['answer']), follow=True),
        # Rule(LinkExtractor(allow=['/followees']), follow=False, callback='unlogined_parse'),
    )

    cookies = COOKIES

    headers = {
        "Accept": "*/*",
        "Accept-Encoding": "gzip,deflate",
        "Accept-Language": "en-US,en;q=0.8,zh-TW;q=0.6,zh;q=0.4",
        "Connection": "keep-alive",
        "Content-Type":" application/x-www-form-urlencoded; charset=UTF-8",
        "User-Agent": "Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.8.1.12) Gecko/20080219 Firefox/2.0.0.12 Navigator/9.0.0.6",
        "Referer": "http://www.zhihu.com/"
    }

    #重写了爬虫类的方法, 实现了自定义请求, 运行成功后会调用callback回调函数
    def start_requests(self):
        # for i, url in enumerate(self.login_page):
            # yield scrapy.Request(url, meta={'cookiejar': i}, callback=self.post_login)
        # return [Request(self.login_page, meta={'cookiejar': 0}, callback=self.post_login)]
        return [Request(self.login_page, callback=self.post_login)]

    def post_login(self, response):
        print 'Preparing login'
        #下面这句话用于抓取请求网页后返回网页中的_xsrf字段的文字, 用于成功提交表单
        xsrf = response.xpath('//input[@name="_xsrf"]/@value').extract()[0]
        print xsrf
        #FormRequeset.from_response是Scrapy提供的一个函数, 用于post表单
        #登陆成功后, 会调用after_login回调函数
        return [FormRequest.from_response(response,   #"http://www.zhihu.com/#signin",
                            # meta={'cookiejar': response.meta['cookiejar']},
                            headers=self.headers,  #注意此处的headers
                            formdata={
                                '_xsrf': xsrf,
                                'email': '2280909422@qq.com',
                                'password': '123123'
                            },
                            cookies=self.cookies,
                            callback=self.after_login,
                            )]

    def after_login(self, response):
        for url in self.start_urls:
            yield self.make_requests_from_url(url)

    def question_log_parse(self, response):

        item = response.meta['item']
        # item = ZhihuItem()
        # item['url'] = response.url
        item['question'] = response.xpath("//div[@id='zh-question-title']/h2/a/text()").extract()[0]
        item['follow_count'] = int(response.xpath("//div[@class='zg-gray-normal']/a/strong/text()").extract()[0])
        # item['scan_count'] = response.xpath("/html/body/div[3]/div[2]/div[3]/div/div[2]/strong[1]").extract()
        item = response.meta['item']
        # answer_count = response.xpath("//h3[@id='zh-question-answer-num']/text()").re(r'(\d+)')
        # item['answer_count'] = int(answer_count[0]) if answer_count else 1
        item['created'] = response.xpath("//*[@id='zh-question-log-list-wrap']/div[1]/div[@class='zm-item-meta']/time/text()").extract()[0]

        yield item

    def question_parse(self, response):
        self.log('A response from %s just arrived!' % response.url)
        item = ZhihuItem()
        item['url'] = response.url
        # item['question'] = response.xpath("//*[@id='zh-question-title']/h2/text()").re(r'.+')[0]
        # item['follow_count'] = int(response.xpath('//*[@id="zh-question-side-header-wrap"]/text()').re(r'(\d+)')[0])
        answer_count = response.xpath('//div[@class="zh-answers-title clearfix"]/h3/text()').re(r'(\d+)')
        item['answer_count'] = int(answer_count[0]) if answer_count else 1

        # 传递参数给question_log_parse，因为要抓取时间
        request = Request(response.url+'/log', callback=self.question_log_parse)
        request.meta['item'] = item

        return request


    def unlogined_parse(self, response):
        with open('zhihu.html', 'wb') as f:
            f.write(response.body)
        # print response.body
        # self.log('A response from %s just arrived!' % response.url)
        # item = ZhihuItem()
        # item['url'] = response.url
        # item['question'] = response.xpath("//*[@id='zh-question-title']/h2/text()").re(r'.+')[0]
        # item['follow_count'] = int(response.xpath('//*[@id="zh-question-side-header-wrap"]/text()').re(r'(\d+)')[0])
        # answer_count = response.xpath('//div[@class="zh-answers-title clearfix"]/h3/text()').re(r'(\d+)')
        # item['answer_count'] = int(answer_count[0]) if answer_count else 1
        # yield item

