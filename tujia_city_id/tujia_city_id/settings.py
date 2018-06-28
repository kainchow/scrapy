# -*- coding: utf-8 -*-

# Scrapy settings for tujia_city_id project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://doc.scrapy.org/en/latest/topics/settings.html
#     https://doc.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://doc.scrapy.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'tujia_city_id'

SPIDER_MODULES = ['tujia_city_id.spiders']
NEWSPIDER_MODULE = 'tujia_city_id.spiders'


# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'tujia_city_id (+http://www.yourdomain.com)'

# Obey robots.txt rules
ROBOTSTXT_OBEY = False

# Configure maximum concurrent requests performed by Scrapy (default: 16)
#CONCURRENT_REQUESTS = 32

# Configure a delay for requests for the same website (default: 0)
# See https://doc.scrapy.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
#DOWNLOAD_DELAY = 3
# The download delay setting will honor only one of:
#CONCURRENT_REQUESTS_PER_DOMAIN = 16
#CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
#COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
#TELNETCONSOLE_ENABLED = False

# Override the default request headers:
DEFAULT_REQUEST_HEADERS = {
        'Accept': 'application/json, text/plain, */*',   'Accept-Encoding': 'gzip, deflate, br',     'Accept-Language': 'zh-CN,zh;q=0.9',    'Connection': 'keep-alive',     'Content-Type': 'application/json;charset=UTF-8',   'Cookie': 'tujia.com_PortalContext_LongerRefUrl=https://www.tujia.com/; _ga=GA1.2.1498618631.1527827618; gr_user_id=cc1920ec-45bf-4152-a57e-9231cf033187; bad_id797098a0-b29d-11e5-b3b1-49764155fe50=f41debe1-6554-11e8-b8e6-e1af0ad106ee; tujia.com_UserSessionId=c642202f-b4ae-4351-9930-36fd9b218bca; tujia.com_MobileContext_StatUVId=99bafd5b-8ad9-491f-ab8a-e72f1b0aa8ec; tujia.com_PortalContext_RefUrl=https://www.tujia.com/; tujia.com_PortalContext_LandingUrl=http://www.tujia.com/api/pchome/homepage; tujia.com_PortalContext_GuestCount=0; tujia.com_PortalContext_BedCount=0; tujia.com_PortalContext_RoomCount=0; _gid=GA1.2.2062072776.1529045257; Hm_lvt_405c96e7f6bed44fb846abfe1f65c6f5=1527827618,1528167118,1529045262; manualclose=1; tujia.com_PortalContext_StartDate=2018-6-15; tujia.com_PortalContext_EndDate=2018-6-16; tujia.com_PortalContext_DestinationId=45; gr_cs1_ca96d354-29c9-408f-b4e0-5a622bbe14ac=user_id%3A0; qimo_seosource_797098a0-b29d-11e5-b3b1-49764155fe50=%E7%AB%99%E5%86%85; qimo_seokeywords_797098a0-b29d-11e5-b3b1-49764155fe50=; accessId=797098a0-b29d-11e5-b3b1-49764155fe50; nice_id797098a0-b29d-11e5-b3b1-49764155fe50=15b36c31-7068-11e8-89fb-6174749c48c2; tujia.com_PortalContext_UserRegisterSource=1; tujia.com_PortalContext_VerifyCode=460c339a-865b-427c-8650-dc312c38397f; tujia.com_PortalContext_LoginErrorTimes=0; tujia.com_PortalContext_UserToken=506ea2c7-c143-4367-8542-f7f3de2dd810; tujia.com_PortalContext_UserId=11935958; tujia.com_MWebHttpContext_UserId=0; _gat=1; gr_cs1_b945d6e8-e105-4cc3-99ce-bdf3ce0ec703=user_id%3A11935958; gr_session_id_1fa38dc3b3e047ffa08b14193945e261=b945d6e8-e105-4cc3-99ce-bdf3ce0ec703_true; Hm_lpvt_405c96e7f6bed44fb846abfe1f65c6f5=1529046962; pageViewNum=7',     'Host': 'www.tujia.com',    'Referer': 'https://www.tujia.com/',    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.87 Safari/537.36'
        }

# Enable or disable spider middlewares
# See https://doc.scrapy.org/en/latest/topics/spider-middleware.html
#SPIDER_MIDDLEWARES = {
#    'tujia_city_id.middlewares.TujiaCityIdSpiderMiddleware': 543,
#}

# Enable or disable downloader middlewares
# See https://doc.scrapy.org/en/latest/topics/downloader-middleware.html
#DOWNLOADER_MIDDLEWARES = {
#    'tujia_city_id.middlewares.TujiaCityIdDownloaderMiddleware': 543,
#}

# Enable or disable extensions
# See https://doc.scrapy.org/en/latest/topics/extensions.html
#EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
#}

# Configure item pipelines
# See https://doc.scrapy.org/en/latest/topics/item-pipeline.html
ITEM_PIPELINES = {
    'tujia_city_id.pipelines.MySQLPipeline': 300,
}

# Enable and configure the AutoThrottle extension (disabled by default)
# See https://doc.scrapy.org/en/latest/topics/autothrottle.html
#AUTOTHROTTLE_ENABLED = True
# The initial download delay
#AUTOTHROTTLE_START_DELAY = 5
# The maximum download delay to be set in case of high latencies
#AUTOTHROTTLE_MAX_DELAY = 60
# The average number of requests Scrapy should be sending in parallel to
# each remote server
#AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
#AUTOTHROTTLE_DEBUG = False

# Enable and configure HTTP caching (disabled by default)
# See https://doc.scrapy.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
#HTTPCACHE_ENABLED = True
#HTTPCACHE_EXPIRATION_SECS = 0
#HTTPCACHE_DIR = 'httpcache'
#HTTPCACHE_IGNORE_HTTP_CODES = []
#HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'

MYSQL_USER = 'root'
MYSQL_PASSWORD = '123456'
MYSQL_DB = 'locals'
