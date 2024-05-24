import scrapy


class PepSpider(scrapy.Spider):
    name = "pep"
    allowed_domains = ["peps.python.org"]
    start_urls = ["https://peps.python.org"]

    def parse(self, response):
        all_peps = response.xpath('//*[@id="numerical-index"]//a/@href')
        for pep_link in all_peps:
            yield response.follow(pep_link, callback=self.parse_pep)

    def parse_pep(self, response):
        yield {
            'number': int(response.xpath(
                '//*[@id="pep-page-section"]/header/ul/li[3]/text()').get(
            ).replace('PEP ', ' ').strip()),

            'name': response.css('.page-title::text').get(),

            'status': response.xpath(
                '//*[@id="pep-content"]/dl/dd[2]/abbr/text()').get()
        }
