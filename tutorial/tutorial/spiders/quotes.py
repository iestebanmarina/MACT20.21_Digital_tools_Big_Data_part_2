import scrapy


class QuotesSpider(scrapy.Spider):
    name = "quotes_a"

    def start_requests(self):
        urls = [
            'https://energia.barcelona/ca/quanta-energia-pots-generar'
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        page = response.url.split("/")[-2]
        filename = f'quotes-{page}.html'
        with open(filename, 'wb') as f:
            f.write(response.body)
        self.log(f'Saved file {filename}')