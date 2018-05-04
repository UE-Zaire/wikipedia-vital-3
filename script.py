import scrapy


class BlogSpider(scrapy.Spider):
    name = 'blogspider'
    start_urls = ['https://en.wikipedia.org/wiki/Wikipedia:Vital_articles']

    custom_settings = {
        'DOWNLOAD_DELAY': 1,
    }
    is_first_url = True
    vital_pages = set()

    def parse(self, response):
        print('RUNNING PARSE')
        if self.is_first_url:
            self.is_first_url = False
            for title in response.css('.columns-3 a'):
                yield {'title': title.css('a ::text').extract_first()}
            for next_page in response.css('.columns-3 a'):
                self.vital_pages.add(next_page.css('a::attr(href)').extract_first())
                yield response.follow(next_page, self.parse)
            all_pages = open('code/pages list', 'w')
            all_pages.write('\n'.join([p[6:] for p in self.vital_pages]))
            all_pages.close()
            return
        else:
            urls = []
            title = response.css('#firstHeading::text').extract_first().replace(' ', '-')
            for url in response.css('a::attr(href)').extract():
                if url in self.vital_pages:
                    urls.append(url[6:])
            print(urls)
            url_file = open('code/' + title, 'w')
            url_file.write('\n'.join(urls))
            url_file.close()
