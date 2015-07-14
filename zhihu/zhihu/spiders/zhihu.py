# -*- coding: utf-8 -*-
import scrapy
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from ..items import ZhihuItem


class ZhihuSpider(CrawlSpider):
    name = "zhihu"
    allowed_domains = ["zhihu.com"]
    start_urls = (
        'http://www.zhihu.com',
    )
    rules = (
        # Rule(LinkExtractor(allow=[r'/question/\d{8}/log$']), callback='logined_parse'),
        Rule(LinkExtractor(allow=['www.zhihu.com/people/'], deny=['followees', 'followers', 'followed', 'topics']), follow=True),
        Rule(LinkExtractor(allow=['www.zhihu.com/question/\d{8}$']), callback='unlogined_parse'),
    )

    def logined_parse(self, response):
        item = ZhihuItem()
        item['url'] = response.url
        item['question'] = response.xpath("//div[@id='zh-question-title']/h2/a/text()").extract()
        item['follow_count'] = response.xpath("//div[@class='zg-gray-normal']/a/strong/text()").extract()
        item['scan_count'] = response.xpath("/html/body/div[3]/div[2]/div[3]/div/div[2]/strong[1]").extract()
        item['created'] = response.xpath("/html/body/div[3]/div[1]/div/div[3]/div[3]/div[3]/time").extract()

        yield item

    def unlogined_parse(self, response):
        # self.log('A response from %s just arrived!' % response.url)
        item = ZhihuItem()
        item['url'] = response.url
        item['question'] = response.xpath("//*[@id='zh-question-title']/h2/text()").re(r'.+')[0]
        item['follow_count'] = int(response.xpath('//*[@id="zh-question-side-header-wrap"]/text()').re(r'(\d+)')[0])
        answer_count = response.xpath('//div[@class="zh-answers-title clearfix"]/h3/text()').re(r'(\d+)')
        item['answer_count'] = int(answer_count[0]) if answer_count else 1
        yield item

