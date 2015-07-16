# -*- coding: utf-8 -*-

# Scrapy settings for zhihu project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#     http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html
#     http://scrapy.readthedocs.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'zhihu'

SPIDER_MODULES = ['zhihu.spiders']
NEWSPIDER_MODULE = 'zhihu.spiders'


# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'zhihu (+http://www.yourdomain.com)'

# Configure maximum concurrent requests performed by Scrapy (default: 16)
#CONCURRENT_REQUESTS=32

# Configure a delay for requests for the same website (default: 0)
# See http://scrapy.readthedocs.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
DOWNLOAD_DELAY=0.25
# The download delay setting will honor only one of:
#CONCURRENT_REQUESTS_PER_DOMAIN=16
#CONCURRENT_REQUESTS_PER_IP=16

# Disable cookies (enabled by default)
COOKIES_ENABLED = True
# COOKIES_DEBUG = True

COOKIES={
    # '_za': '8b3bdb96-7784-451d-bfb0-726fba7c14b8',
    # 'q_c1': "bee7ddc5d3ea446ea2a9b7daf9ef1b14|1436940809000|1436940809000",
    # 'cap_id': "MTk4NWE0MGFjZWY3NDg1NDg2NGNiNjAwYmFlZmIzZDA=|1436940809|f825d3c97ae7c5f3a838c3904509fc7650965a63",
    # '_xsrf': '9310e9977866ce371bcd7c99c38310af',
    # '_gat': '1',
    # '__utmt': '1',
    # '__utma': '51854390.1083912520.1436938228.1436938228.1436938228.1',
    # '__utmb': '51854390.20.10.1436938228',
    # '__utmc': '51854390',
    # '__utmz': '51854390.1436938228.1.1.utmcsr=zhihu.com|utmccn=(referral)|utmcmd=referral|utmcct=/',
    # '__utmv': '51854390.000--|2=registration_date=20150715=1^3=entry_date=20150715=1',
    # '_ga': 'GA1.2.1083912520.1436938228',
    'z_c0': "QUJCTUViRHpZd2dYQUFBQVlRSlZUZWZCelZVOEtXOGFYZE4yaE4xWDBLVkY4U09xSWNiVFRRPT0=|1436955879|54180840244374e947f7a31187cfdf7306e7191f",
    # 'unlock_ticket': "QUJCTUViRHpZd2dYQUFBQVlRSlZUUU1pcGxXekhTQ0RWNm54Q2pSa1kwTUJTVktSMmYyTHRBPT0=|1436949243|09c05223d3e848ca8e7bbefd8d0c3e27d02c9062"
}

# Disable Telnet Console (enabled by default)
#TELNETCONSOLE_ENABLED=False

# Override the default request headers:
#DEFAULT_REQUEST_HEADERS = {
#   'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
#   'Accept-Language': 'en',
#}

# Enable or disable spider middlewares
# See http://scrapy.readthedocs.org/en/latest/topics/spider-middleware.html
#SPIDER_MIDDLEWARES = {
#    'zhihu.middlewares.MyCustomSpiderMiddleware': 543,
#}

# Enable or disable downloader middlewares
# See http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html
DOWNLOADER_MIDDLEWARES = {
    # 'zhihu.middlewares.MyCustomDownloaderMiddleware': 543,
    # 'zhihu.contrib.downloadmiddleware.google_cache.GoogleCacheMiddleware':50,
    # 'zhihu.contrib.downloadmiddleware.random_userproxy.ProxyMiddleware': 100,
    # 'scrapy.contrib.downloadermiddleware.httpproxy.HttpProxyMiddleware': 110,
    # 'scrapy.contrib.downloadermiddleware.useragent.UserAgentMiddleware': None,
    'zhihu.contrib.downloadmiddleware.rotate_useragent.RotateUserAgentMiddleware':400,
}

# Enable or disable extensions
# See http://scrapy.readthedocs.org/en/latest/topics/extensions.html
#EXTENSIONS = {
#    'scrapy.telnet.TelnetConsole': None,
#}

# Configure item pipelines
# See http://scrapy.readthedocs.org/en/latest/topics/item-pipeline.html

ITEM_PIPELINES = {'zhihu.pipelines.ZhihuPipeline': 300, }

MONGODB_SERVER = 'localhost'
MONGODB_PORT = 27017
MONGODB_DB = 'scrapy'
MONGODB_COLLECTION = 'zhihu'

# Enable and configure the AutoThrottle extension (disabled by default)
# See http://doc.scrapy.org/en/latest/topics/autothrottle.html
# NOTE: AutoThrottle will honour the standard settings for concurrency and delay
#AUTOTHROTTLE_ENABLED=True
# The initial download delay
#AUTOTHROTTLE_START_DELAY=5
# The maximum download delay to be set in case of high latencies
#AUTOTHROTTLE_MAX_DELAY=60
# Enable showing throttling stats for every response received:
#AUTOTHROTTLE_DEBUG=False

# Enable and configure HTTP caching (disabled by default)
# See http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
#HTTPCACHE_ENABLED=True
#HTTPCACHE_EXPIRATION_SECS=0
#HTTPCACHE_DIR='httpcache'
#HTTPCACHE_IGNORE_HTTP_CODES=[]
#HTTPCACHE_STORAGE='scrapy.extensions.httpcache.FilesystemCacheStorage'


PROXIES = [
    {'ip_port': '183.221.147.50:8123', 'user_pass': ''},
    {'ip_port': '117.136.234.12:80', 'user_pass': ''},
    {'ip_port': '117.136.234.8:80', 'user_pass': ''},
    {'ip_port': '117.136.234.18:80', 'user_pass': ''},
    {'ip_port': '117.136.234.6:80', 'user_pass': ''},
    {'ip_port': '117.136.234.3:80', 'user_pass': ''},
]


#广度优先
# DEPTH_PRIORITY = 1
# SCHEDULER_DISK_QUEUE = 'scrapy.squeue.PickleFifoDiskQueue'
# SCHEDULER_MEMORY_QUEUE = 'scrapy.squeue.FifoMemoryQueue'