import scrapy

from pep_parse.settings import ALLOWED_DOMAINS, NAME, START_URLS


class PepSpider(scrapy.Spider):
    name = NAME
    allowed_domains = [ALLOWED_DOMAINS]
    start_urls = [START_URLS]

    def parse(self, response):
        for pep_link in response.xpath('//*[@id="numerical-index"]//a/@href'):
            yield response.follow(pep_link, callback=self.parse_pep)

    def parse_pep(self, response):
        yield {
            'number': int(response.xpath(
                '//header/ul/li[3]/text()'
            ).get().replace('PEP ', ' ').strip()),

            'name': response.xpath(
                '//*[@class="page-title"]/text()'
            ).get(),

            'status': response.css(
                'dt:contains("Status")+dd abbr::text'
            ).get()
        }
