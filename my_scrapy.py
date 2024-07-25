import my_scrapy


class MySpider(my_scrapy.Spider):

    name = "MySpider"
    start_urls = ["https://quotes.toscrape.com"]

    def parse(self, response):
        result = response.xpath("//samll[@class='author']::/text()").get()
        print(result)
