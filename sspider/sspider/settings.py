# Scrapy settings for sspider project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#

BOT_NAME = 'sspider'

SPIDER_MODULES = ['sspider.spiders']
NEWSPIDER_MODULE = 'sspider.spiders'

DEPTH_LIMIT = 1
# Crawl responsibly by identifying yourself (and your website) on the user-agent
USER_AGENT = 'Chrome/18.0.1025.133'
